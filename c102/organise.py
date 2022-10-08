# importando os pacotes
from importlib.resources import path
import os
import shutil

# criando variáveis para armazenar os caminhos dos diretórios
from_dir = "D:/Documentos/BYJUS/AulasVScode/Aulas/Alunos/Aluno 0/Python/c102/assets"
to_dir = "D:/Documentos/BYJUS/AulasVScode/Aulas/Alunos/Marco/Python/c102/assets"

# exibindo os arquivos existentes no diretório de origem
list_of_files = os.listdir(from_dir)
print(list_of_files)

# iniciando o processo de copiar/mover os arquivos
for file_name in list_of_files:
  # separando nome e extensão dos arquivos
  name, extension = os.path.splitext(file_name)
  
  # verificando a extensão dos arquivos para saber se sao imagens
  if extension == '':
    continue
  if extension in ['.gif','.png','.jpg','.jpeg','.jfif']:
    path1 = from_dir + '/' + file_name
    path2 = to_dir + '/' + "Arquivos_imagem"
    path3 = to_dir + '/' + "Arquivos_imagem" + '/' + file_name
    print("path1", path1)
    print("path3",path3)
    
    # movendo os arquivos para a nova pasta
    if os.path.exists(path2):
      print(f'Movendo {file_name} ...')
      shutil.move(path1,path3)
    else:
      os.mkdir(path2)
      print(f'Movendo {file_name} ...')
      shutil.move(path1,path3)