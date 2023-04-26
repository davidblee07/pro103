import os
import time
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

origem = "C:/Users/PC/Downloads"
destino = "C:/Users/PC/Desktop/Byjus David/Arquivos_Documentos"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
 
 def on_created(self, event):
    print(f"{event.src_path} foi criado")
    name, extension = os.path.splitext(event.src_path)
    for key,value in dir_tree.items():
      if extension in value:
        file_name = os.path.basename(event.src_path)
        path1 = origem+"/"+key
        path2 = destino+"/"+key
        path3 = destino+"/"+key+"/"+file_name
        if(os.path.exists(path2)):
          print('movendo o arquivo')
          shutil.move(path1, path3)
        else:
          os.makedirs(path2)  
          print('movendo o arquivo')
          shutil.move(path1, path3)

 def on_deleted(self, event):
    print(f"Opa! Alguém excluiu{event.src_path}!")
    name, extension = os.path.splitext(event.src_path)
    for key,value in dir_tree.items():
      if extension in value:
        file_name = os.path.basename(event.src_path)
        path1 = origem+"/"+key
        path2 = destino+"/"+key
        path3 = destino+"/"+key+"/"+file_name
        if(os.path.exists(path2)):
          print('movendo o arquivo')
          shutil.move(path1, path3)
        else:
          os.makedirs(path2)  
          print('movendo o arquivo')
          shutil.move(path1, path3)

 def on_modified(self, event):
    print(f"{event.src_path} foi modificado")
    name, extension = os.path.splitext(event.src_path)
    for key,value in dir_tree.items():
      if extension in value:
        file_name = os.path.basename(event.src_path)
        path1 = origem+"/"+key
        path2 = destino+"/"+key
        path3 = destino+"/"+key+"/"+file_name
        if(os.path.exists(path2)):
          print('movendo o arquivo')
          shutil.move(path1, path3)
        else:
          os.makedirs(path2)  
          print('movendo o arquivo')
          shutil.move(path1, path3)

 def on_moved(self, event):
    print(f"{event.src_path} foi movido")
    name, extension = os.path.splitext(event.src_path)
    for key,value in dir_tree.items():
      if extension in value:
        file_name = os.path.basename(event.src_path)
        path1 = origem+"/"+key
        path2 = destino+"/"+key
        path3 = destino+"/"+key+"/"+file_name
        if(os.path.exists(path2)):
          print('movendo o arquivo')
          shutil.move(path1, path3)
        else:
          os.makedirs(path2)  
          print('movendo o arquivo')
          shutil.move(path1, path3)

    event_handler = FileMovementHandler()

    observer = Observer()

    observer.schedule(event_handler, origem, recursive=True)
    
    observer.start()  

    try:
      while True:
             time.sleep(2)
             print("executando...")
    except KeyboardInterrupt:
             print("Interrompido!")
             observer.stop()     
