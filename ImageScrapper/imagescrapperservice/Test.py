from bs4 import BeautifulSoup as bs
import os
import json
import urllib.request
import urllib.parse
import urllib.error
import ssl

def get_soup(url,header):
    req = urllib.request.Request(url, headers = header)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    html = bs(respData, 'html.parser')
    return html


query = input("query image")# you can change the query for the image  here
image_type=query
query= query.split()
query='+'.join(query)
url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
print (url)

        
#add the directory for your image here
DIR="Pictures"
header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
}
soup = get_soup(url,header)


ActualImages=[]# contains the link for Large original images, type of  image
for a in soup.find_all("div",{"class":"rg_meta"}):
    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
    ActualImages.append((link,Type))

print  ("there are total" , len(ActualImages),"images")

if not os.path.exists(DIR):
            os.mkdir(DIR)
DIR = os.path.join(DIR, query.split()[0])

if not os.path.exists(DIR):
            os.mkdir(DIR)
###print images
for i , (img , Type) in enumerate( ActualImages):
    try:
        ctx = ssl._create_unverified_context()
        req = urllib.request.Request(img, headers = header)
        respData = urllib.request.urlopen(req, context=ctx)
        raw_img = respData.read()

        cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
        print (cntr)
        if len(Type)==0:
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
        else :
            f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')


        f.write(raw_img)
        f.close()
    except Exception as e:
        print ("could not load : "+img)
        print (e)
#i hope this helps you

#share