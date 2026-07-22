import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import ImageTk, Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import pyttsx3
import numpy as np

np.set_printoptions(suppress=True)

# Main Window
top = tk.Tk()
top.geometry('900x650')
top.title('Brain Tumor Detection')
top.configure(bg="#E3F2FD")   # Light blue background


# Heading
heading = tk.Label(
    top,
    text="🧠 Brain Tumor Detection System",
    font=("Helvetica", 28, "bold"),
    bg="#0D47A1",
    fg="white",
    pady=15
)
heading.pack(fill="x")


# Frame for image
frame = tk.Frame(top, bg="#E3F2FD")
frame.pack(pady=20)


sign_image = tk.Label(frame, bg="#E3F2FD")
sign_image.pack()


# Prediction label
label = tk.Label(
    top,
    bg="#E3F2FD",
    fg="#0D47A1",
    font=("Arial", 18, "bold")
)
label.pack(pady=10)


# Speech
def botsay(message):
    engine = pyttsx3.init()
    engine.say("The prediction is " + message)
    engine.runAndWait()


# Classification
def classify(file_path):

    model = tf.keras.models.load_model('keras_Model.h5')

    with open('labels.txt', 'r') as f:
        label_names = f.read().splitlines()

    img = image.load_img(file_path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    predictions = model.predict(x)
    class_index = np.argmax(predictions[0])
    class_name_predicted = label_names[class_index]

    label.configure(text="Prediction: " + class_name_predicted)

    messagebox.showinfo("Result", "Prediction: " + class_name_predicted)

    botsay(class_name_predicted)


# Classify Button
def show_classify_button(file_path):
    classify_b = tk.Button(
        top,
        text="🔍 Classify Image",
        command=lambda: classify(file_path),
        font=("Arial", 14, "bold"),
        bg="#43A047",
        fg="white",
        padx=20,
        pady=10,
        relief="raised",
        bd=4
    )
    classify_b.pack(pady=15)


# Upload image
def upload_image():
    try:
        file_path = filedialog.askopenfilename()

        uploaded = Image.open(file_path)
        uploaded.thumbnail((350, 350))

        im = ImageTk.PhotoImage(uploaded)

        sign_image.configure(image=im)
        sign_image.image = im

        label.configure(text='')

        show_classify_button(file_path)

    except:
        pass


# Upload Button
upload = tk.Button(
    top,
    text="📂 Upload MRI Image",
    command=upload_image,
    font=("Arial", 14, "bold"),
    bg="#FB8C00",
    fg="white",
    padx=25,
    pady=12,
    relief="raised",
    bd=4
)

upload.pack(pady=20)


top.mainloop()