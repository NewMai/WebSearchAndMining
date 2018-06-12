
def RemoveIlegal(src, dst):
    data = set()
    with open(src, "r") as fr:
        while True:
            line = fr.readline()
            if not line:
                break
            if "http://www.17k.com/book/" not in line:
                continue
            if len(line) < 36:
                print "Illegal url : %s" % line
            temp = line[:-2]
            if not line in data:
                data.add(line)
    with open(dst, "w") as fw:
        for line in data:
            fw.write(line)


def Main():
    src = "url.txt"
    dst = "url_new.txt"
    RemoveIlegal(src, dst)

Main()


