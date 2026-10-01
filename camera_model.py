import cv2

class Camera:
    def __init__(self, cam_num):
        self.cam_num = cam_num
        self.vid = cv2.VideoCapture(self.cam_num)
        
    def set_dimensions(self, height, width):
        """Define y aplica las dimensiones a la cámara"""
        self.height = height
        self.width = width
        self.vid.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)  
        self.vid.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        
    def find_max(self):
        """Halla las dimensiones maximas que la camara puede abarcar y los devuelve en forma de tupla"""
        self.max_width = int(self.vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.max_height = int(self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        return (self.max_height, self.max_width)
        
    def close(self):
        """Cierra la cámara"""
        if self.vid.isOpened():
            self.vid.release()
        cv2.destroyAllWindows()
        
    def show_video(self, stop_key):
        if not isinstance(stop_key, str) or len(stop_key) != 1:
            return 'Debe ser un string de un solo caracter'
        
        if not self.vid.isOpened():
            return 'Error: No se pudo accder a la camara'
        
        while True:
            rect, frame = self.vid.read() #Returns a tuple (rect, frame)
            #rect / ret --> boolean indicating if whether the frame reading was done correctly or not, or if the video is still on or not.
            #frame --> numPy matrix, contains the actual frame pixels in BGR format. If ret = False --> frame = None
            
            if not rect:
                print('No se pudo recibir el fotograma')
                break
            
            cv2.imshow('Video', frame)
    
            if cv2.waitKey(1) & 0xFF == ord(stop_key.lower()): #Waits every 1 ms for a keyboard event
                break
        
        self.close()
