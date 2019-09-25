import hashlib

def miner(key):
    out = ''
    count = 0
    while out != "000000":
        out = hashlib.md5(f"{key}{count}".encode('utf-8')).hexdigest()
        out = out[0:6]
        count+=1
    return count-1


print(miner("bgvyzdsv"))