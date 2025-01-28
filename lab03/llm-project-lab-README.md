# LLM and Project Lab

## Intro to Large Language Models (LLM)
Large Language Models (LLMs) are a type of artificial intelligence model designed to understand and generate human language. These models are trained on vast amounts of text data and can perform a variety of tasks such as translation, summarization, question answering, and more. LLMs leverage deep learning techniques to capture the nuances of language, making them powerful tools for natural language processing applications.

## Course Project
Create an AI based DnD Dungeon Master (DM) to allow you to play DnD with your friends without needing someone to be a DM. The Dungeon Master will be able to generate a story, create NPC characters, manage the game world, and make appropriate changes to the player character sheets. The project will be broken down into several milestones, each building on the previous one to create a fully functional DnD Dungeon Master.

Note: This project is designed to be a fun and interactive way to apply the concepts you have learned in the course. Feel free to get creative and experiment with different ideas to enhance the project.

Note: You are free to not use DnD as the theme for your project. You can make it a general text-based adventure game if you prefer or something else entirely. But the project should use all the technologies that are expected in the project. Look at the project rubric for more details.

## Capabilities of the DnD Dungeon Master
1. Generate a random story
2. Create NPC characters
3. Manage the game world
4. Make changes to player character sheets
5. Implement a turn-based combat system

##  Scaffolding
As a part of lab03 you are provided with a basic scaffolding for the project. The scaffolding includes the following:

1. Networked game server and client (Dungeon Master Server and Player Client) `utils/dndnetwork.py`
2. Chat template for a DnD llm agent `utils/templates/dm_chat.json`
3. A basic DungeonMaster and Player class that allow you to use the networked game server and client `utils/base.py`

## This Lab

In this lab you will create a basic DnD agent using `lab03_dnd_agent.py` that should allow a single player to play DnD with the Dungeon Master. You will write the basic code for the flow of the chat in `lab03_dnd_agent.py` based on the code in `demo_agent.py`. You can use various system prompts and model hyperparameters that you learned about in class to improve the agent. 

As you run `dnd_agent.py` remember to gracefully exit the program by typing '/exit' in the chat. This is crucial for grading purposes.

You will edit the file `lab03.md` with your reflections on the things that you tried and the effects that it had on the game experience. It is ok, as far as evidence of iterative improvement rubric goes, if your code was doing something right but by removing something it became worse as long as you document it. 

## Learning Objectives

1. Understand the basic workflow of communication with an LLM model. 
2. Understand the input to an LLM as a series of messages and the message format.
3. Ability to use an appropriate model and model parameters to improve the chat experience.

## Lab Task
1. Add your reflection to `lab03.md`
2. Add `lab03_dnd_agent.py`, `lab03.md` and `attempts.txt` to your commit.
3. Submit your commit link to the lab03 submission on Canvas.

## Lab03 Grading Rubric

1. __Evidence of Iterative Improvement__: Measures how well each iteration builds on the previous, highlighting specific changes and improvements made along the way.

2. __Analytical Depth__: Looks at how thoroughly the student investigates the causes of issues or successes, using data or logical reasoning to guide conclusions.

3. __Clarity of Ideas__: Focuses on how effectively the student communicates their thought process, ensuring the reflection is organized and easy to follow.