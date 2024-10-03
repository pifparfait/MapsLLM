# Talking Agents

**Talking Agents** is a project designed to simulate policy discussions using agents based on large language models (LLMs). The agents represent different viewpoints (positive, neutral, and negative) on various topics and generate responses based on those perspectives. This project allows for the exploration of how LLMs can simulate decision-making processes, and how different inputs affect agent behavior.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributors](#contributors)
- [License](#license)

## Project Overview

This repository contains the source code for simulating conversations between agents discussing policies. Each agent responds with its own perspective (positive, neutral, or negative) on a given policy or topic. The primary goal is to evaluate how different policies are perceived and how LLMs can be used in decision-making simulations.

## Features

- **LLM Integration**: The project uses advanced language models to generate agent responses.
- **Customizable Scenarios**: Easily create new policy discussions by changing inputs.
- **Agent Perspectives**: Agents represent different viewpoints, including positive, neutral, and negative perceptions.
- **Policy Exploration**: Explore how different agents might respond to policies on various topics.
- **Jupyter Notebook Support**: Includes a Jupyter notebook for interactive development and testing.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/talking-agents.git
   cd talking-agents
2. **Create a virtual environment**:
   ```bash
   pyenv virtualenv 3.10.0 myenv310
   pyenv activate myenv310
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
4. **Pull the necessary Ollama distribution (required for LLM)**:
   ```bash
   ollama pull qwen2.5:0.5b
   
## Usage

1. **Run the Python script to simulate agents' discussions**:
   ```bash
   python talking_agents.py
2. **Explore the Jupyter notebook for interactive exploration:**:
   ```bash
   jupyter notebook talking_agents.ipynb
3. Modify the `policy_to_discuss` in the Python file or notebook to simulate different policies and agents' responses.

## Project Structure

- `abm.py`: Agent-based modeling scripts.
- `llm_connection.py`: Script for integrating language models with agents.
- `talking_agents.py`: Main script to run agent simulations.
- `talking_agents.ipynb`: Jupyter notebook for interactive exploration.
- `requirements.txt`: List of required Python packages for the project.

## Contributors
- **Adrian Mora** - [amcarrero](https://github.com/amcarrero)
- **Parfait Atchadé** - [pipfarfait](https://github.com/pipfarfait)


## License

This project is licensed under the MIT License - see the LICENSE file for details.
```
You can copy and paste this directly into your `README.md` file in VS Code or GitHub. Let me know if you need any further modifications!
