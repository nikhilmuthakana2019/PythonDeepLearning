import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# Functions 

def canny_detection(frame):
    # Convert input frame to grayscale since RGB is not required for white lane detection
    gray_frame = cv.cvtColor(frame, cv.COLOR_RGB2GRAY)
    font = cv.FONT_HERSHEY_DUPLEX 
    cv.putText(gray_frame, 'Press q to quit', (50, 50),  
                font, 1, (255, 255, 255), 1, cv.LINE_4)
    cv.imshow("Grayscale",gray_frame)
    
def show_input_video(frame):
    # Display the input video in a new window
    font = cv.FONT_HERSHEY_DUPLEX 
    cv.putText(frame, 'INPUT VIDEO, Press q to quit', (50, 50),  
                font, 1, (255, 255, 255), 1, cv.LINE_4)
    cv.imshow("Input",frame)
    
    

# Main 
# Place a sample video in the working directory
input_video = cv.VideoCapture("sample.mp4") # Replace sample.mp4 with your video name
while (input_video.isOpened()):
    # Read each frame of the video using the variables:
    # ret = a boolean return value from getting the frame
    # frame = the current frame being projected in the video
    ret,frame = input_video.read()
    # show_input_video(frame) # Display input video
    canny_detection(frame) # Convert to grayscale and display
    if cv.waitKey(20) & 0xFF == ord('q'):
        break
# Close the windows and remove video from memory
input_video.release()
cv.destroyAllWindows()