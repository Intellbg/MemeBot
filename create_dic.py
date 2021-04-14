from os import listdir
from os.path import isfile,join
#Path to files 
dic_path="dic.py"      #Dictionaty plain txt file
img_path="img/"         #Meme folder imagenes path 

file=open(dic_path,'w')    #Open plain text Dictionary File  
img_files = [f for f in listdir(img_path) if isfile(join(img_path, f))] #Gets all files in image files
img_files.sort()
#Writes a python dictionary, every image gets a entry
file.write("dic={\n")  
for i in img_files:
    name=i.split(".")
    file.write("'"+name[0].lower()+"':'"+img_path+i+"',\n")
file.write("}")
