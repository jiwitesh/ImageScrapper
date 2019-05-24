# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:55:29 2019

@author: Jiwitesh_Sharma
"""

from imagescrapperservice.ImageScrapperService import ImageScrapperService
from flask import Flask, render_template, request
from PIL import Image
import os.path
#import request
app = Flask(__name__)
app.debug = True

response = 'Welcome!'
@app.route('/')
def home():
    return render_template('index.html', responses =response )
   
@app.route('/searchImages', methods=['GET'])
def searchImages():
    if request.method == 'POST':
        keyWord = request.form['keyword']
         
    else:
        keyWord = request.args.get('keyword')
    print('printing = '+keyWord)
   
    #keyWord = "jiwitesh"
    image_name= keyWord.split()
    image_name='+'.join(image_name)
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    
    service = ImageScrapperService
    #(imageURLList, header, keyWord, fileLoc)
    masterListOfImages = service.downloadImages(keyWord, header)
    imageList = masterListOfImages[0]
    imageTypeList = masterListOfImages[1]
    
    service.insertImagesIntoDB(imageList, image_name)
    
    imageList = service.pullImages(image_name)
    response = "We have downloaded ", len(imageList) , "images of "+ image_name +" for you"
   
    return home()
@app.route("/searchResult.html")
def searchPage():
    return render_template('searchResult.html')
   
@app.route("/searchData", methods=['GET'])
def searchData():
    if request.method == 'POST':
        image_name = request.form['keyword']
        print("printing = ",image_name)
    else:
        image_name = request.args.get('keyword')
        print("printing = ",image_name)
    #image_name = "ironman"
    #image_name = 'jiwitesh'
    service = ImageScrapperService
    #fileLoc = "static"
    imageList = service.pullImages("jiwitesh")
    
    #if not os.path.exists(fileLoc):
    #    os.mkdir(fileLoc)
    #innerFile = os.path.join(fileLoc, "Pictures")
    #
    #if not os.path.exists(innerFile):
    #    os.mkdir(innerFile)
    
    #imageListKeys = imageList
    #for image in imageListKeys:
    #    f = open(os.path.join(r"static\Pictures"))
        #raw_image = Image.open(image)
        #f = (os.path.join(innerFile))
    #    f.write(imageList.get(image))
    #    f.close()
    #listOfImages = getListOfImages(imageList)
    #images
    #for image in imageList.keys():
    #from PIL import Image
    #"searchResult.html".render(Image)
    imgList = []
    # dir_path can be set outside of your loop
    dir_path = "C:\\Users\\Jiwitesh_Sharma\\ImageScrapper\\ui\\static"
    for image in imageList.keys():
        
        #print(image)
        try:
            #os.path.join(fileName, image), Image.open(imageList.get(image)))
            imgList.append(Image.open(imageList.get(image)))
            raw_image = Image.open(imageList[image])
            name = ("%s" % (image)) + ".jpg"
            file_path = os.path.join( dir_path, name) 
            raw_image.save(file_path)
        except:
            print("Something went wrong when writing to the file")
        finally:
            raw_image.close()
            
        #raw_image.save()
    #full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'shovon.jpg')
    return render_template('searchResult.html', images=imgList)
    
    
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8000)