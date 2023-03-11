import cv2

img = cv2.imread("D:/Documentos/BYJUS/AulasVScode/Aulas/Alunos/Aluno 0/Python/c103/Image_Files/story_image_1.png")

# cv2.imshow("Imagem de Exibição",img)
#cv2.waitKey(0)
#print(img)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Escala de cinza",gray_img)
# cv2.waitKey(0)
# print(gray_img)


import cv2


img = cv2.imread("D:/Documentos/BYJUS/AulasVScode/Aulas/Alunos/Aluno 0/Python/c103/Image_Files/story_image_1.png")
img2 = cv2.imread("D:/Documentos/BYJUS/AulasVScode/Aulas/Alunos/Aluno 0/Python/c103/Image_Files/story_image_2.png")

cv2.imshow("Janela 1",img)
cv2.imshow("Janela 2",img2)

gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Janela 3",gray_img)

print(img)

cv2.waitKey(0)




