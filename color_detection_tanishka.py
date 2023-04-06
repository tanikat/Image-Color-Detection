import cv2
import numpy as np
import pandas as pd

img_path = "C://Users//Admin//Downloads//Tanishka color//colordetection.jpg"
img = cv2.imread(img_path)
img=cv2.resize(img,(700,500))

clicked = False
r = g = b = xpos = ypos = 0

index=["color","color_nm","hex","R","G","B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

def getColor(R,G,B):
    mini = 10000
    for i in range(len(csv)):
        d = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(d<=mini):
            mini = d
            cname = csv.loc[i,"color_nm"]
    return cname

def draw_function(event, x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
       
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)

while(1):
    cv2.imshow("image",img)
    if (clicked):
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        txt = getColor(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        cv2.putText(img, txt,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked=False
  
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()
