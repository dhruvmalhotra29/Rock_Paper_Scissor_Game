import cv2
from keras.models import load_model
import numpy as np
import os


capture = cv2.VideoCapture(0)  ## 0 is the identity of default webcam
i = 0
count = 0
c = 0
p_score = 0
b_score = 0

b_index =3
p_index = 3

model = load_model("./model_weights.h5")
options = ["Paper","Scissor","Stone", " "]

while True:
    
    
    ret,frame = capture.read()   ## ret returns a boolean expression --> 0 if the photo is not captured else 1 & frame is the photo
    
    if ret == False:
        continue
    
    
    
    
    

    if i<10:    
        cv2.putText(frame,"Bot Move: " + str(options[b_index]),(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
        cv2.putText(frame,"Player Move:  " + str(options[p_index]),(300,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
        cv2.putText(frame,"Bot Score : " + str(b_score),(50,450),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2,cv2.LINE_AA)
        cv2.putText(frame,"Player Score : " + str(p_score),(320,450),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
        cv2.rectangle(frame,(150,150),(330,330),(255,0,0),2)  ## It draws a rectangle with the given coordinates and given color & width. 
    
    else:
        if b_score>p_score:
            cv2.putText(frame,"Match Ended : " ,(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
            cv2.putText(frame,"Winner : Bot " ,(150,330),cv2.FONT_HERSHEY_SIMPLEX,1,(255,192,203),2,cv2.LINE_AA)
            
        elif p_score>b_score:
            cv2.putText(frame,"Match Ended : ",(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
            cv2.putText(frame,"Winner : Player ",(150,330),cv2.FONT_HERSHEY_SIMPLEX,1,(255,192,103),2,cv2.LINE_AA)
            
        else:
            cv2.putText(frame,"Match Ended : ",(20,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2,cv2.LINE_AA)
            cv2.putText(frame,"Match Ties! ",(150,330),cv2.FONT_HERSHEY_SIMPLEX,1,(255,192,203),2,cv2.LINE_AA)
            
        
            

            

    count+=1
    
    offset = 10
    image = frame[150:330,150:330]
    
 
    

    
    
    
        # 1. Image
        # 2. Text_data that you want to write
        # 3. Coordinate where you want the text
        # 4. Type of Font
        # 5. Font scale
        # 6. Color
        # 7. Thickness
        # for better_look line type is "Line_AA"
        

        
    cv2.imshow("Game",frame)
 

    
    if count%300==0 and i<10:
        i+=1
        c+=1
        #Saves the frames with frame-count 
        cv2.imwrite("./test_data/ " + str(c) + ".jpg",image) 
        print("Image: " + str(count) + " saved")
        

        # Covert to RGB
        img  = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        # Covert to gray
        gray  = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        # create a binary thresholded image
        _, binary = cv2.threshold(gray,145,120, cv2.THRESH_BINARY_INV)
        
     
        
        
        
        binary = cv2.resize(binary,(22500,3))
        binary = np.reshape(binary,(1,150,150,3)) 
        
        
        
        
        
        p_index = np.argmax(model.predict(binary))
        print(options[p_index])
        
        b_index = np.random.randint(3)

        
        if p_index ==0 and b_index==1:
            b_score += 1
        
        elif p_index == 0 and b_index == 2:
            p_score += 1
        
        elif p_index ==1 and b_index ==0:
            p_score += 1
        
        elif p_index ==1 and b_index ==2:
            b_score += 1
            
        elif p_index==2 and b_index == 0:
             b_score += 1
            
        elif p_index==2 and b_index == 1:
            p_score += 1
            
        else:
            p_score += 0
            b_score += 0 
            
        try:
             os.remove("./test_data/ "+ str(c) + ".jpg")
        
        except:
            pass
        

    
    key_pressed = cv2.waitKey(1) & 0xFF  ## Bitwise operation performed to get ascii value of entered character
    
    if key_pressed == ord('q'):
        break                      ## ord(ch)  where ch is any alphabet . It returns the ASCII value.


    
        
capture.release()   ## It releases the webcamera
cv2.destroyAllWindows()   ## It destroys all the windows
    
    