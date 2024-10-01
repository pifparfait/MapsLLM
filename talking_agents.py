policy_to_discuss = '''
Should MIT require all students to take a class on ethics?
'''

positive_perception = '''
Ethics is a fundamental part of any profession. It is important for students to understand the ethical implications of their work.
'''

negative_perception = '''
Students are already overburdened with classes. Adding another requirement would be too much.
'''

# scenario 1: neutrals talk with positive and negative (only neutrals change their opinion)
# scenario 2: negatives talk with positive and neutral (only negatives change their opinion)
# scenario 3: positives talk with neutral and negative (only positives change their opinion)
# scenario 4: everyone talks with everyone

from abm import TalkingAgentsABM

abm = TalkingAgentsABM(policy_to_discuss, positive_perception, negative_perception)
abm.get_abm_server().launch()