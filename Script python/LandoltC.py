import cv2

diff1 = cv2.imread('lanc.png')
diff2 = cv2.imread('lanc2.png')

diff_total = cv2.absdiff(diff1, diff2)

imagen_gris = cv2.cvtColor(diff_total, cv2.COLOR_BGR2GRAY)
contours, _ = cv2.findContours(imagen_gris, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    if cv2.contourArea(c) >= 20:
        posicion_x, posicion_y, ancho, alto = cv2.boundingRect(c)
        cv2.rectangle(diff1, (posicion_x, posicion_y), (posicion_x + ancho, posicion_y + alto), (0, 0, 255),
                      2)

while (1):
    cv2.imshow('Imagen1', diff1)
    cv2.imshow('Imagen2', diff2)
    cv2.imshow('Diferencias detectadas', diff_total)
    tecla = cv2.waitKey(5) & 0xFF
    if tecla == 27:
        break

cv2.destroyAllWindows()
