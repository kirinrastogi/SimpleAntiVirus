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
    for line in f.read().split(" "):
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
        f.write(md5 + " ")
    f.close()
    return

total = set()

try:
    # import from db
    f = open("\kirinrastogi\Dev\git-work\SimpleAntiVirus\Database\db.txt", "r")
    total = getSetOfHashes(f)
        
except Exception, e:
    warn(str(e))

try:
    # add pull from virusshare to total
    getPull('\kirinrastogi\Dev\git-work\SimpleAntiVirus\Update\url.txt')
except Exception, e:
    warn(str(e))

try:
    #write to file
    write("\kirinrastogi\Dev\git-work\SimpleAntiVirus\Database\db.txt")
except Exception, e:
    warn(str(e))
