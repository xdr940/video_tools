from path import Path
import os
from  tqdm import tqdm
import cv2
import matplotlib.pyplot as plt
#path = Path('/home/roit/datasets/MC/10001000/p3/normal')
#path = '/home/roit/datasets/Binjiang/00082'

def rename():
    path = '/home/roit/datasets/scu/seq06'
    path = Path(path)
    files = path.files()
    files.sort()
    ext = files[0].ext
    for idx, item in tqdm(enumerate(files)):
        cmd = 'mv ' + str(item) + ' ' + item.parent / ('{:04}' + ext).format(idx + 1)
        os.system(cmd)


def resize():
    #path = '/home/roit/testouts/vsd/zhou'
    path = "/home/roit/datasets/npmcm2020/airport_1500"
    path = Path(path)
    files = path.files()
    files.sort()
    ext = files[0].ext
    for item in tqdm(files):
        img = cv2.imread(item)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
        #img = cv2.resize(img,(480,270))

        cv2.imwrite(item,img)

def color2gray():
    path = "/home/roit/datasets/npmcm2020/airport_1500"
    #path = '/home/roit/datasets/MC/0000/p1/color'
    dump_dir = '/home/roit/datasets/npmcm2020/airport_1500_gray'
    dump_dir = Path(dump_dir)
    dump_dir.mkdir_p()
    path = Path(path)
    files = path.files()
    files.sort()
    ext = files[0].ext
    for item in tqdm(files):
        img = cv2.imread(item,cv2.IMREAD_GRAYSCALE)
        cv2.imwrite(dump_dir/item.stem+".jpg", img)

if __name__ == '__main__':
    rename()
    #color2gray()