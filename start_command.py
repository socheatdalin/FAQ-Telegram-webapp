from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext


async def start_command(update: Update, context: CallbackContext,):
    keyboard = [
        [InlineKeyboardButton(text="Start", callback_data="0")],
        InlineKeyboardButton(text="Library", callback_data="1")]
    
    await update.message.reply_photo(photo="./library/library_images/welcome.png", caption="👋 Welcome to our Telegram chat bot! We're thrilled to have you on board and ready to explore the exciting possibilities that await. Whether you're here for information, assistance, our bot is here to make your experience enjoyable.\n\n🚀 To get started, check out the following commands our bot:\nSchool: /school\nLibrary: /library\n\n🌈 Thank you for joining us on this adventure! Your curiosity and engagement drive us to continually improve and enhance your experience. If you have any feedback or suggestions, we're all ears—just drop us a message.\n🤖 Happy chatting, and may your interactions with our bot be both informative and entertaining! Let the conversation begin! 🤖✨")

# def button(bot, update):

#     subK = [
#             InlineKeyboardButton("Start", callback_data='0'),
#             InlineKeyboardButton("Library", callback_data='1')
#         ]

#     reply_markup = InlineKeyboardMarkup(subK)

#     query = update.callback_query

#     # bot.edit_message_text(chat_id=query.message.chat_id,
#     #                       message_id=query.message.message_id,
#     #                       reply_markup=ReplyKeyboardRemove())


#     query.edit_message_text(chat_id=query.message.chat_id,
#                           message_id=query.message.message_id,
#                           reply_markup=reply_markup)
