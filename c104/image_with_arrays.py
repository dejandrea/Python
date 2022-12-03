import numpy as np
import cv2

# criando imagens

black = np.zeros([600,600])

# f_row = black[1:2]
# print(f_row)

# f_col = black[:,1:2]
# print(f_col)

black[200:400,200:400] = 255
print(black)

cv2.imshow("Preto",black)
# print(black)
cv2.waitKey(0)


import cv2
import numpy as np 

black = np.zeros([600,600])


# f_row = black[1:2]
# print(f_row)

# f_col = black[:,1:2]
# print(f_col)

black[200:400,200:400] = 115

print(black)
cv2.imshow("janela",black)
cv2.waitKey(0)



