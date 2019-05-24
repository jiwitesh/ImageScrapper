# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:12:33 2019

@author: Jiwitesh_Sharma
"""

from imagescrapperservice.ImageScrapperService import ImageScrapperService
from PIL import Image
class ImageScrapperClient:
    
    
    keyWord = input("Enter your keyword")
    fileLoc="Pictures"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    
    image_name= keyWord.split()
    image_name='+'.join(image_name)
    service = ImageScrapperService
    #service.__main__(keyWord, image_name, fileLoc, header)
    masterListOfImages = service.downloadImages(keyWord, header)
    imageList = masterListOfImages[0]
    imageTypeList = masterListOfImages[1]
    
    service.insertImagesIntoDB(imageList, image_name)
    
    image_name = "jiwitesh"
    imagesList = service.pullImages(image_name)
    for image in imagesList.keys():
        imagesList.get(image)
    
    
