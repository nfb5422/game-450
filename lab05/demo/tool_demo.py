from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[2]))

import requests
from util.llm_utils import TemplateChat

# beauty of Python
def process_function_call(function_call):
    name = function_call.name
    args = function_call.arguments

    return globals()[name](**args)

def get_weather(city):
    city_data = requests.get(f'https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en&format=json')
    city_lat = city_data.json()['results'][0]['latitude']
    city_lon = city_data.json()['results'][0]['longitude']
    weather_data = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={city_lat}&longitude={city_lon}&current=temperature_2m')
    curr_temp = str(weather_data.json()['current']['temperature_2m'])+str('°C')

    return f'The current temperature of {city} is {curr_temp}!'

chat = TemplateChat.from_file('lab05/demo/tool_template.json')

response = chat.completion(**{'ask': 'What is the weather in Paris?'})

if response.message.tool_calls:
    chat.messages.append({'role': 'tool',
                          'name': response.message.tool_calls[0].function.name, 
                          'arguments': response.message.tool_calls[0].function.arguments,
                          'content': process_function_call(response.message.tool_calls[0].function)
                         })
    response = chat.completion()

print(response.message.content)

