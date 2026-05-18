import cv2
import numpy as np

def handle_bar(v):
    pass

# Carregando imagens
img_rgb = cv2.imread("assets/pork_frame.png")
img_rgb = cv2.resize(img_rgb, None, fx=0.5, fy=0.5)
img_hsv = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2HSV)

# Criando uma janela chamada Track Bars (é importante manter o mesmo nome)
cv2.namedWindow("Track Bars")

# Criando uma track bar propiamente dita
cv2.createTrackbar("Hue Min.", # Nome da track bar
                   "Track Bars", # Qual janela que vai ser colocada (tem que ser o mesmo nome que criamos)
                   131, # Valor minimo que vai aparecer na barra
                   179, # Valor maximo que vai aparecer na barra
                   handle_bar # call back function pra controlar a barra
                  )

# Repetindo o processo para todos os canais
cv2.createTrackbar("Hue Max.", "Track Bars", 159, 179, handle_bar)
cv2.createTrackbar("Sat. Min.", "Track Bars", 0, 255, handle_bar)
cv2.createTrackbar("Sat. Max.", "Track Bars", 255, 255, handle_bar)
cv2.createTrackbar("Val. Min.", "Track Bars", 0, 255, handle_bar)
cv2.createTrackbar("Val. Max.", "Track Bars", 168, 255, handle_bar) 

while True:

    # Pegando os valores de cada uma das barras
    h_min = cv2.getTrackbarPos("Hue Min.", "Track Bars")
    h_max = cv2.getTrackbarPos("Hue Max.", "Track Bars")
    s_min = cv2.getTrackbarPos("Sat. Min.", "Track Bars")
    s_max = cv2.getTrackbarPos("Sat. Max.", "Track Bars")
    v_min = cv2.getTrackbarPos("Val. Min.", "Track Bars")
    v_max = cv2.getTrackbarPos("Val. Max.", "Track Bars")

    print("-" * 50)
    print(f"Hue: [{h_min}, {h_max}]\nVal: [{s_min}, {s_max}]\nSat: [{v_min}, {v_max}]")
    print("-" * 50)

    # Criando uma mascara para funcionar como segmentação
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(img_hsv, lower, upper)

    cv2.imshow("RGB", img_rgb)
    cv2.imshow("HSV", img_hsv)
    cv2.imshow("Track Bars", mask)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break