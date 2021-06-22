import os


def check_object(type_file, filename):
    path = "\\".join(os.getcwd().split("\\")[:os.getcwd().split("\\").index("SnakeReincarnation")+1])
    for file in os.listdir(path+"\\"+"Source"+"\\"+type_file+"\\"):
        if filename == file.split(".")[0]:
            return True
    return False
