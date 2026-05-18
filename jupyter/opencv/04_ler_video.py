import cv2

# Podemos passar como parametro um path ou um número que indica qual câmera queremos ler
video_capture = cv2.VideoCapture("assets/mais8k.mp4") # ler o video do path
# video_capture = cv2.VideoCapture(1) # ler uma webcam 0

# Ler um vídeo é diferente de ler uma imagem. Na verdade o video nada mais é do que uma sequencia de imagens (frames)
# para isso, fazemos um loop para ler todos os frames do video
while True:

    # O método read() vai ler o video e retornar duas infomações:
    # is_ok: se o frame foi lido corretamente
    # frame: o frame do video (np.ndarray)
    is_ok, frame = video_capture.read()
    if not is_ok:
        print("Houve algum problema em carregar o video ou ele acabou")
        break

    # Resize frame of video to 1/4 size for faster face detection processing
    # frame = cv2.resize(frame, None, fx=0.25, fy=0.25)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Para não ficar lendo pra sempre, precisamos de uma maneira de encerrar o vídeo
    # neste caso, esperamos apertar a letra q para fechar
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Agora a gente libera o objeto que esta capturando o vídeo (é similar quando fechamos um arquivo)
# e vamos destruir todas as janelas que o cv2 criou
video_capture.release()
cv2.destroyAllWindows() 
