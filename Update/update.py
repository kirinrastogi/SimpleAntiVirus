#get info from virusshare, store in txt file
import requests

def getPull(path):
    f = open(path, 'r')
    print(f.read())
    r = requests.get(f.read())
    for s in r.content.split('\n'):
        if not s.startsWith("#"):
            total.add(s)
    return

def getSetOfHashes(f):
    s = set()
    for line in f.read().split(" "):
        s.add(line)
    return s

def warn(s):
    f = open("log.log", "w")
    f.write("error occured: " + str(s) + " \n")
    f.close()
    return

def write(path):
    f = open(path, "w")
    for md5 in total:
        f.write(md5 + " ")
    f.close()
    return

total = set()

try:
    # import from db
    f = open("E:\kirinrastogi\Dev\git-work\SimpleAntiVirus\Database\db.txt", "r")
    total = getSetOfHashes(f)
        
except Exception, e:
    warn(str(e))

try:
    # add pull from virusshare to total
    getPull('E:\kirinrastogi\Dev\git-work\SimpleAntiVirus')
except Exception, e:
    warn(str(e))

try:
    #write to file
    write("E:\kirinrastogi\Dev\git-work\SimpleAntiVirus\Database\db.txt")
except Exception, e:
    warn(str(e))
