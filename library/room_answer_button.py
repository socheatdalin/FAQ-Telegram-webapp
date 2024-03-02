from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, InlineQueryResultPhoto
from telegram.ext import  ContextTypes
from library.library_qa_list import library_qa_list
from library.database_library import library_database_collection, image_database_collection

image = image_database_collection()
data = library_qa_list(library_database_collection())
library = library_database_collection()

async def button_click_answer_room_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    option_selected = query.data
    media =[]
    for index, value in enumerate(data['questions']):
        if option_selected == f'room_qa_{index}':
            answer = data['answers'][index]
            document = library.find_one({'question': value, 'answer': answer})
            if document:
                object_id = document['_id']
                librarys_id = str(object_id)
                image_docs = image.find({'library_id': librarys_id})
                
                for image_doc in image_docs:
                    file_path = image_doc.get('filepath')
                    print(file_path)
                    if file_path:
                        with open(file_path, 'rb') as photo_file:
                            media.append(InputMediaPhoto(media=photo_file))
                # photos = [InlineQueryResultPhoto(id=str(index), photo_url=media[index].media, thumb_url=media[index].media) for index in range(len(media))]
            await query.answer(text="Query processed.")
            keyboard = [
                    [InlineKeyboardButton("start", callback_data=f"start"),
                    InlineKeyboardButton("library", callback_data="library_qa")]
                    ]

            reply_markup = InlineKeyboardMarkup(keyboard)
            await context.bot.send_media_group(chat_id=query.message.chat_id, caption=f"🤔 <b>Question:</b> {value}\n\n🤖 <b>Answer:</b> {answer}", media=media, parse_mode="HTML")            
            await context.bot.send_message(chat_id=query.message.chat_id,text="Returning to the start...", reply_markup=reply_markup)