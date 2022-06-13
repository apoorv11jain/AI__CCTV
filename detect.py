#this project is made by Apoorv Jain for the IBM Summer Training
#this project is used to detect the weapons such as gun to user
# hence it is a AI CCTV camera

#Step 1:- importing all the modules we required
import cv2  # the open cv module is used in the recognition of the weapons
import pyttsx3  #this module is used for the voice in the code hence making it more user friendly 
from tkinter import *    # these 2 modules are used to make the 
from tkinter import ttk    #programm visually more user friendly

# Step 2: - the defining of the constant values 
engine=pyttsx3.init('sapi5')
rate=engine.getProperty("rate")
engine.setProperty("rate",150)
volume=engine.getProperty("volume")
engine.setProperty("volume",1)
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)
b =cv2.CascadeClassifier('cascade.xml')
# the above cascade classifier is specially made by me using the Cascade Trainer GUI application
#this classifier is way better than that avialable online

repeat =0

#Step 3: - i have defind a function detector which will open the the web cam and check whether
#  any weapon is present in the screen or not it will be giving an voice output saying alert if
#  any weapon found in the camera
#  press esc key for exiting the window 
def detector():
    a=cv2.VideoCapture(-1)
    while True:
        check, frame = a.read()
        if check == True:
            g = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            f = b.detectMultiScale( g, 1.05, 5)
            for x,y,w,h in f:
                i= cv2.rectangle(frame, (x,y),(x+w,x+h),(0,0,255),5)
                cv2.putText(frame, "Weapon", (x-50, y-50), cv2.FONT_HERSHEY_DUPLEX, 2,(0, 255, 0), 3)
                engine.say("Alert!")
                engine.runAndWait()
            cv2.imshow("CCTV", frame)
            u= cv2.waitKey(30) & 0xff
            if u ==27:
                break
        else:
            print("error in CCTV PLEASE TRY RESTARTING")
        
    cv2.destroyAllWindows()
    a.release()

#Step 4: - these are the main files defining to open a tkinter window with a button in it
# if the button is pressed the detector function is called    
root = Tk()
btn =ttk.Button(root,text=" PRESS THIS TO START CCTV")
btn.pack()
label =ttk. Label(root, text =" PREE THE ESC KEY IN YOUR DEVICES TO EXIT FROM THE CCTV WINDOW ").pack()
btn.config(command = detector)
