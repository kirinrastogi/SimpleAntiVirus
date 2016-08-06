#get info from virusshare, store in txt file
import requests

def getPull(path):
    f = open(path, 'r')
    r = requests.get(f.read())
    f.close()
    for s in r.content.split("\n"):
        if not s.startswith("#"):
            total.add(s)
    return

def getSetOfHashes(f):
    s = set()
    for line in f.read().split("\n"):
        s.add(line)
    return s

def warn(s):
    f = open("log.log", "w")
    f.write("error occured: " + str(s) + " \n")
    f.close()
    print(str(s))
    return

def write(path):
    f = open(path, "w")
    for md5 in total:
        f.write(md5 + "\n")
    f.close()
    return

total = set()
try:
    db_path = ""
    path_file = open('db path.txt', 'r')
    db_path = path_file.read()
    path_file.close()
except Exception, e:
    warn("Database path is empty, or non existent.")

try:
    # import from db
    f = open(db_path, "r")
    total = getSetOfHashes(f)
        
except Exception, e:
    warn(str(e))

try:
    # add pull from virusshare to total
    getPull('url.txt')
except Exception, e:
    warn(str(e))

try:
    #write to file
    write(db_path)
except Exception, e:
    warn(str(e))
