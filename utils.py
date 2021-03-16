import json


def convert_request_form_to_dict(request_form):
    chat_history = json.loads(dict(request_form)["msg"])
    return chat_history

def convert_request_form_to_list(request_form):
    chat_dict = json.loads(dict(request_form)["msg"])
    chat_list = list()
    for idx in range(len(chat_dict)):
        chat_list.append(chat_dict[str(idx)])
    return chat_list
