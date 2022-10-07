# -*- coding: utf-8 -*-

# import the libraries

from tkinter import *
from tkinter import ttk, font, filedialog, Entry
from tkinter.messagebox import askokcancel, showinfo, WARNING
import getpass
from PIL import Image
from PIL import ImageTk
import base64
from turtle import clear
import grpc
import numpy as np


#Services os backend

import backend_pb2
import backend_pb2_grpc

#Services os inference

import inference_pb2
import inference_pb2_grpc

# initialize Object
root = Tk()

panelA = None
strPath = None



def run_model():
    global strPath
    
    path_msg = inference_pb2.img_path2(path=strPath)
    response = inference_client.predict(path_msg)

    v_percent = response.percent
    v_result = response.dataresult

    text2.insert(END, v_result)
    text3.insert(END, '{:.2f}'.format(v_percent)+'%') 



    

def select_image():
    # grab a reference to the image panels
    global panelA, backend_client, strPath
    # open a file chooser dialog and allow the user to select an input
    # image
    path =  filedialog.askopenfilename(title="Select image",
            filetypes=(
                ("JPEG", "*.jpeg"),
                ("DICOM", "*.dcm"),
                ("jpg files", "*.jpg"),
                ("png files", "*.png"),
            ))

    # ensure a file path was selected
    if len(path) > 0:

        strPath = path
        
        path_message = backend_pb2.img_path(path=path)
        response = backend_client.load_image(path_message)

        img_content = response.img_content
        img_w = response.width
        img_h = response.height

        b64decoded = base64.b64decode(img_content)
        imagen = np.frombuffer(b64decoded, dtype=np.uint8).reshape(img_h, img_w, -1)

        # convert the images to PIL format...
        image = Image.fromarray(imagen)
            
        newsize = (250, 250)
        
        image = image.resize(newsize)
        image = ImageTk.PhotoImage(image)

        # if the panels are None, initialize them
        
        if panelA is None:
        
            panelA = Label(image=image)
            panelA.image = image
            panelA.place(x=90, y=90)

        else:
            panelA.configure(image=image)
            panelA.image = image

        button1['state'] = 'enabled'
        

# initialize the window toolkit 

root.title("Detector de Neumonia")
root.geometry("490x560")        
root.resizable(0,0)

fonti = font.Font(weight='bold')

#   LABELS
lab1 = ttk.Label(root, text="Imagen Radiografica", font=fonti)
lab3 = ttk.Label(root, text="Resultado:", font=fonti)
lab6 = ttk.Label(root, text="Probabilidad:", font=fonti)

# Variable Resultado
result = StringVar()

#   INPUT BOXES
text2 = Text(root)
text3 = Text(root)

#   BUTTONS
button1 = ttk.Button(root, text="Predecir", state='disabled', command= run_model) 
button2 = ttk.Button(root, text="Cargar Imagen", command= select_image)


#   WIDGETS POSITIONS   
lab1.place(x=110, y=65)
lab3.place(x=80, y=370)
lab6.place(x=80, y=415)
button1.place(x=220, y=460)
button2.place(x=70, y=460)
text2.place(x=220, y=370, width=90, height=30)
text3.place(x=220, y=415, width=90, height=30)





# Backend client definition
MAX_MESSAGE_LENGTH = 256*1024*1024

options = [('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)]
channel = grpc.insecure_channel("backend:50051", options = options)
backend_client = backend_pb2_grpc.BackendStub(channel=channel)

# Inference client definition
channel2 = grpc.insecure_channel("inference:50052")
inference_client = inference_pb2_grpc.inferenceStub(channel=channel2)


# create a button, then when pressed, will trigger a file chooser
# dialog and allow the user to select an input image; then add the
# button the GUI
#btn = Button(root, text="Select an image", command=select_image)
#btn.pack(side="bottom", fill="both", expand="yes", padx="10", pady="10")
# kick off the GUI
root.mainloop()
