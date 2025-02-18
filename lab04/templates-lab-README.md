# Prompt Engineering and Templates Lab  

## Introduction to Templates
Templates are pre-defined structures or formats that can be used to reuse well engineered prompts to generate consistent and coherent text. They provide a framework for organizing information and ensuring that the output follows a specific style or tone. 

## Demo
File 'demo.py' shows the use of templates to create different types of recruitable agents.

## Lab Tasks
1. Edit `lab04_trader_chat.json` to create a prompt template for a DnD trader that successfully executes the trade. 
2. The `lab04_params` dictionary will be read by the testing framework to load your json and supporting parameter.
  - At the minimum, you will need `'template_file'`, `'sign'` and `'end_regex'` keys set in the `lab04_params`.  
3. You can experience your trader agent by completing the "main" and running `lab04.py`.
1. Sign your name in `lab04.py` to make your tests reproducible.
4. Run the tests using **pytest** framework in VSCode to ensure that it passes most of the tests in `lab04/tests/test_trader.py`
5. Show the status of some tests in VSCode to the instructor during the lab.
6. Upload a screenshot of status of tests in VSCode along with the commit hash in the textbox for for URL on Canvas.


## Lab04 Grading Rubric

1. __Status of Test Cases__: Measures how many test cases pass based on the prompt template created.