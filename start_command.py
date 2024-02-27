from telegram import Update
from telegram.ext import CallbackContext

async def start_command(update: Update, context: CallbackContext):
    await update.message.reply_photo(photo="./library/library_images/welcome.png", caption="👋 Welcome to our Telegram chat bot! We're thrilled to have you on board and ready to explore the exciting possibilities that await. Whether you're here for information, assistance, our bot is here to make your experience enjoyable.\n\n🚀 To get started, check out the following commands our bot:\nSchool: /school\nLibrary: /library\n\n🌈 Thank you for joining us on this adventure! Your curiosity and engagement drive us to continually improve and enhance your experience. If you have any feedback or suggestions, we're all ears—just drop us a message.\n🤖 Happy chatting, and may your interactions with our bot be both informative and entertaining! Let the conversation begin! 🤖✨")
