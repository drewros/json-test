import json
path = "newfile.json"
try:
    f = open(path, "r")
    d = json.load(f)
    f.close()
except:
    d = {}
print (d)
newkey = input("Please write a new key ")
newval = input("Please write a new value ")
d[newkey] = newval

f = open(path, "w")
json.dump(d,f)
f.close()
