from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler, CallbackContext
from pymongo import MongoClient
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import json_util
import ast
from flask_cors import CORS
from bson import ObjectId
from werkzeug.utils import secure_filename

# Import files to app
#school
from start_command import start_command
from school.add_school_question import add_school_question
# from school.school_qa_list import school_qa_list
from school.list_all_school_question import list_all_school_questions
from school.button_click_answer import button_click_answer
from handle_message import handle_message
# from school.school_information import send_image
# from school.list_all_building_questions import list_all_building_questions
# from school.list_all_department_questions import list_all_department_questions

#library
from library.library_qa_list import library_qa_list 
from library.add_library_question import add_library_question
from library.list_all_library_question import list_all_library_questions
from library.library_answer_button import button_click_answer_library_handler
from library.book_answer_button import button_click_answer_book
from library.list_all_book_question import list_all_book_questions
from library.list_all_room_question import list_all_room_questions
from library.room_answer_button import button_click_answer_room_handler

# call dotenv file before access values
load_dotenv()

# start command
start_command

DATABASE = os.getenv('DATABASE_CONNECTION')
TOKEN = os.getenv('TOKEN')
BOT_USERNAME = os.getenv('BOT_USERNAME')

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER='school\school_images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

IMAGE_FOLDER='library\library_images'
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

client = MongoClient(DATABASE, tlsAllowInvalidCertificates=True)

db = client['FAQ_Webapp']
# Collections
school_collection = db['school']
library_collection = db['library']
image_collection = db['images']

def get_school_collection(): return school_collection
def get_library_collection(): return library_collection

# Add school question router
@app.route("/add_school_question", methods=['POST'])
def add_school_questions_list():
    school_id = add_school_question(school_collection) 
    if 'files' not in request.files:
        return jsonify({'error':'No file part'})
    files = request.files.getlist('files')
    for file in files:  
        if files:          
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            image_collection.insert_one({'filename':filename, 'filepath': filepath, 'school_id': school_id})
        else:
            return jsonify({'error': 'Invalid request data'}), 400     
    return jsonify({'message': 'Images added successfully'}), 201   
    
# Add library question router
@app.route("/add_library_question", methods=['POST'])
def add_library_question_list():
    library_id = add_library_question(library_collection) 
    if 'files' not in request.files:
        return jsonify({'error':'No file part'})
    files = request.files.getlist('files')
    for file in files:  
        if files:          
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['IMAGE_FOLDER'], filename)
            file.save(filepath)
            image_collection.insert_one({'filename':filename, 'filepath': filepath, 'library_id':library_id})
        
            # return jsonify({'message': 'image added successfully'}), 201
        else:
            return jsonify({'error': 'Invalid request data'}), 400     
    return jsonify({'message': 'Images added successfully'}), 201   
        
# school_QAs = school_qa_list(school_collection)
library_QAs = library_qa_list(library_collection)

# school_data = school_QAs['questions']
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {context} caused error {context.error}')
    
@app.route("/all_questions", methods=['GET'])
def all_questions():
    if request.method == "GET":
        school_data = list(school_collection.find())
        school_json_data = json_util.dumps(school_data)
        school_data_result = ast.literal_eval(school_json_data)
        
        library_data = list(library_collection.find())
        library_json_data = json_util.dumps(library_data)
        library_data_result = ast.literal_eval(library_json_data)
        return {'schoolData': school_data_result, 'libraryData': library_data_result}

@app.route("/all_questions/delete/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    try:
        item_id_obj = ObjectId(item_id)
        result = school_collection.delete_one({'_id': item_id_obj})
        
        if result.deleted_count == 1:
            response = {'message': 'Item deleted successfully'}
        else:
            result = library_collection.delete_one({'_id': item_id_obj})
            if result.deleted_count == 1:
                response = {'message': 'Item deleted successfully'}
            else: response = {'message': 'Item not found'}
    except Exception as e:
        response = {'message': str(e)}

    return jsonify(response)

async def callBack_handler(update: Update, context: CallbackContext):
    # Extracting the callback query from the update
    query = update.callback_query
    if query.data == 'start':
        await query.message.answer(start_command)
    
    

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=5000)
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('school', list_all_school_questions))
    
#     app.add_handler(CommandHandler('building', list_all_building_questions))
#     app.add_handler(CommandHandler('department', list_all_department_questions))

    # app.add_handler(CommandHandler('book', list_all_book_detail))
    app.add_handler(CommandHandler('library', list_all_library_questions))
    app.add_handler(CommandHandler('room', list_all_room_questions))
    app.add_handler(CommandHandler('book', list_all_book_questions))
    app.add_handler(CallbackQueryHandler(button_click_answer_library_handler, pattern=r'^library_qa_'))
    app.add_handler(CallbackQueryHandler(button_click_answer_room_handler, pattern=r'^room_qa_'))
    app.add_handler(CallbackQueryHandler(button_click_answer_book, pattern=r'^book_qa_'))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_handler(CallbackQueryHandler(button_click_answer))
    # app.add_handler(CallbackQueryHandler(callBack_handler))

    app.add_error_handler(error)    
    app.run_polling(poll_interval=3)
    
    