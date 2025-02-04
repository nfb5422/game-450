from math import exp
from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[2]))

import json
import pytest
from jsondiff import diff
from util.llm_utils import TemplateChat
from lab04.lab04 import lab04_params

def load_test_data(file_path="lab04/test/test_scenarios.json"):
    with open(Path(file_path), 'r') as f:
        return json.load(f)

@pytest.mark.parametrize("scenario", load_test_data())
def test_scenario(scenario):
    """
    For each scenario, we want to simulate a conversation that leads to
    an ORDER ... DONE line, then confirm the final JSON matches scenario["response"].
    """

    # 1) Prepare scenario data:
    inventory = json.dumps(scenario["inventory"])
    ask = scenario["ask"]
    expected_response = scenario["response"]

    customer_template_file = 'lab04/test/customer_chat.json'
    customer = TemplateChat.from_file(customer_template_file, sign='Pulin', ask=ask)
    lab04_params['inventory']= inventory
    trader = TemplateChat.from_file(**lab04_params)
    chat_generator = trader.start_chat()
    print(next(chat_generator))
    while True:
        try:
            cust_message = customer.chat_turn().message.content
            print(f"Customer: {cust_message}")
            message = chat_generator.send(cust_message).strip()
            print(f"Trader: {message}")
            customer.instance['messages'].append({'role': 'assistant', 'content': cust_message})
            customer.instance['messages'].append({'role': 'user', 'content': message})
        except StopIteration as e:
            print(f"Trader: {e.value[0]}")
            result = e.value[1]
            break

    # Compare to what we expect
    print('Output: ',result)
    print('Expected: ',expected_response)
    assert not diff(json.loads(result), expected_response)

if __name__ == "__main__":
    test_scenario(
        {
            "inventory": ["mana potion", "health potion"],
            "ask": "One health potion and two mana potions",
            "response": ["health potion", "mana potion", "mana potion"],
        }
    )
