from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MultiGrid
from mesa.datacollection import DataCollector
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import Slider
from llm_connection import LLM_executor


class TalkingAgent(Agent):
    def __init__(self, unique_id, model, group, policy, positive, negative, scenario):
        super().__init__(unique_id, model)
        self.group = group
        self.policy = policy
        self.positive = positive
        self.negative = negative
        self.scenario = scenario

    def step(self):
        self.talk_and_decide()

    def talk_and_decide(self):

        def check_and_change(deci):
            if 'POSITIVE' in deci.upper():
                self.group = 'positive'
            elif 'NEGATIVE' in deci.upper():
                self.group = 'negative'
            elif 'NEUTRAL' in deci.upper():
                self.group = 'negative'

        def log_info(info_msg, llm_answer):
            print('--------'+info_msg.upper()+'--------')
            print(llm_answer)

        if self.scenario == 1:
            if self.group != 'neutral':
                pass
            else:
                other_agent = self.random.choice([agent for agent in self.model.schedule.agents if agent.group != 'neutral'])

                opinion = ''
                if(other_agent.group == 'positive'):
                    prompt = 'Act like a person. Generate a positive opinion about this policy, to convince neutral people towards it: ' + self.policy + '. An example could be: ' + self.positive
                    opinion = self.model._llm_executor.get_answer(prompt)
                    log_info('agent {} is proposing a positive opinion'.format(other_agent.unique_id), opinion)

                if(other_agent.group == 'negative'):
                    prompt = 'Act like a person. Generate a negative opinion about this policy, to convince neutral people towards it: ' + self.policy + '. An example could be: ' + self.negative
                    opinion = self.model._llm_executor.get_answer(prompt)
                    log_info('agent {} is proposing a negative opinion'.format(other_agent.unique_id), opinion)

                prompt = 'You are a {} agent deciding on this policy: '.format(self.unique_id) + self.policy + '. Here is an opinion other person says to you: ' + opinion + '. Answer with POSITIVE, NEGATIVE or NEUTRAL to decide your vote on the policy.'
                deci = self.model._llm_executor.get_answer(prompt)
                
                log_info('agent {} has made a decision'.format(self.unique_id), deci)

                check_and_change(deci)

        if self.scenario == 2:
            if self.group != 'negative':
                pass
            else:
                other_agent = self.random.choice([agent for agent in self.model.schedule.agents if agent.group != 'negative'])

                opinion = ''
                if(other_agent.group == 'positive'):
                    prompt = 'Act like a person. Generate a positive opinion about this policy, to convince negative people towards it: ' + self.policy + '. An example could be: ' + self.positive
                    opinion = self.model._llm_executor.get_answer(prompt)
                    log_info('agent {} is proposing a positive opinion'.format(other_agent.unique_id), opinion)

                if(other_agent.group == 'neutral'):
                    prompt = 'Act like a person. Generate a neutral opinion about this policy, to convince negative people towards it: ' + self.policy + '.'
                    opinion = self.model._llm_executor.get_answer(prompt)
                    log_info('agent {} is proposing a neutral opinion'.format(other_agent.unique_id), opinion)

                prompt = 'You are a {} agent deciding on this policy: '.format(self.unique_id) + self.policy + '. Here is an opinion other person says to you: ' + opinion + '. Answer with POSITIVE, NEGATIVE or NEUTRAL to decide your vote on the policy.'
                deci = self.model._llm_executor.get_answer(prompt)
                
                log_info('agent {} has made a decision'.format(self.unique_id), deci)

                check_and_change(deci)

        if self.scenario == 3:
            if self.group != 'positive':
                pass
            else:
                other_agent = self.random.choice([agent for agent in self.model.schedule.agents if agent.group != 'positive'])

                opinion = ''
                if(other_agent.group == 'negative'):
                    prompt = 'Act like a person. Generate a negative opinion about this policy, to convince positive people towards it: ' + self.policy + '. An example could be: ' + self.negative
                    opinion = self.model._llm_executor.get_answer(prompt)
                    log_info('agent {} is proposing a negative opinion'.format(other_agent.unique_id), opinion)

                if(other_agent.group == 'neutral'):
                    prompt = 'Act like a person. Generate a neutral opinion about this policy, to convince positive people towards it: ' + self.policy + '.'
                    opinion = self.model._llm_executor.get_answer(prompt)
                    log_info('agent {} is proposing a neutral opinion'.format(other_agent.unique_id), opinion)

                prompt = 'You are a {} agent deciding on this policy: '.format(self.unique_id) + self.policy + '. Here is an opinion other person says to you: ' + opinion + '. Answer with POSITIVE, NEGATIVE or NEUTRAL to decide your vote on the policy.'
                deci = self.model._llm_executor.get_answer(prompt)
                
                log_info('agent {} has made a decision'.format(self.unique_id), deci)

                check_and_change(deci)

        if self.scenario == 4:
                other_agent = self.random.choice(self.model.schedule.agents)

                opinion = ''
                if(other_agent.group == 'negative'):
                    prompt = 'Act like a person. Generate a negative opinion about this policy, to convince positive people towards it: ' + self.policy + '. An example could be: ' + self.negative
                    opinion = self.model._llm_executor.get_answer(prompt)
                    log_info('agent {} is proposing a negative opinion'.format(other_agent.unique_id), opinion)

                if(other_agent.group == 'neutral'):
                    prompt = 'Act like a person. Generate a neutral opinion about this policy, to convince positive people towards it: ' + self.policy + '.'
                    opinion = self.model._llm_executor.get_answer(prompt)
                    log_info('agent {} is proposing a neutral opinion'.format(other_agent.unique_id), opinion)

                if(other_agent.group == 'positive'):
                    prompt = 'Act like a person. Generate a positive opinion about this policy, to convince negative people towards it: ' + self.policy + '. An example could be: ' + self.positive
                    opinion = self.model._llm_executor.get_answer(prompt)
                    log_info('agent {} is proposing a positive opinion'.format(other_agent.unique_id), opinion)

                prompt = 'You are a {} agent deciding on this policy: '.format(self.unique_id) + self.policy + '. Here is an opinion other person says to you: ' + opinion + '. Answer with POSITIVE, NEGATIVE or NEUTRAL to decide your vote on the policy.'
                deci = self.model._llm_executor.get_answer(prompt)
                
                log_info('agent {} has made a decision'.format(self.unique_id), deci)

                check_and_change(deci)


