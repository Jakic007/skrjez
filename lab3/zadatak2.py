import sys

def hd(arguments, cnt):
    for x in range(0, 100, 10):
        if(x==0):
            print("Hyp#Q10#Q20#Q30#Q40#Q50#Q60#Q70#Q80#Q90")
            print(format(cnt, '03d'), end=("#"))
        elif(x!=90):
            print(arguments[x], end="#")
        else:
            print(arguments[x])
    print()

if(len(sys.argv) != 2):
    print("Invalid nuber of arguments provided")
    sys.exit(1)

try:
    with open(sys.argv[1], "r") as file:
        cnt=0
        lines= file.readlines()
        for line in lines:
            line = line.strip().split(" ")
            line.sort()
            cnt+=1
            hd(line, cnt)
except IOError: 
    print("File not readable")

