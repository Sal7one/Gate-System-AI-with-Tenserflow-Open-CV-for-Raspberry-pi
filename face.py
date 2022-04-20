import cv2
import face_recognition
from time import sleep

def change_brightness(img, value= 30):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v,value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return img



def face_detect():
        face_cap = cv2.VideoCapture(0)
        face_cascading = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')

        while(True):
            # Capture frame-by-frame
            ret, frame = face_cap.read()
            face_Detection = face_cascading.detectMultiScale(frame)
            wroteimage = False
            for(x, y, w, h) in face_Detection: # show the photo frames
                myimg = "img1.png"
                ROI = frame[y:y+h, x:x+w] #ROI --> rejoin of interest
                cv2.imwrite(myimg, ROI)
                color = (0,0,255)
                stroke = 2
                wid=x+w
                hig=y+h
                cv2.rectangle(frame,(x, y),(wid, hig), color, stroke)
                wroteimage = True
            
            # cv2.imshow('Live Photo', frame)
            if(wroteimage):
                cv2.waitKey(60)
                break
        face_cap.release()

def tawakkalna_detect():

            face_cap2 = cv2.VideoCapture(0)
            face_cascading2 = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt.xml')

            while(True):
                # Capture frame-by-frame
                ret, frame2 = face_cap2.read()
                face_Detection2 = face_cascading2.detectMultiScale(frame2)
                
                wroteimage = False
                for(x, y, w, h) in face_Detection2: # show the photo frames
                    print(x,y,w,h)
                    ROI2 = frame2[y:y+h, x:x+w] #ROI --> rejoin of interest
                    ROI2 = change_brightness(ROI2, value = -30) # change brightness
                    myimg2 = "img2.png"
                    cv2.imwrite(myimg2, ROI2)
                    color2 = (0,0,255)
                    stroke2 = 2
                    wid2=x+w
                    hig2=y+h
                    cv2.rectangle(frame2,(x, y),(wid2, hig2), color2, stroke2)
                    wroteimage = True

                # cv2.imshow('Tawaklna Photo', frame2)
                if(wroteimage):
                    cv2.waitKey(60)
                    break
            face_cap2.release()

def start():
    personFound = False
    deniedTime = 0
    face_detect()
    while (not personFound):
            print("Please show Tawakllan to the camera")
            sleep(3)
            tawakkalna_detect()
            sleep(0.2)
            
            image1 = face_recognition.load_image_file('img1.png')# livee
            image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)

            face1 = face_recognition.face_locations(image1)
            Encface1 = face_recognition.face_encodings(image1)

            image2 = face_recognition.load_image_file('img2.png')# twakllna
            image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

            face2 = face_recognition.face_locations(image2)

            if(len(face1) and len(face2) > 0):
                face1 = face_recognition.face_locations(image1)[0]
                Encface1 = face_recognition.face_encodings(image1)[0]
                face2 = face_recognition.face_locations(image2)[0]
                Encface2 = face_recognition.face_encodings(image2)[0]
                compareface = face_recognition.compare_faces([Encface1], Encface2,tolerance=0.6)
                personFound = compareface[0]
                if(not personFound):
                    deniedTime+=1
            else:
                deniedTime +=1
            if(deniedTime >=3):
                print("Access denied!!")
                break
            elif not personFound:
                print("Please try again")
                print("Maintain 15 cm distance at least and adjust your phone brightness")
                sleep(2)
                tawakkalna_detect()
            
    return personFound
