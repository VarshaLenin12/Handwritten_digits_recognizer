# Handwritten Digits Recognizer


## Overview
The **Handwritten Digits Recognizer** is a machine learning application designed to identify digits from images of handwritten numbers. Utilizing a convolutional neural network (CNN) built with TensorFlow and Keras, this project demonstrates an efficient and effective approach to image classification.

## Features
- **Image Upload & Recognition:** Upload an image containing a handwritten digit, and the model predicts the digit with high accuracy of 0.9488.
- **In-Memory Processing:** Images are processed in-memory for faster predictions without the need to save files on disk.
- **User-Friendly Interface:** A clean and intuitive web interface powered by Flask, allowing easy interaction with the model.
- **Responsive Design:** The web application is mobile-friendly and adapts seamlessly to different screen sizes.

## Technologies Used
- **Frontend:**
  - HTML5 & CSS3
  - Bootstrap for responsive design
- **Backend:**
  - Flask (Python)
  - TensorFlow & Keras for the machine learning model
  - OpenCV & Pillow for image processing
- **Version Control:**
  - Git & GitHub

## Installation

### Prerequisites
- Python 3.6+
- `pip` package manager

### Setup Instructions

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/VarshaLenin12/VarshaLenin12-Handwritten_digits_recognizer.git
    cd Handwritten_digits_recognizer
    ```

2. **Create a Virtual Environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Download the Model:** 
   Ensure the trained model (`digit_recognition_model2.h5`) is in the root directory.

5. **Run the Application:**

    ```bash
    python app.py
    ```

6. **Access the Application:** 
   Open your web browser and go to `http://127.0.0.1:5000/`.

---

## Usage

1. **Upload an Image:** Navigate to the home page and upload an image of a handwritten digit (supported formats: PNG, JPG, JPEG, GIF).
2. **View Prediction:** The application processes the image and displays the predicted digit along with the uploaded image.

---

## Project Structure

```plaintext
.
├── app.py                        # Main Flask application
├── digit_recognition_model2.h5   # Pre-trained model
├── static/
│   ├── ind_styles.css            # Custom CSS styles
├── templates/
│   ├── index.html                # Home page
│   └── result.html               # Result page
├── uploads/                      # (Optional) Directory for uploaded files
├── README.md                     # Project documentation
└── requirements.txt              # Python dependencies

## Model Details

- **Architecture:** Convolutional Neural Network (CNN)
- **Layers:** 2D Convolutional layers, MaxPooling, Flatten, Dense layers with ReLU and softmax activation.
- **Optimizer:** Adam
- **Loss Function:** Categorical Crossentropy

---

## Demo

[Handwritten Digits Recognizer Demo](https://youtu.be/demo_video_link)

---

## Contributing

Contributions are welcome! If you'd like to improve or expand this project, feel free to fork the repository and submit a pull request. Please ensure your contributions align with the project's goals and style.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- [TensorFlow](https://www.tensorflow.org/) - Machine learning framework
- [Flask](https://flask.palletsprojects.com/) - Lightweight WSGI web application framework
- [OpenCV](https://opencv.org/) - Open Source Computer Vision Library

---

## Contact

For any inquiries or support, please reach out to me via [LinkedIn](www.linkedin.com/in/varsha-l-ml).

