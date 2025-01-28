import re
import json
import ollama
import hashlib
import logging

from pathlib import Path

ollama_seed = lambda x: int(str(int(hashlib.sha512(x.encode()).hexdigest(), 16))[:8])

def pretty_stringify_chat(messages):
  stringified_chat = ''
  for message in messages:
      role = message["role"].capitalize()
      content = message["content"]
      stringified_chat += f"{role}: {content}\n\n\n"
  return stringified_chat

def insert_params(string, **kwargs):
    pattern = r"{{(.*?)}}"
    matches = re.findall(pattern, string)
    for match in matches:
        replacement = kwargs.get(match.strip())
        if replacement is not None:
            string = string.replace("{{" + match + "}}", replacement)
    return string

class ChatTemplate:
    def __init__(self, template, sign=None, end_regex=None):
        self.instance = template
        self.instance['options']['seed'] = hash(str(sign))
        self.end_regex = end_regex
        self.messages = self.instance['messages']

    def from_file(template_file, sign=None, end_regex=None):
        with open(Path(template_file), 'r') as f:
            template = json.load(f)

        return ChatTemplate(template, sign, end_regex)

    def chat(self, **kwargs):
        response = self.completion(**kwargs)
        message = response['message']
        self.messages.append({'role': message.role, 'content': message.content})
        logging.info(f'{message.role}: {message.content}')

        if self.end_regex is not None:
            ending_match = self.check_ending(message.content)
            if ending_match:
                return message.content, ending_match

        return response 

    def completion(self, **parameters):
        for item in self.instance['messages']:
            item['content'] = insert_params(item['content'], **parameters)

        return ollama.chat(**self.instance)
    
    def check_ending(self, message):
        if match:=re.search(self.end_regex, message, re.DOTALL):
            return match[0]
        else:
            return False
    