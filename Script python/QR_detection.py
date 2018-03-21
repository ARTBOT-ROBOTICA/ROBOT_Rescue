import zbar
import numpy as np
import cv2

capture = cv2.VideoCapture(1)
#"http://192.168.1.68:9000/?action=stream"
font = cv2.FONT_HERSHEY_SIMPLEX

while 1:
    val, frame = capture.read()

    if val:

        frame_gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        dimensiones = frame_gris.shape  
        imagen_zbar = zbar.Image(dimensiones[1], dimensiones[0], 'Y800', frame_gris.tobytes())
        escaner = zbar.ImageScanner()
        escaner.scan(imagen_zbar)
        for codigo_qr in imagen_zbar:
            loc = codigo_qr.location 
            dat = codigo_qr.data[:-2] 
            localizacion = np.array(loc, np.int32)
 
            cv2.polylines(frame, [localizacion], True, (255,0,0), 2)
 
            cx = (loc[0][0]+loc[2][0])/2
            cy = (loc[0][1]+loc[2][1])/2
            cv2.putText(frame,dat,(cx,cy), font, 0.7,(255,255,255),2)
        cv2.imshow('Imagen', frame)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
