# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 12:11:13 2019

@author: Jiwitesh_Sharma
"""
from bs4 import BeautifulSoup as bs
import os
import json
import urllib.request
import urllib.parse
import urllib.error

class ImageScrapper:


    def createURL(keyWord):
        keyWord= keyWord.split()
        keyWord='+'.join(keyWord)
        url="https://www.google.co.in/search?q="+keyWord+"&source=lnms&tbm=isch"
        return url
        #print (url)
        #add the directory for your image here
    
    def get_RawHtml(url,header):
        #url = "https://acadgild.com/customers/reviews"
        #header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
        req = urllib.request.Request(url, headers = header)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        html = bs(respData, 'html.parser')
        return html
        
    # contains the link for Large original images, type of  image
    def getimageUrlList(rawHtml):
        imageUrlList=[]
        for a in rawHtml.find_all("div",{"class":"rg_meta"}):
            link , imageExtension =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
            imageUrlList.append((link,imageExtension))
        
        print  ("there are total" , len(imageUrlList),"images")
        return imageUrlList
    
    def downloadImagesFromURL(imageUrlList, header):
        masterListOfImages = []
        
        ###print images
        imageFiles = []
        imageTypes = []
        #header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
        #        }
        for i , (img , Type) in enumerate( imageUrlList):
            try:
                req = urllib.request.Request(img, headers = header)
                respData = urllib.request.urlopen(req)
                raw_img = respData.read()
                #soup = bs(respData, 'html.parser')
                
                imageFiles.append(raw_img)
                imageTypes.append(Type)
               
            except Exception as e:
                print ("could not load : "+img)
                print (e)
        masterListOfImages.append(imageFiles)
        masterListOfImages.append(imageTypes)
        
        return masterListOfImages
    
    ''' for i , (img , Type) in enumerate( imageUrlList):
           try:
               req = urllib.request.Request(img, headers = header)
               respData = urllib.request.urlopen(req)
               raw_img = respData.read()
       
               cntr = len([i for i in os.listdir(fileLoc) if image_type in i]) + 1
               print (cntr)
               if len(Type)==0:
                   f = open(os.path.join(fileLoc , image_type + "_"+ str(cntr)+".jpg"), 'wb')
               else :
                   f = open(os.path.join(fileLoc , image_type + "_"+ str(cntr)+"."+Type), 'wb')
       
       
               f.write(raw_img)
               f.close()
           except Exception as e:
               print ("could not load : "+img)
               print (e)'''
            
   
        