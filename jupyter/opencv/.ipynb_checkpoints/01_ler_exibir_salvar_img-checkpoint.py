import cv2

# Método para carregar a imagem
# O primeiro parâmetro é o path para a imagem
# O segundo é uma flag que informamos como a imamgem deve ser carregada
# Os dois modos principais são: cv2.IMREAD_COLOR (default) e cv2.IMREAD_GRAYSCALE
# Se o path estiver errado, você recebe o erro -215
img = cv2.imread("assets/goku.png", cv2.IMREAD_COLOR)

# Método interno do opencv que carrega uma nova janela para mostrar a imagem
# O primeiro parâmetro é o nome que aparece na janela e o segundo a imagem em si
# ATENÇÃO: mesmo em BGR o imshow mostra a imagem corretamente. Isso pode ser fonte erro!
cv2.imshow("Goku", img)

# Método para permitir a exibição da nova janela por N milisegundos ou
# até uma tecla ser pressionada
cv2.waitKey()

# Método para salvar/escrever uma imagem
# Podemos, inclusive, alterar o formato da imagem 
cv2.imwrite("novo_goku.jpg", img)
