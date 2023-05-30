from flask import Flask, request, render_template
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os
import json

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        print("Accepting Input")
        return render_template('home.html', results="Submit")
    else:
        print("Started with Post")
        model_path = os.path.join("artifacts", "model.h5")
        model = tf.keras.models.load_model(model_path)
        upload_file = request.files['image']
        temp_filename = 'temp.png'
        upload_file.save(temp_filename)
        img = os.path.join(os.getcwd(), temp_filename)
        img = image.img_to_array(tf.image.resize(image.load_img(img), [224, 224])) / 255
        img = np.expand_dims(img, axis=0)

        results = model.predict(img)
        print("after Prediction")
        results_json = json.dumps("Predicted Age = "+str(results[0][0].tolist()))  # Convert the results to JSON format

        os.remove(temp_filename)  # Remove the temporary file

        return results_json


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
