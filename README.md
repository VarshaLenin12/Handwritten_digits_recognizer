# Handwritten Digits Recognizer

![GitHub repo size](https://img.shields.io/github/repo-size/VarshaLenin12/VarshaLenin12-Handwritten_digits_recognizer)
![GitHub stars](https://img.shields.io/github/stars/VarshaLenin12/VarshaLenin12-Handwritten_digits_recognizer?style=social)
![GitHub forks](https://img.shields.io/github/forks/VarshaLenin12/VarshaLenin12-Handwritten_digits_recognizer?style=social)

Welcome to the Handwritten Digits Recognizer project! This project utilizes machine learning to recognize handwritten digits from images. The goal is to provide accurate digit classification based on images, aiding in various applications such as automated form processing and digit recognition.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview
The Handwritten Digits Recognizer is a machine learning application designed to classify handwritten digits from images. The project features a web interface built with Flask, allowing users to upload images and receive digit predictions.

### Live Demo
Check out the live demo of the project [here](https://handwritten-digits-recognizer.onrender.com/).

## Features
- 🖼️ Upload and classify handwritten digit images.
- 🔍 Real-time predictions with a user-friendly web interface.

## Installation
To get started with the Handwritten Digits Recognizer, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/VarshaLenin12/VarshaLenin12-Handwritten_digits_recognizer.git
    cd VarshaLenin12-Handwritten_digits_recognizer
    ```

2. **Create and activate a virtual environment:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Download the Model:**
   Ensure the trained model (`digit_recognition_model2.h5`) is in the root directory.

5. **Run the application:**
    ```sh
    python app.py
    ```

## Usage
Once the application is running, access the web interface at `http://127.0.0.1:5000`. Upload an image of a handwritten digit and click "Predict" to get the classification result.

## Model Details

- **Architecture:** Convolutional Neural Network (CNN)
- **Layers:** 2D Convolutional layers, MaxPooling, Flatten, Dense layers with ReLU and softmax activation.
- **Optimizer:** Adam
- **Loss Function:** Categorical Crossentropy

### Key Metrics:
- **Accuracy:** High accuracy 0f 0.9488 in digit classification.
- **Performance:** Efficient and fast predictions with minimal latency.

## Technologies Used
- **Python:** Core programming language.
- **Flask:** Web framework for frontend and backend.
- **TensorFlow/Keras:** Machine learning library for model training and predictions.
- **OpenCV:** Image processing library.
- **NumPy:** Numerical computations.
- **Pillow:** Image handling.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a pull request.

##
## Contact
If you have any questions or want to connect, feel free to reach out:

- **Email:** [varshalenin999@gmail.com](mailto:varshalenin999@gmail.com)
- **LinkedIn:** [Varsha L](https://www.linkedin.com/in/varsha-l-ml)

Thank you for visiting the Handwritten Digits Recognizer project! Feel free to explore, use, and contribute to this project.
