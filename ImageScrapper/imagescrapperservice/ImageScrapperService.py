# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:26:53 2019

@author: Jiwitesh_Sharma
"""

from dao import DAO
from imagescrapper.ImageScrapper import ImageScrapper
from PIL import Image
from imagescrapperutils.ImageScrapperUtils import ImageScrapperUtils
import pdb
class ImageScrapperService:
    
    utils = ImageScrapperUtils
    imgScrapper = ImageScrapper
    dao = DAO
    keyWord = ""
    fileLoc = ""
    image_name = ""
    header = ""
    '''def __main__(keyWord, image_name, fileLoc, header):
    keyWord = keyWord
    fileLoc = fileLoc
    image_name = keyWord
    dao = DAO
    utils = ImageScrapperUtils
    imgScrapper = ImageScrapper'''
    # you can change the query for the image  here
    
    #pdb.set_trace()
    
    def downloadImages( keyWord, header):  
        imgScrapper = ImageScrapper
        url = imgScrapper.createURL(keyWord)
        rawHtml = imgScrapper.get_RawHtml(url, header)
        
        imageURLList = imgScrapper.getimageUrlList(rawHtml)
        
        masterListOfImages = imgScrapper.downloadImagesFromURL(imageURLList, header)
        
        return masterListOfImages
    
    def insertImagesIntoDB(imageList, image_name):
        dao = DAO
        dao.insert_image(imageList, image_name)
    def pullImages(image_name):
        #image_name = 'jiwitesh'
        #utils = ImageScrapperUtils
        dao = DAO
        imageList = dao.retrieve_image(image_name)
        #imageTypes =[]
        #imageFiles, imageTypes, fileLoc, keyWord 
        #utils.storeImage(imageList, imageTypes, fileLoc, image_name)
        return imageList
        #for image in imageList.keys():
        #   print(image)
        #    imageList.get(image)
    