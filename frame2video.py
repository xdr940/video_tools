import cv2
from path import Path
from tqdm import tqdm
import argparse

import matplotlib.pyplot as plt


parser =argparse.ArgumentParser(description="generate histogram ")
parser.add_argument('--path',
                    #default='/home/roit/datasets/Binjiang/0008/',
                    #default='/media/roit/greenp2/output_dir/0020'
                    default='/home/roit/bluep2/test_out/vsd/uav0000317_00000_s_ab'
                    #default='/home/roit/datasets/MC/10001000/p2/depth'

                    )
parser.add_argument('--input_size',
                    default=(1600,600),
                    help="width,height")
parser.add_argument('--out_h',default=600,type=int)
parser.add_argument('--out_w',default=1280,type=int)
parser.add_argument('--out_size',default=(1280,600),type=int)

parser.add_argument('--ext',default='png')
parser.add_argument('--dump_root',default='./uav0000317_00000_s_ab.avi')
parser.add_argument('--type',default='rgb',choices=['rgb','gray'])
parser.add_argument('--scales',default=255,choices=[1,255])
parser.add_argument('--near',default='big_value',choices=['small_value','big_value'])
parser.add_argument('--fps',default=30)
args = parser.parse_args()

def main(args):
    fps = args.fps
    dump_root = args.dump_root
    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    #fourcc = cv2.VideoWriter_fourcc(*'XVID')


    videoWriter = cv2.VideoWriter(dump_root, fourcc, fps, args.input_size)   #和输入一样大小wh


    folderName = Path(args.path)
    if folderName.exists()==False:
        print('folder no exist')
        return
    files = folderName.files()
    files.sort()
    for img_p in tqdm(files):
        img = cv2.imread(img_p)
        #img = cv2.resize(img,args.out_size)
        videoWriter.write(img)
    videoWriter.release()
if __name__=='__main__':
    main(args)
    print('ok')
