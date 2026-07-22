# 🧠 Brain Tumor Classification from MRI Images using Deep CNN

## 📌 Overview

Brain Tumor Classification from MRI Images is a Deep Learning project that uses a Convolutional Neural Network (CNN) to classify brain MRI scans into **five different categories**. The application provides a simple graphical user interface (GUI) where users can upload an MRI image, receive an instant prediction, and hear the prediction through **Text-to-Speech (TTS)**.

This project demonstrates the use of Artificial Intelligence and Computer Vision for automated medical image classification.

> **Note:** This project is developed for educational and research purposes only. It is not intended for clinical or medical diagnosis.

---

## ✨ Features

- 🧠 Classifies MRI images into **5 brain tumor categories**
- 📷 Upload MRI images through a simple GUI
- 🤖 Deep CNN-based image classification
- 📊 Displays predicted class with confidence score
- 🔊 Announces the prediction using Text-to-Speech
- ⚡ Fast and accurate prediction
- 💻 Easy-to-use interface

---

## 🧠 Tumor Categories

The model classifies MRI images into the following categories:

- Glioma
- Meningioma
- Pituitary Tumor
- acoustic neuroma
- craniopharyngioma*(Replace with your actual class name if different.)*

---

## 🛠️ Technologies Used

- Python
- TensorFlow
- Keras
- OpenCV
- NumPy
- Pillow (PIL)
- Tkinter
- pyttsx3 (Text-to-Speech)
- Matplotlib

---

## 📂 Project Structure

```
Brain-Tumor-Classification/
│
├── dataset/
├── model/
│   └── brain_tumor_model.h5
├── images/
├── train.py
├── predict.py
├── gui.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🔄 Project Workflow

```
MRI Image
     │
     ▼
Image Preprocessing
     │
     ▼
Deep CNN Model
     │
     ▼
Prediction
     │
     ├── Display Result
     ├── Confidence Score
     └── Voice Output (Text-to-Speech)
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Brain-Tumor-Classification.git
cd Brain-Tumor-Classification
```

### 2. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python finalgui.py
```

---

## 📸 How It Works

1. Open the application.
2. Upload a brain MRI image.
3. The image is preprocessed automatically.
4. The Deep CNN predicts the tumor category.
5. The predicted class and confidence score are displayed.
6. The result is announced using Text-to-Speech.

---

## 🔊 Voice Assistant Feature

After prediction, the application automatically speaks the result.

**Example:**

```
Prediction Complete.
The MRI image is classified as Glioma.
```

---

## 🎯 Applications

- Medical Image Classification
- Deep Learning Projects
- Computer Vision Applications
- AI Research
- Educational Demonstrations
- Healthcare Technology Learning

---

## 🚀 Future Enhancements

- Improve classification accuracy using larger datasets
- Support DICOM medical images
- Add Grad-CAM visualization
- Deploy as a Flask or Streamlit web application
- Real-time hospital integration
- Cloud deployment

---

## 💡 Skills Demonstrated

- Deep Learning
- Convolutional Neural Networks (CNN)
- Computer Vision
- Medical Image Processing
- Image Classification
- Python Programming
- TensorFlow & Keras
- OpenCV
- GUI Development
- Text-to-Speech Integration

---

## 📦 Requirements

```
Python 3.9+

TensorFlow
Keras
OpenCV
NumPy
Pillow
Matplotlib
Tkinter
pyttsx3
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

## 📈 Model Pipeline

```
MRI Image
      │
      ▼
Resize Image
      │
      ▼
Normalize Pixels
      │
      ▼
Deep CNN
      │
      ▼
Softmax Classification
      │
      ▼
Predicted Tumor Class
      │
      ├── Display on GUI
      └── Speak using Text-to-Speech
```

---

## 🤝 Contributing

Contributions are welcome!

If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Swathi N M **

Bachelor Of Computer Appkication (BCA)

Python • Deep Learning • Computer Vision • OpenCV • TensorFlow • CNN

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub!
