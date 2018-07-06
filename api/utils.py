from flask import jsonify

def respond_to_json(success=True, message="Operation was successful",
                    data=None, metadata={}, status=200):
    metadata["status_code"] = status
    return jsonify({
        "success": success,
        "message": message,
        "data": data,
        "metadata": metadata
    }), status
