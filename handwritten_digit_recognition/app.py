from flask import Flask, request, render_template, redirect
import tensorflow as tf
import numpy as np
import cv2
import io
import base64
from PIL import Image

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('digit_recognition_model2.h5')

# Define the allowed extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Read the image in memory
        img = Image.open(io.BytesIO(file.read()))
        img = img.convert('L')  # Convert to grayscale

        # Convert the image to a NumPy array
        img_array = np.array(img)
        
        # Resize and preprocess the image
        img_resized = cv2.resize(img_array, (28, 28))
        img_resized = img_resized.astype('float32') / 255.0
        img_resized = np.expand_dims(img_resized, axis=(0, -1))
        
        # Predict
        prediction = model.predict(img_resized)
        digit = np.argmax(prediction)

        # Convert the image back to base64
        buffered = io.BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
        img_data = f"data:image/png;base64,{img_str}"

        return render_template('result.html', digit=digit, img_data=img_data)

    return render_template('result.html', error="Invalid file type. Please upload a PNG, JPG, JPEG, or GIF image.")

if __name__ == '__main__':
    app.run(debug=True)
