from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from school.school_qa_list import school_qa_list
from school.database_school import school_database_collection
data = school_qa_list(school_database_collection())
async def list_all_school_questions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = []
    for index, value in enumerate(data['questions']):
        keyboard.append([InlineKeyboardButton(text = value, callback_data=f"very_long_{index}")])
    schoolIndexes = []
    for index, value in enumerate(data['types']):
        if value == "school":
            schoolIndexes.append(index)

    render_questions = InlineKeyboardMarkup([keyboard[i] for i in schoolIndexes])
    await update.message.reply_photo(photo="./school/school_images/school.jpeg", caption="Welcome to Institute of Technology of Cambodia!\n\n🚀 To know more about our school, please follow this commands below:\nDepartement: /department\nBuilding: /building\n\n☺ Please select the question for more details:", reply_markup=render_questions)