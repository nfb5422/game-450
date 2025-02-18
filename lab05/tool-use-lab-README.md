# Tool Use Lab

## Intro to Tool Use
Tool use in the context of language models refers to the ability of these models to interact with external tools or APIs to perform specific tasks. This capability allows language models to extend their functionality beyond generating text, enabling them to execute actions, retrieve information, and manipulate data in real-time. Tool use is particularly valuable for applications that require dynamic responses or interactions with external systems, such as chatbots, virtual assistants, and automated workflows.

## Lab Task

NOTE: Please don't change my code. Only edit the files that have the name of the lab and in places where the comments ask for it.

Based on the example shown, create an agent that can perform skill check based dice rolls for DnD. The agent should be able to roll a dice and sucessfully create the next response based on the tool's output.

Ensure that template provides the tool information to the ollama model like in `demo/tool_template.json`.

Fill out the `process_response` method that will used in the TemplateChat._chat_generator() function. 

Before submitting the commit link, ensure that the agent is able to make correct tool calls by ensuring that you see somethign like the following on the console after the player's message.

```
Tools Called: 
 defaultdict(<class 'list'>, {'process_function_call_calls': [{'name': 'process_function_call', 'args': (Function(name='roll_for', arguments={'dc': 5, 'player': 'adventurer', 'skill': 'Athletics'}),), 'kwargs': {}, 'result': 'adventurer rolled 7 for Athletics and succeeded!'}]}) 
```

Last and the most important part of lab task, add a comment to the canvas submission imagining what a possible wonderful but realistic use of tool calling can be. (30% points)