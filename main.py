import hikexp

class Args:
    def __init__(self, rhost, rport, reboot, noverify):
        self.rhost = rhost
        self.rport = rport
        self.reboot = reboot
        self.noverify = noverify

def isHikvision(line):
    if ("Hikvision" in line) or ("hikvision" in line) or (line == "Webs") or (line == "web") or ("RVi" in line):
        return True
    return False

res = open("results.txt","w")


with open(".txt", encoding="utf-8") as ips:
    try:
        for line in ips:
            rhost = line.split("\t")[0]
            rport = line.split("\t")[1]
            if (isHikvision(line.split("\t")[5])):
                cam = hikexp.Http(rhost, rport, "http")
                if hikexp.check(cam, Args(rhost, rport, False, False)):
                    res.write(rhost + ":" + rport + "\n")
    except:
        print("Err")
res.close()
