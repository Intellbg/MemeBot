file=open("dic.txt",'w')
file.write("dic={ \n")
from os import listdir
from os.path import isfile,join
onlyfiles = [f for f in listdir('img/') if isfile(join('img/', f))]

for i in onlyfiles:
    file.write("'"+i[:-4]+"':'img/"+i+"',\n")
file.write("}")
