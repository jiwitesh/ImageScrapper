# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 06:38:44 2019

@author: Jiwitesh_Sharma
"""
from pymongo import MongoClient
import gridfs
from PIL import Image


def insert_image(raw_image, keyWord):
    
    db = MongoClient()
    db = db["ImagesDB"]
    fs = gridfs.GridFS(db)
    count = 1
    for image in raw_image:
        fs.put(image, filename=keyWord+"_"+str(count)) 
        count +=1
        #fileid_List.append(fs.put(raw_image))
    
    #collections.insert_one({"imagefile":keyWord,"fileid":fileid_List})
   
    '''client = MongoClient()
    db = client['imageData']
    collections = db.images
    result = collections.insert_one(data)
    #return result;
    with open(request.GET["image_name"], "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    print (encoded_string)
    abc=db.database_name.insert({"image":encoded_string})
    return HttpResponse("inserted")'''

def retrieve_image(keyWord):
    #keyWord = "jiwitesh"
    db = MongoClient()
    db = db["ImagesDB"]
    fs = gridfs.GridFS(db)
    imageList = {}
    for i in range(500):
        i = i+1
        filename = keyWord+"_"+str(i)
        try:
            if not fs.exists({"filename": filename}):
                print("mongo file does not exist! {0}".format(filename))
                #raise Exception("mongo file does not exist! {0}".format(filename))
            else:
                im_stream = fs.find_one({'filename':filename})
                #imageList[filename] = Image.open(im_stream)
                imageList[filename] = im_stream
        except:
             print("mongo file does not exist! {0}".format(filename))
    return imageList
    #query = { "imaegType": { "$regex": "test"} }
    #imagesArray = fs.find(query); 
    #imageBytes = fs.get({},{ "_id": 0, "data": 1 })
    '''im_stream = fs.get("testImage0")
    im = Image.open(im_stream)
    return imagesArray'''

         
    #most_recent_three = fs.find().sort("uploadDate", -1).limit(3)
    #print(most_recent_three.cursor_id)
    '''for grid_out in fs.get():
    data = grid_out
    Image.open(data).save(data+".jpg", '.png')'''
    #PL(data)
    #print(data)
    '''for grid_out in fs.find({"filename": "lisa.txt"},no_cursor_timeout=True):
    data = grid_out.read()
    print(data)'''
   