from flask import Flask, jsonify, request
from flask_cors import CORS
from game import Room, Game
from data.rooms import rooms

app = Flask(__name__)
CORS(app)

game = Game(rooms)

@app.route("/command", methods=["POST"])
def command():
    data = request.get_json()
    text = data["text"].lower().strip()
    if text == "look":
        response = game.examine()
    elif text.startswith("go "):
        direction = text.split(" ")[1]
        response = game.move(direction)
    elif text.startswith("take "):
        item = text.split(" ", 1)[1]
        response = game.take_item(item)
    else:
        response = {"type": "error", "message": "I don't understand that command."}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, port=5555)