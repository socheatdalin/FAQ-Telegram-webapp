from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CallbackContext
from library.library_qa_list import library_qa_list
from library.database_library import library_database_collection

data = library_qa_list(library_database_collection())

async def list_all_library_questions(update: Update, context: CallbackContext):
    keyboard = []
    for index, value in enumerate(data['questions']):
        keyboard.append([InlineKeyboardButton(text = value, callback_data=f"library_qa_{index}")])
    libraryIndexes = []
    for index, value in enumerate(data['types']):
        if value == "library":
            libraryIndexes.append(index)
            
    render_questions = InlineKeyboardMarkup([keyboard[i] for i in libraryIndexes])
    await update.message.reply_photo(photo="./library/library_images/library.jpg", caption="Welcome to Institute of Technology of Cambodia!\n\n🚀 To know more about our library, please follow this commands below:\nBook: /book\nRoom: /room\n\n☺ Please select the question for more details:", reply_markup=render_questions)

# def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

#     subK = [
#             InlineKeyboardButton("Start", callback_data='0'),
#             InlineKeyboardButton("Library", callback_data='1')
#         ]

#     reply_markup = InlineKeyboardMarkup(subK)

#     query = update.callback_query


#     query.edit_message_text(chat_id=query.message.chat_id,
#                           message_id=query.message.message_id,
#                           reply_markup=reply_markup)
