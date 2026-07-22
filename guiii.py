
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog, messagebox
from tkinter import *
from PIL import ImageTk, Image
import cv2
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import pyttsx3
from tkinter import messagebox
# init function to get an engine instance for the speech synthesis
import pandas as pd
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np


np.set_printoptions(suppress=True)
top = tk.Tk()
top.geometry('800x600')
top.title('brain tumor Detection ')

df=pd.read_csv('data.csv')
def display_info(item):
    if item in df['name'].values:
        row = df[df['name']==item].iloc[0]
        infomessage=f"fruit Name:{row['name']}\n"+f"Fruit info:{row['info']}"

        messagebox.showinfo("Recommandation",infomessage)
        botsay(infomessage)





def botsay(message):
    engine = pyttsx3.init()

    engine.say("the prediction is  "+ message)
    engine.runAndWait()
def classify(file_path):

    model = tf.keras.models.load_model('keras_Model.h5')

    # Load the label namess
    with open('labels.txt', 'r') as f:
        label_names = f.read().splitlines()

    # Load and preprocess the image
    img_path = file_path
    img = image.load_img(img_path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = x / 255.0

    # Predict the class of the image
    predictions = model.predict(x)
    class_index = np.argmax(predictions[0])
    class_name_predicted = label_names[class_index]

    # Print the predicted class
    print('Predicted class:', class_name_predicted)
    label.configure(foreground='#011638', text=class_name_predicted)
    label.place(relx=0.70, rely=0.20)
    elabel = class_name_predicted
    messagebox.showinfo("info","the prediction is :"+ elabel)
    display_info(elabel)



def show_classify_button(file_path):
    classify_b = Button(top, text="Classify Image",command=lambda: classify(file_path), padx=10, pady=5)
    classify_b.configure(background='#364156', foreground='white', font=('arial', 10, 'bold'))
    classify_b.place(relx=0.79, rely=0.46)

def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25),(top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text='')
        show_classify_button(file_path)
    except:
        pass

label = Label(top)
label = Label(top, background='white', font=('arial', 15, 'bold'))
sign_image = Label(top)

upload = Button(top, text="Upload an image",  padx=10, pady=5)
#webcam = Button(top, text="Butterfly classification", command=liveEmotion, padx=21, pady=5)
upload.configure(background='#364156', foreground='white', command=upload_image, font=('arial', 10, 'bold'))
#webcam.pack(side=BOTTOM,pady=70)
upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(top, text="brain tumor Detection ", pady=20, font=('arial', 20, 'bold'))

heading.configure(background='black', foreground='white')
heading.pack()

top.mainloop()
