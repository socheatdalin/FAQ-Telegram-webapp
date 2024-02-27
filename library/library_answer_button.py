from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import  ContextTypes, CallbackContext
import bson
from library.library_qa_list import library_qa_list
from library.database_library import library_database_collection, image_database_collection

image = image_database_collection()
data = library_qa_list(library_database_collection())
library = library_database_collection()
async def button_click_answer_library_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    option_selected = query.data
    for index, value in enumerate(data['questions']):
        if option_selected == f'library_qa_{index}':
            answer = data['answers'][index]
            # new_data = {}
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
                            caption = f"🤔 <b>Question:</b> {value}\n\n🤖 <b>Answer:</b> {answer}"
                            # Respond to the callback query
                            await query.answer()
                            # Send the photo with caption to the chat
                            await context.bot.send_photo(chat_id=query.message.chat_id, photo=photo_file, caption=caption, parse_mode="HTML")
