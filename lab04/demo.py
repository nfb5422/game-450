from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parents[1]))

from lab04 import run_console_chat

if __name__ ==  '__main__':
    #  run lab04.py to test your template
    recruit_template_file = 'lab04/demo_template.json'
    run_console_chat(template_file=recruit_template_file,
                     recruit_difficulty='not easy',
                     reward='a sword',
                     sign='Pulin',
                     end_regex=r'RECRUIT(.*)DONE')