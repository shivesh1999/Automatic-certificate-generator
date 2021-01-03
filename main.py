#Python libraries


from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import cv2

# function for getting the coordinates for name placment
def click_event(event, x, y, flags, params): 
    global mouseX,mouseY
    # checking for left mouse clicks 
    if event == cv2.EVENT_LBUTTONDOWN: 
        # displaying the coordinates on the Shell 
        print(x, ' ', y) 
        # displaying the coordinates on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(img, str(x) + ',' +
                    str(y), (x,y), font, 
                    1, (255, 0, 0), 2) 
        cv2.imshow('image', img)
        mouseX,mouseY = x,y

# driver function 
if __name__=="__main__": 
    
    cv2.namedWindow("image", cv2.WINDOW_NORMAL) 
    img = cv2.imread('certificate.jpg', 1) 
    #resisizing to fit different sizes of certificates
    imS = cv2.resize(img, (960, 540))  
    cv2.imshow('image', imS) 
    # setting mouse hadler for the image and calling the click_event() function 
    cv2.setMouseCallback('image', click_event) 
    # wait for a key to be pressed to exit 
    cv2.waitKey(0) 
    clname=['name']
    df = pd.read_csv('list.csv',names=clname,header=None)
    font = ImageFont.truetype('arial.ttf',120)
    for index,j in df.iterrows():
        img1 = Image.open('certificate.jpg')
        draw = ImageDraw.Draw(img1)
        draw.text(xy=(mouseX,mouseY),text='{}'.format(j['name']),fill=(0,0,0),font=font)
        img1.save('{}.jpg'.format(j['name']))

  