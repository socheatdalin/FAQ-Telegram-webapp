from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import  ContextTypes
from library.library_qa_list import library_qa_list
from library.database_library import library_database_collection, image_database_collection

image = image_database_collection()
data = library_qa_list(library_database_collection())
library = library_database_collection()
# async def button_click_answer_room_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     query = update.callback_query
#     option_selected = query.data
    
#     for index, value in enumerate(data['questions']):
#         if option_selected == f'room_qa_{index}':
#             answer = data['answers'][index]
     
#         if option_selected == f'book_qa_{index}':
#             answer = data['answers'][index]
#             await query.message.reply_photo(photo="./library/images/meetingRoom2.jpg", caption=f"🤔 <b style='color: red;'>Question:</b> {value}\n\n🤖 <b>Answer:</b> {answer}", parse_mode="HTML")       await query.message.reply_photo(photo="./library/images/meetingRoom2.jpg", caption=f"🤔 <b style='color: red;'>Question:</b> {value}\n\n🤖 <b>Answer:</b> {answer}", parse_mode="HTML")
