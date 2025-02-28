import requests 
import json 
import configparser

# ... existing code ...
# DeepSeek API credentials
config_path = "D:\\workspace\\OpenSrc\\notes_typ\\my_key_dk.ini"
DEEPSEEK_API_URL = 'https://api.deepseek.com/v1/chat/completions'

def get_key():
    config = configparser.ConfigParser()
    config.read(config_path)
    try:
        return config.get('DeepSeek', 'api_key')
    except (configparser.NoSectionError, configparser.NoOptionError):
        raise Exception("API Key not found in config.ini")
    
def chat_with_deepseek(prompt, key):
    headers = {
        'Authorization': f'Bearer {key}',
        'Content-Type': 'application/json'
    }
    # Update request data structure
    data = {
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        'model': 'deepseek-chat',
        'temperature': 0.5,
        # 'max_tokens': 4096
    }
    
    # ... rest of the function remains unchanged ...
    
    # API endpoint
    response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        # Parse response content
        return response.json().get('choices', [{}])[0].get('message', {}).get('content', '')
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

def main():
    keyString = get_key()
    while True:
        try:
            user_input = input("question: \n")
            if user_input.strip() == '':  # Filter empty input
                continue
            if user_input.lower() in ['exit', 'quit']:
                print("\nConversation ended, goodbye!")
                break
            
            # Maintain existing call logic...
            response = chat_with_deepseek(user_input, keyString)
            
            # Optimize output format
            print("response".center(80, '-'))
            print(response.strip())
            print("-" * 80)
            
        except Exception as e:
            print(f"\nError: {str(e)}")

# ... keep other code unchanged ...

if __name__ == "__main__":
    main()