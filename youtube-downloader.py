# importing the module
from pytube import *

# where to save
SAVE_PATH = "C:\\"

# link of the video to be downloaded
link = input("Your link: ")

try:
    # object creation using YouTube
    # which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error")  # to handle exception

# filters out all the files with "mp4" extension
try:
    yt.streams.filter(progressive=True,
                      file_extension="mp4").first().download(output_path=SAVE_PATH)
except:
    print("Some Error!")
print('Task Completed!')
