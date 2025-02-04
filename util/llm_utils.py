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

class TemplateChat:
    def __init__(self, template, sign=None, **kwargs):
        self.instance = template
        self.instance['options']['seed'] = hash(str(sign))
        self.messages = self.instance['messages']
        self.end_regex = kwargs['end_regex'] if 'end_regex' in kwargs else None
        self.parameters = kwargs

    def from_file(template_file, sign=None, **kwargs):
        with open(Path(template_file), 'r') as f:
            template = json.load(f)

        return TemplateChat(template, sign, **kwargs)

    def completion(self, **kwargs):
        self.parameters |= kwargs
        for item in self.instance['messages']:
            item['content'] = insert_params(item['content'], **self.parameters)

        return ollama.chat(**self.instance)

    def chat_turn(self, **kwargs):
        response = self.completion(**kwargs)
        message = response['message']
        self.messages.append({'role': message.role, 'content': message.content})
        logging.info(f'{message.role}: {message.content}')
        return response 

    def start_chat(self, **kwargs):
        while True:
            response = self.chat_turn(**kwargs)

            if self.end_regex:
                if match:=re.search(self.end_regex, response.message.content, re.DOTALL):
                    return response.message.content, match.group(1).strip()

            prompt = yield response.message.content

            logging.info(f'User: {prompt}')
            self.instance['messages'].append({'role': 'user', 'content': prompt})
            if prompt == '/exit':
                break