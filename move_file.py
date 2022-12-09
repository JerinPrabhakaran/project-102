import os
import shutil
x = 0

from_dir = "C:/Users/sjeri/OneDrive/Desktop/downloads"
to_dir = "C:/Users/sjeri/OneDrive/Documents/coding/Python/project 102"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for x in list_of_files :
  name,extension = os.path.splitext(x)
  print(extension)
      
  if extension == '':
   continue
  if extension in ['.gif', '.png', '.jpg', '.jpeg','.bmp']:
            
        path1 = from_dir + '/' + x
        path2 = to_dir + '/' + "Image_Files" 
        path3 = to_dir + '/' + "Image_Files" + '/' + x     
        

        if os.path.exists(path2):
            print("Moving " + x + ".....")

            shutil.move(path1, path3)
            print("j")

        else:
            os.makedirs(path2)
            print("Moving " + x + ".....")
            shutil.move(path1, path3)
            print("j")
  else:
        if extension in ['.doc', '.docx', '.txt', '.pdf','.xlsx']:
       
         path4 = from_dir + '/' + x
         path5 = to_dir + '/' + "documents" 
         path6 = to_dir + '/' + "documents" + '/' + x 

        if os.path.exists(path5):
            print("Moving " + x + ".....")

            shutil.move(path4, path6)
            print("e")

        else:
            os.makedirs(path5)
            print("Moving " + x + ".....")
            shutil.move(path4, path6)
            print("e")