class TalkingModel(Model):
    def __init__(self, Scenario, Np, Nn, Nneu, policy, positive, negative):
        super().__init__()

        self._llm_executor = LLM_executor()

        self.num_agents = Np + Nn + Nneu
        self.grid = MultiGrid(10, 10, True)
        self.schedule = RandomActivation(self)

        group_positions = {
            "positive": (range(0, 5), range(0, 5)),
            "negative": (range(5, 10), range(0, 5)),
            "neutral": (range(0, 10), range(5, 10))
        }

        def instatiate_agent(group):
            agent = TalkingAgent(i, self, group, policy, positive, negative, Scenario)
            self.schedule.add(agent)
            x_range, y_range = group_positions[group]
            x = self.random.choice(x_range)
            y = self.random.choice(y_range)
            self.grid.place_agent(agent, (x, y))

        for i in range(Np):
            instatiate_agent("positive")

        for i in range(Nn):
            instatiate_agent("negative")

        for i in range(Nneu):
            instatiate_agent("neutral")


        self.datacollector = DataCollector(
            model_reporters={"positive": lambda m : len([agent for agent in m.agents if agent.group == "positive"]),
                    "negative":  lambda m : len([agent for agent in m.agents if agent.group == "negative"]),
                    "neutral":  lambda m : len([agent for agent in m.agents if agent.group == "neutral"])},
        )

        self.datacollector.collect(self)

    def step(self):
        self.datacollector.collect(self)
        self.schedule.step()


def agent_portrayal(agent):
    portrayal = {"Shape": "circle", "Filled": "true", "r": 0.5, "Layer": 0}
    if agent.group == "positive":
        portrayal["Color"] = "green"
    elif agent.group == "negative":
        portrayal["Color"] = "red"
    else:
        portrayal["Color"] = "blue"
    return portrayal


class TalkingAgentsABM:
    def __init__(self, policy, positive, negative):
        grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
        chart = ChartModule([{"Label": "positive", "Color": "green"},
                     {"Label": "negative", "Color": "red"},
                     {"Label": "neutral", "Color": "blue"}],
                    data_collector_name='datacollector')
        
        model_params = {
            "Scenario": Slider("Scenario", 1, 1, 4, 1),
            "Np": Slider("Number of positive agents", 6, 3, 24, 3),
            "Nn": Slider("Number of negative agents", 6, 3, 24, 3),
            "Nneu": Slider("Number of neutral agents", 6, 3, 24, 3),
            "policy": policy,
            "positive": positive,
            "negative": negative
        }

        self.server = ModularServer(TalkingModel,
                                    [grid, chart],
                                    "Talking Agents Model",
                                    model_params)
    
    def get_abm_server(self):
        return self.server
