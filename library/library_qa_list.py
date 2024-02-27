from bson import json_util
import ast

def library_qa_list(collection):
    questions = []
    answers = []
    types = []
    data_from_mongo = list(collection.find())
    json_data = json_util.dumps(data_from_mongo)
    data = ast.literal_eval(json_data)
    for value in data:
        if 'question' in value:
            questions.append(value['question'])
        if 'answer' in value:
            answers.append(value['answer'])
        if 'type' in value:
            types.append(value['type'])
       
    return {'questions': questions, 'answers': answers, 'types': types}
