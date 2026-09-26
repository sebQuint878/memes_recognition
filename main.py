import cv2

vid = cv2.VideoCapture(0)

vid.set(cv2.CAP_PROP_FRAME_WIDTH, 10000)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 10000)

max_ancho = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
max_alto = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(f"Resolución máxima detectada: {max_ancho}x{max_alto}")

while True:
    rect, frame = vid.read() #Returns a tuple (rect, frame)
    #rect / ret --> boolean indicating if whether the frame reading was done correctly or not, or if the video is still on or not.
    #frame --> numPy matrix, contains the actual frame pixels in BGR format. If ret = False --> frame = None
    
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows() 
