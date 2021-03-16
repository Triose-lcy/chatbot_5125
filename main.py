from flask import Flask, render_template, request, send_from_directory, jsonify
from pprint import pprint
import utils

app = Flask(__name__, template_folder='templates')
app.static_folder = 'templates/'


@app.route("/")
def home():
    # conversation = [
    #     {"who": "bot", "content": "What can I do for you?"},
    #     # {"who": "user", "content": "Where should I go?"}
    # ]
    # return render_template("index.html", conversation=conversation)
    return render_template("index.html")


@app.route("/get_response", methods=["POST"])
def get_bot_response():
    chat_history = utils.convert_request_form_to_list(request.form)
    pprint(chat_history)

    bot_response = "copy that"

    return jsonify(bot_response)


@app.route('/images/<filename>')
def send_images_needs_by_javascript(filename):
    return send_from_directory('templates/images', filename)


if __name__ == "__main__":
    app.run()


