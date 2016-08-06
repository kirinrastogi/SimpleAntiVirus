#get info from virusshare, store in txt file
import requests

total = set()

try:
    # import from db
    f = open("db.txt", "r")
    total = getSetOfHashes(f)
        
except Exception, e:
    warn(str(e))

try:
    # add pull from virusshare to total
    getPull('https://virusshare.com/hashes/VirusShare_00264.md5')
except Exception, e:
    warn(str(e))

try:
    #write to file
    write("E:\kirinrastogi\Dev\git-work\SimpleAntiVirus\Database\db.txt")
except Exception, e:
    warn(str(e))

def getPull(url):
    r = requests.get(url)
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
