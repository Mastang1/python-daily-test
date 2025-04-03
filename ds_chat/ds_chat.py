from deepseek.api import DeepSeekAPI
import os,sys,json
import configparser
import platform

from rich.console import Console
from rich.markdown import Markdown

#This is the config file path, and you can change it to your own config file path
config_path = r"D:/workspace/OpenSrc/notes_typ/my_key_dk.ini"
DEEPSEEK_API_URL = 'https://api.deepseek.com/v1/chat/completions'
TRANS_SYS_PROM =  "你是一个中英文翻译专家，将用户输入的中文翻译成英文，或将用户输入的英文翻译成中文。对于非中文内容，它将提供中文翻译结果。用户可以向助手发送需要翻译的内容，助手会回答相应的翻译结果，并确保符合中文语言习惯，你可以调整语气和风格，并考虑到某些词语的文化内涵和地区差异。同时作为翻译家，需将原文翻译成具有信达雅标准的译文。\"信\" 即忠实于原文的内容与意图；\"达\" 意味着译文应通顺易懂，表达清晰；\"雅\" 则追求译文的文化审美和语言的优美。目标是创作出既忠于原作精神，又符合目标语言文化和读者审美的翻译。"
CHAT_SYS_PROM = r"你是智能助手，请把应答以markdown格式输出，并尽量采用python rich库可以渲染的格式， 终端会用rich库渲染markdown格式的文本，输出风格要具有设计感，要符合markdown语法"
EOF_OF_QUESTION = ":::"

def print_markdown(text):
    console = Console()
    markdown = Markdown(text)
    console.print(markdown)
def input_mltiline(eof=EOF_OF_QUESTION):
    lines = []
    while True:
        line = input()
        if line.lower().strip()[-3:] == eof:
            break
        lines.append(line)

    code = "".join(lines)
    return code

def is_windows():
    return platform.system() == 'Windows'

def is_linux():
    return platform.system() == 'Linux'

def is_mac():
    return platform.system() == 'Darwin'

def get_key():
    config = configparser.ConfigParser()
    config.read(config_path)
    try:
        return config.get('DeepSeek', 'api_key')
    except (configparser.NoSectionError, configparser.NoOptionError):
        raise Exception("API Key not found in config.ini")

class DeepSeekChat:
    def __init__(self, api_key=""):
        self.api = DeepSeekAPI(api_key)
    
    def start_chat(self):
        print("DeepSeek Chat - Type 'exit' to quit")
        while True:
            print("\nQ: > ")
            user_input = input_mltiline()
            print("\n")
            
            if user_input.lower() in ["exit", "quit"]:
                print("Goodbye!")
                break

            print("query".center(80, '*'))
            if user_input.lower() == 'balance':
                json_balance = self.api.user_balance()
                print(f"Balance: {json_balance}")   
                continue
            if user_input.lower().split("#")[0] in 'translate' and len(user_input.lower().split("#")[0]) >= 2:
                try:
                    response = self.api.chat_completion(prompt=user_input.lower().split("#")[1] , stream=False, prompt_sys=TRANS_SYS_PROM)
                    print_markdown(f"A: >\n {response}")
                except Exception as e:
                    print(f"Error: {str(e)}")
                finally:
                    continue
            if user_input.lower() == 'clear':
                if is_windows:
                    os.system('cls')
                else:
                    os.system('clear')
                continue

            if user_input.lower().split("#")[0] in "stream":
                try:
                    print("\n")
                    print("A: > \n")
                    # Enable streaming response
                    for chunk in self.api.chat_completion(prompt=user_input, stream=True, prompt_sys="you are a smart assistant"):
                        print(chunk, end='', flush=True)
                    print("\n"*2)
                except Exception as e:
                    print(f"Error: {str(e)}")

            else:
                try:
                    response = self.api.chat_completion(prompt=user_input, stream=False, prompt_sys=CHAT_SYS_PROM)
                    print("\n")
                    print("A: > \n")
                    print_markdown(f"\n {response}")
                    print("\n"*2)
                except Exception as e:
                    print(f"Error: {str(e)}")

if __name__ == "__main__":
    chat = DeepSeekChat(api_key=get_key())
    chat.start_chat()
