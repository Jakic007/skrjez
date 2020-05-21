import sys

if(len(sys.argv) != 3):
    print("Primjer pozivanja: python3 zadatak1.py '/zadaci-faq.html' TestPrimjeri/localhost_access_log.2008-02-24.txt")
    sys.exit(1)

try:
    with open(sys.argv[2], "r") as file:
        ipLog = {}
        lines= file.readlines()
        for line in lines:
            line = line.strip().split(".")
            ip = line[0]+"."+line[1]+".*.*"
            if ipLog.get(ip):
                ipLog[ip]=ipLog.get(ip)+1
            else:
                ipLog[ip]=1
except IOError: 
    print("File not readable")

ipLog={k: v for k, v in sorted(ipLog.items(), key=lambda item: item[1], reverse=True)}

print ("-------------------------------------------")
print ("Broj pristupa stranici: " + sys.argv[1])
print ("    IP podmreza : Broj pristupa")
print ("-------------------------------------------")
for ip, count in ipLog.items():
    if(count>2):
        print('{:>15} : {}'.format(ip, count))