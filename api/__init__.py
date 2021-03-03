from flask import Flask, jsonify, request
from .predictions.predict import get_prediction


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    @app.route('/')
    def hello():
        return 'Webservice is up!'

    @app.route('/predict', methods=['POST'])
    def predict():
        if request.method == 'POST':
            file = request.files['filedata']
            img_bytes = file.read()
            class_id, class_name = get_prediction(image_bytes=img_bytes)
            return jsonify({'class_id': class_id, 'class_name': class_name})

    return app
