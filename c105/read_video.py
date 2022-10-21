import cv2
from cv2 import waitKey

video = cv2.VideoCapture("D:/Documentos/BYJUS/AulasVScode/Aulas/Alunos/Aluno 0/Python/c105/AnthonyShkraba.mp4")

if (video.isOpened() == False):
  print("Não foi possível abrir o vídeo!")
  
video_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
video_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
video_fps = int(video.get(cv2.CAP_PROP_FPS))

# print(video_height)
# print(video_width)
# print(video_fps)

copia = cv2.VideoWriter("D:/Documentos/BYJUS/AulasVScode/Aulas/Alunos/Aluno 0/Python/c105/copia.mp4",cv2.VideoWriter_fourcc(*'DIVX'),30,(video_width,video_height))

while True:
  ret,frame = video.read()
  copia.write(frame)
  cv2.imshow("video 1",frame)
  
  if waitKey(15) == 32:
    break
  
copia.release()

cv2.destroyAllWindows()

