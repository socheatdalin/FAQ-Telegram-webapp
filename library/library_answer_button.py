from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import  ContextTypes, CallbackContext
import bson
from library.library_qa_list import library_qa_list 
from library.database_library import library_database_collection, image_database_collection
from start_command import start_command

image = image_database_collection()
data = library_qa_list(library_database_collection())
library = library_database_collection()

async def button_click_answer_library_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    option_selected = query.data
    media =[]
    # answer = None
    for index, value in enumerate(data['questions']):
        if option_selected == f'library_qa_{index}':
            answer = data['answers'][index]
            document = library.find_one({'question': value, 'answer': answer})
            if document:
                object_id = document['_id']
                librarys_id = str(object_id)
                image_docs = image.find({'library_id': librarys_id})
                # print(document)
                print(librarys_id)
            # print(image_docs)
                for image_doc in image_docs:
                    # file_path = image_doc.get('filepath')
                    file_path = image_doc['filepath']
                    # print(image_doc)
                    print(file_path)
                    if file_path:
                        with open(file_path, 'rb') as photo_file:
                            media.append(InputMediaPhoto(media=photo_file))
                            # Respond to the callback query
            # await start_command(update, context)
            await query.answer(text="Query processed.")
                            # Send the photo with caption to the chat
            keyboard = [
                [InlineKeyboardButton("library", callback_data="library"),
                InlineKeyboardButton("start", callback_data="start")]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await context.bot.send_media_group(chat_id=query.message.chat_id,caption=f"🤔 <b>Question:</b> {value}\n\n🤖 <b>Answer:</b> {answer}",media=media,parse_mode="HTML")
            # await update.message.reply_text(text="Menu", reply_markup= reply_mark )
            # await context.bot.send_message(chat_id=query.message.chat_id,text="Returning to the start...", reply_markup=reply_markup)
            await context.bot.send_photo(chat_id=query.message.chat_id,photo="./library/library_images/welcome.png", caption="👋 Welcome to our Telegram chat bot! We're thrilled to have you on board and ready to explore the exciting possibilities that await. Whether you're here for information, assistance, our bot is here to make your experience enjoyable.\n\n🚀 To get started, check out the following commands our bot:\nSchool: /school\nLibrary: /library\n\n🌈 Thank you for joining us on this adventure! Your curiosity and engagement drive us to continually improve and enhance your experience. If you have any feedback or suggestions, we're all ears—just drop us a message.\n🤖 Happy chatting, and may your interactions with our bot be both informative and entertaining! Let the conversation begin! 🤖✨")
