import subprocess
from PIL import Image
import cv2
import uuid
import os

IMG_PATH='images'
def detect_object():
    
    #  unique_id=str(uuid.uuid4())
    #  dir_path=os.path.join(IMG_PATH,unique_id)
    #  dir_path_abs=os.path.abspath(dir_path)
    #  os.mkdir(dir_path)


    #  source_img_path=os.path.join(IMG_PATH,unique_id,'source_'+filename)

    source_img_path='source.jpg'
    source_abspath=os.path.abspath(source_img_path)

    command=f'cd yolov5 && python detect.py --weights best.pt --img 1280 --conf 0.4 --source {source_abspath} --dest .'

    print(command)
    subprocess.run(command,shell=True)
    detection=Image.open('img.jpg')
    results_file=open('results.csv','r')
    text=results_file.read().split(' ')


    return  detection,*(int(x) for x in text)
    


