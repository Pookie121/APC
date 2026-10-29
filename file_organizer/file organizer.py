import os
import shutil

path = r"C:\Users\SAKSHI PATIL\OneDrive\Desktop\python\File organizer"

for file in os.listdir(path):
    if os.path.isfile(os.path.join(path, file)):
        ext = file.split(".")[-1] if "." in file else "Others"
        folder = path + "\\" + ext
        os.makedirs(folder, exist_ok=True)
        shutil.move(path + "\\" + file, folder)

print("Files organized successfully!")
