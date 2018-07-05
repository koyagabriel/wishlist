from flask import jsonify

def index():
    return jsonify({
        "success": True,
        "message": "Welcome to Flask Homepage"
    })
