import os, shutil

imageTypes = [".png", ".jpeg", ".jpg", ".gif", ".tiff", ".bmp"]
documentTypes = [".doc", ".docx", ".pdf", ".odt", "rtf", ".txt", ".ppt", ".pptx"]
musicTypes = [".mp3", ".wav", ".flac"]
videoTypes = [".mp4", ".avi", ".flv", ".mov"]


files = []

def Clean():
    files = os.listdir(GetPath()) # return array of file names (string)

    Move(files)

    print("Success!")


def GetPath():
    desktopPath = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 

    return desktopPath

def Move(files):
    for i, file in enumerate(files):
        for x, image in enumerate(imageTypes):
            if image in file:
                MoveImage(file)
                break
        for y, document in enumerate(documentTypes):
            if document in file:
                MoveDocument(file)
                break
        for z, music in enumerate(musicTypes):
            if music in file:
                MoveMusic(file)
                break
        for a, video in enumerate(videoTypes):
            if video in file:
                MoveVideo(file)
                break

def MoveImage(file):
    shutil.move(GetPath() + "\\" + file, os.path.join(os.path.join(os.environ['USERPROFILE']), 'Pictures') )
def MoveDocument(file):
    shutil.move(GetPath() + "\\" + file, os.path.join(os.path.join(os.environ['USERPROFILE']), 'Documents') )
def MoveMusic(file):
    shutil.move(GetPath() + "\\" + file, os.path.join(os.path.join(os.environ['USERPROFILE']), 'Music') )
def MoveVideo(file):
    shutil.move(GetPath() + "\\" + file, os.path.join(os.path.join(os.environ['USERPROFILE']), 'Videos') )