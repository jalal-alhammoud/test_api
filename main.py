from flask import Flask, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# إعداد معلومات وصفية للAPI (بدون دعم tags كما في FastAPI)
API_TITLE = "Recommendation System API"
API_DESCRIPTION = "A comprehensive API for product recommendations using various algorithms"
API_VERSION = "1.0.0"

@app.route("/health", methods=["GET"])
def health_check():
    """
    Health check endpoint
    """
    return jsonify({
        "status": "healthy",
        "version": API_VERSION,
        "api_title": API_TITLE,
        "description": API_DESCRIPTION
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
