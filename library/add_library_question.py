from flask import request, jsonify, Flask


def add_library_question(collection):
    if request.method == 'POST':
        data = request.form
        question: str = data['question']
        answer: str = data['answer']
        type: str = data['type']
        if question and answer:
            result = collection.insert_one({'question': question, 'answer': answer, 'type': type})
            return  str(result.inserted_id)
        # jsonify({'message': 'Question added successfully'}), 201
        else:
            return jsonify({'error': 'Invalid request data'}), 400    
      
        
    