#importar o módulo time
import time
from playsound import playsound

#defina uma função de contagem regressiva
def countDown_timer(seconds):
  while seconds > 0:
    mins = int(seconds / 60)
    secs = int(seconds % 60)
    timer = f'{mins}:{secs} '
    
    print(f"{timer}" ,end='\r')
    time.sleep(1)
    seconds -= 1
  
  print('Tempo esgotado!')
  time.sleep(1)
  

#digite e tempo em segundos
seconds = input("Digite o tempo em segundos")

#chamada da função
countDown_timer(int(seconds))