import os
import sys
import time
from typing import List, Dict

from openai import OpenAI, APIConnectionError, RateLimitError, APIStatusError
from dotenv import load_dotenv
from colorama import init, Fore, Style

# 初始化颜色库
init(autoreset=True)

# 加载环境变量
load_dotenv()

class VCChatAssistant:
    def __init__(self):
        """
        初始化助手，配置DeepSeek客户端和系统提示词
        """
        self.api_key = os.getenv("DEEPSEEK_API_KEY")
        if not self.api_key:
            print(f"{Fore.RED}错误: 未找到 DEEPSEEK_API_KEY 环境变量。请在 .env 文件中配置。")
            sys.exit(1)

        # DeepSeek 使用 OpenAI 兼容接口
        self.client = OpenAI(
            api_key=self.api_key,
            base_url="https://api.deepseek.com"
        )

        # 核心：定义金融/舆情分析专用的系统提示词
        self.system_prompt = {
            "role": "system",
            "content": (
                "你是一位拥有20年经验的资深金融风投合伙人及舆情危机分析专家。"
                "你的目标是辅助用户进行投资决策和市场情绪判断。"
                "请遵循以下回答原则："
                "1. 【专业性】：使用专业的金融分析框架（如SWOT, PESTEL, 波特五力）进行拆解。"
                "2. 【敏锐度】：从新闻或舆情中识别潜在的投资机会（Alpha）或风险信号（Red Flags）。"
                "3. 【结构化】：回答必须逻辑清晰，采用'核心观点 -> 数据/证据 -> 结论/建议'的结构。"
                "4. 【客观性】：保持中立，区分'事实'与'情绪'，对市场噪音进行降噪处理。"
                "5. 【简洁】：在命令行环境中，尽量言简意赅，重点突出。"
            )
        }

        # 维护对话历史
        self.messages: List[Dict[str, str]] = [self.system_prompt]

    def _get_response_stream(self, user_input: str):
        """
        处理API请求，支持流式输出和错误重试
        """
        self.messages.append({"role": "user", "content": user_input})

        max_retries = 3
        attempt = 0

        while attempt < max_retries:
            try:
                # 调用 DeepSeek API
                stream = self.client.chat.completions.create(
                    model="deepseek-chat", # 或者 deepseek-reasoner
                    messages=self.messages,
                    stream=True, # 开启流式输出，提升用户体验
                    temperature=1.3 # 设置为1.3以获得更有创意的分析，若需严谨数据可调低至0.7
                )
                return stream

            except APIConnectionError as e:
                attempt += 1
                print(f"{Fore.YELLOW}\n[网络波动] 连接服务器失败，正在重试 ({attempt}/{max_retries})...")
                time.sleep(2)
            except RateLimitError as e:
                print(f"{Fore.RED}\n[请求受限] API调用频率过高，请稍后重试。")
                return None
            except APIStatusError as e:
                print(f"{Fore.RED}\n[API错误] 状态码: {e.status_code}, 信息: {e.message}")
                return None
            except Exception as e:
                print(f"{Fore.RED}\n[未知错误] {str(e)}")
                return None
        
        print(f"{Fore.RED}\n[失败] 多次重试失败，请检查网络连接。")
        return None

    def chat_loop(self):
        """
        主聊天循环
        """
        print(f"{Style.BRIGHT}{Fore.CYAN}="*60)
        print(f"DeepSeek 金融风投与舆情分析助手 [v1.0] (已连接)")
        print(f"输入 'exit' 或 'quit' 退出程序")
        print(f"输入 'clear' 清空上下文记忆")
        print(f"{Style.BRIGHT}{Fore.CYAN}="*60 + "\n")

        while True:
            try:
                user_input = input(f"{Fore.GREEN}您 (User): {Style.RESET_ALL}").strip()

                if not user_input:
                    continue

                if user_input.lower() in ['exit', 'quit']:
                    print(f"{Fore.CYAN}再见！祝您投资顺利。")
                    break
                
                if user_input.lower() == 'clear':
                    self.messages = [self.system_prompt]
                    print(f"{Fore.YELLOW}>>> 上下文记忆已清空 <<<")
                    continue

                print(f"{Fore.BLUE}分析师 (AI): {Style.RESET_ALL}", end="", flush=True)

                stream = self._get_response_stream(user_input)
                
                if stream:
                    full_response = ""
                    # 处理流式响应
                    for chunk in stream:
                        if chunk.choices[0].delta.content is not None:
                            content = chunk.choices[0].delta.content
                            print(content, end="", flush=True)
                            full_response += content
                    
                    print("\n") # 换行
                    # 将助手的完整回答加入历史记录
                    self.messages.append({"role": "assistant", "content": full_response})
                
            except KeyboardInterrupt:
                print(f"\n{Fore.CYAN}程序已终止。")
                break

if __name__ == "__main__":
    assistant = VCChatAssistant()
    assistant.chat_loop()