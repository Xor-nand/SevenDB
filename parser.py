import re

def linesof(file):
    f = open(file, "r")
    listline = f.readlines()
    f.close()
    return listline

def write(a):
    print(a)

def check(str, pattern):
    # _matching the strings
    if re.search(pattern, str):
        listofprods.append(str)
    else:
        trash.append(str)

def sprit(prodline):
    prod = prodline.strip().split('  ')
    res = []
    for ele in prod:
        if ele.strip():
            res.append(ele.strip())
    return(res)

file = "outputmail.txt"
listline = linesof(file)
listofprods = []
trash = []
box = []

pattern = re.compile('\d[.]\d+\s')

for i in listline:
     check('{}'.format(i), pattern)

for prod in listofprods:
    box.append(sprit(prod))

boxx = box.pop(0)

for item in box:
    print ("OGGETTO: {}, PREZZO: {}, QT: {}".format(item[0],item[3],item[2]))
