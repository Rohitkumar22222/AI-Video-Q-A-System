# converts these videos to mp3
import os
import subprocess
files = os.listdir("videos")
# print(files)

for file in files:
    tutorial_number = file.split("Tutorial_#")[1].split("(")[0]
    file_name = file.split("___")[0]
    print(tutorial_number, file_name)
    subprocess.run(["ffmpeg" , "-i" , f"videos/{file}" , f"audios/{tutorial_number}_{file_name}.mp3"])
    