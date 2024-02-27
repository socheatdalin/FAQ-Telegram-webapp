from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from library.library_qa_list import library_qa_list
from library.database_library import library_database_collection
data = library_qa_list(library_database_collection())
async def list_all_book_questions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for index, value in enumerate(data['questions']):
            keyboard.append([InlineKeyboardButton(text = value, callback_data=f"book_qa_{index}")])
    bookIndexes = []
    for index, value in enumerate(data['types']):
            if value == "book":
                bookIndexes.append(index)
    render_questions = InlineKeyboardMarkup([keyboard[i] for i in bookIndexes])
    await update.message.reply_photo(photo="./library/library_images/meetingRoom.jpg", caption="🚀 Welcome to Institute of Technology of Cambodia Library's book!\n\n☺ Please select the question for more details:", reply_markup=render_questions)
    # await update.message.reply_text("List of Questions:", reply_markup=render_questions)
    