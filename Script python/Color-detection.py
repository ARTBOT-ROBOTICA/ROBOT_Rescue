import cv2
import numpy as np

captura = cv2.VideoCapture(1)

while (1):

    _, imagen = captura.read()
    hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    #azul_bajos = np.array([94, 162, 75], dtype=np.uint8)
    #azul_altos = np.array([109, 255, 255], dtype=np.uint8)
    #rojo_bajos = np.array([137, 107, 136], dtype=np.uint8)
    #rojo_altos = np.array([208, 255, 255], dtype=np.uint8)
    #amarillo_bajos = np.array([9, 92, 138], dtype=np.uint8)
    #amarillo_altos = np.array([30, 255, 255], dtype=np.uint8)

    verde_bajos = np.array([94, 162, 75], dtype=np.uint8)
    verde_altos = np.array([109, 255, 255], dtype=np.uint8)
    moments = cv2.moments(mask)
    area = moments['m00']

    if (area > 2000000):
        x = int(moments['m10'] / moments['m00'])
        y = int(moments['m01'] / moments['m00'])
        print "x = ", x
        print "y = ", y
        cv2.rectangle(imagen, (x, y), (x + 5, y + 5), (0, 0, 255), 5)
        cv2.imshow('mask', mask)

    cv2.imshow('Camara', imagen)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break

cv2.destroyAllWindows()