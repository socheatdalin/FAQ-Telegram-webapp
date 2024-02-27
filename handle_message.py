from telegram import Update
from telegram.ext import ContextTypes
from dotenv import load_dotenv
import os
load_dotenv()
BOT_USERNAME = os.getenv('BOT_USERNAME')
def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hi' in processed:
        return "Hello Dear my love!"
    else: return "We cloud not response for that!"
    
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    print(f'User: {update.message.chat.id} - {message_type}: {text}')
    
    if message_type == "group":
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
        
    else:
        response: str = handle_response(text)
    print(f'Bot: {response}')
    await update.message.reply_text(response)

# from telegram import Update
# from telegram.ext import ContextTypes
# from dotenv import load_dotenv
# import os
# from openai import OpenAI

# client = OpenAI(api_key = os.getenv("CHATGPT_API_KEY"))
# load_dotenv()
# BOT_USERNAME = os.getenv('BOT_USERNAME')

# token = os.getenv('TOKEN')

# def handle_response(question: str) -> str:
#     model_engine = "gpt-3.5-turbo-instruct"
#     prompt = (f"Q: {question}\n"
#     "A:")
#     response = client.completions.create(
#         prompt = prompt,
#         max_tokens = 2024,
#         n = 1,
#         stop = None,
#         model = model_engine
#     )

#     answer = response.choices[0].text.strip()
#     return answer
    
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     question: str = update.message.text
#     print(f'User: {update.message.chat.id}: {question}')
    
#     response: str = handle_response(question)
#     print(f'Bot: {response}')
    
#     await update.message.reply_text(f'🤔 Question\n{question}\n\n🤖 Answer\n{response}')


# from telegram import Update
# from telegram.ext import ContextTypes
# from dotenv import load_dotenv
# import os
# from openai import OpenAI

# client = OpenAI(api_key = os.getenv("CHATGPT_API_KEY"))
# load_dotenv()
# BOT_USERNAME = os.getenv('BOT_USERNAME')

# token = os.getenv('TOKEN')

# def handle_response(question: str) -> str:
#     model_engine = "gpt-3.5-turbo-instruct"
#     prompt = (f"Q: {question}\n"
#     "A:")
#     response = client.completions.create(
#         prompt = prompt,
#         max_tokens = 2024,
#         n = 1,
#         stop = None,
#         model = model_engine
#     )

#     answer = response.choices[0].text.strip()
#     return answer
    
# async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     question: str = update.message.text
#     print(f'User: {update.message.chat.id}: {question}')
    
#     response: str = handle_response(question)
#     print(f'Bot: {response}')
    
#     await update.message.reply_text(f'🤔 Question\n{question}\n\n🤖 Answer\n{response}')