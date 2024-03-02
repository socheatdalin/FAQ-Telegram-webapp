from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import ContextTypes
import bson
from school.school_qa_list import school_qa_list 
from school.database_school import school_database_collection , image_database_collection
data = school_qa_list(school_database_collection())
school = school_database_collection()
# image = image_school_list(image_database_collection())
image = image_database_collection()
async def button_click_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
        query = update.callback_query
        
        option_selected = query.data
        media =[]
        for index, value in enumerate(data['questions']):
                if option_selected == f'very_long_{index}':
                        answer = data['answers'][index]
                        document = school.find_one()
                        object_id = document['_id']
                        id_school = str(object_id)
                        image_docs = image.find({'school_id': id_school})
                        print("object",image_docs)
                        print("id ",id_school)
                        for image_doc in image_docs:
                                file_path = image_doc.get('filepath')
                                print(file_path)
                                if file_path:
                                        with open(file_path, 'rb') as photo_file:
                                                media.append(InputMediaPhoto(media=photo_file))  
                                                
                                                # Respond to the callback query
        await query.answer(text="Query processed.")
                                                # Send the photo with caption to the chat
        await context.bot.send_media_group(chat_id=query.message.chat_id,caption=f"🤔 <b>Question:</b> {value}\n\n🤖 <b>Answer:</b> {answer}",media=media, parse_mode="HTML")
             
                

                