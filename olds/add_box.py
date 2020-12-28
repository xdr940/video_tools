"""
目的：将原图片(img)与其xml(xml)，合成为打标记的图片(labelled)，矩形框标记用红色即可
已有：（1）原图片文件夹(imgs_path)，（2）xml文件夹(xmls_path)
思路：
    step1: 读取（原图片文件夹中的）一张图片
    step2: 读取（xmls_path）该图片的xml文件，并获取其矩形框的两个对角顶点的位置
    step3: 依据矩形框顶点坐标，在该图片中画出该矩形框
    step4: 图片另存为'原文件名'+'_labelled'，存在‘lablled’文件夹中
"""
from tqdm import tqdm
import os
import cv2 as cv
import xml.etree.ElementTree as ET
from path import Path


def xml_jpg2labelled(imgs_path, xmls_path, labelled_path):
    imgs_path = Path(imgs_path)
    xmls_path = Path(xmls_path)
    labelled_path = Path(labelled_path)
    labelled_path.mkdir_p()

    imgs_list = imgs_path.files()
    imgs_list.sort()

    xmls_list = xmls_path.files()
    xmls_list.sort()

    nums = len(imgs_list)
    for i in range(nums):
        img_path =  imgs_list[i]
        xml_path = xmls_list[i]
        img = cv.imread(img_path)
        labelled = img
        root = ET.parse(xml_path).getroot()
        objects = root.findall('object')
        for obj in objects:
            bbox = obj.find('bndbox')
            xmin = int(bbox.find('xmin').text.strip())
            ymin = int(bbox.find('ymin').text.strip())
            xmax = int(bbox.find('xmax').text.strip())
            ymax = int(bbox.find('ymax').text.strip())
            labelled = cv.rectangle(labelled, (xmin, ymin), (xmax, ymax), (0, 0, 255), 2)
        cv.imwrite(labelled_path/"{}.jpg".format(img_path.stem),labelled)
        # cv.imshow('labelled', labelled)
        # if cv.waitKey(100) & 0xff == ord('q'):
        #     break


if __name__ == '__main__':
    imgs_path = './00516s/'
    xmls_path = './00516s_xml/'
    labelled_path = './00516s_labelled'
    xml_jpg2labelled(imgs_path, xmls_path, labelled_path)