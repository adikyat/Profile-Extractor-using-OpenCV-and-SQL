# Import OpenCV2 for image processing
import cv2
import webbrowser
import sqlite3
import time
import datetime


# Import numpy for matrices calculations
import numpy as np

import os 

 
def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)

# Create Local Binary Patterns Histograms for face recognization
recognizer = cv2.face.LBPHFaceRecognizer_create()

assure_path_exists("trainer/")

# Load the trained mode
recognizer.read('trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

# Loop
while True:
    a=0
    c=0
    
    
    


    # Read the video frame
    ret, im =cam.read()

    # Convert the captured frame into grayscale
    gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

    # Get all face from the video frame
    faces = faceCascade.detectMultiScale(gray, 1.2,5)

    # For each face in faces
    for(x,y,w,h) in faces:

        # Create rectangle around the face
        cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

        # Recognize the face belongs to which ID
        Id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        
        h=0

        # Check the ID if exist 
        if(Id == 1 and (100 - confidence)>40):
            Id = "HI chetan"
            
            
            
            a=1
            
        elif(Id == 2 and (100 - confidence)>40):
            Id = "HI Taran"

            
            

            c=1
            
        else:
            Id = "Who r u?"
            h=1
            
            


        # Put text describe who is in the picture
        cv2.putText(im, str(Id), (x,y-50), font,1, (255,0,0),3)

    # Display the video frame with the bounded rectangle
    cv2.imshow('im',im) 

    # If 'q' is pressed, close program
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break




if(a==1):
    webbrowser.open("https://www.facebook.com/profile.php?id=100007736056726", new=0, autoraise=True)
if(c==1):
    webbrowser.open("https://www.facebook.com/raj.lamba.3994", new=1, autoraise=True)    

# Stop the camera
cam.release()

# Close all windows
cv2.destroyAllWindows()





time =  time.asctime( time.localtime(time.time()) )
    
if(a==1):
    con=None
    cursor=None
    try:
                
        con=sqlite3.connect("log.db")
        name = "Chetan Kor"
        print(a)
        sql = "insert into people values('%s','%s')"
        args = (name,time)
        cursor = con.cursor()
        cursor.execute(sql % args)
        con.commit()
        print(cursor.rowcount , "Records inserted")
    except Exception as e:
        print("Add issue",e)
        con.rollback()
    finally:
        if cursor is not None:
                cursor.close()
        if con is not None:
                con.close();
        


if(c==1):
    con=None
    cursor=None
    try:
                
        con=sqlite3.connect("log.db")
                    
                    #time = time.asctime( time.localtime(time.time()) )
        name = "Taran Lamba"
        print(c)
        sql = "insert into people values('%s','%s')"
        args = (name,time)
        cursor = con.cursor()
        cursor.execute(sql % args)
        con.commit()
        print(cursor.rowcount , "Records inserted")
    except Exception as e:
        print("Add issue_taran")
        con.rollback()
    finally:
        if cursor is not None:
                cursor.close()
        if con is not None:
                con.close();
        


if(h==1):
        con=None
        cursor=None
        print(h)
        try:
                
            con=sqlite3.connect("log.db")
            name = "Stranger"
            sql = "insert into people values('%s','%s')"
            args = (name,time)
            cursor = con.cursor()
            cursor.execute(sql % args)
            con.commit()
            print(cursor.rowcount , "Records inserted")
        except Exception as e:
            print("Add issue1",e)
            con.rollback()
        finally:
            if cursor is not None:
                    cursor.close()
            if con is not None:
                    con.close();
   
    
while True:
    opt = int(input("1 View Record,2 Exit"))
    if opt == 1:
        con = None
        cursor = None
        try:
                        con = sqlite3.connect("log.db")
                        sql = "select * from people"
                        cursor = con.cursor()
                        cursor.execute(sql)
                        data = cursor.fetchall()
                        for d in data:
                                print("Name=" , d[0], "Date_Time=",d[1])
        except Exception as e:
                        print("select issue",e)
        finally:
                        if cursor is not None:
                                cursor.close()
                        if con is not None:
                                con.close();
    elif opt == 2:
                break
    else:
                print("Invalid Option")
    

        
