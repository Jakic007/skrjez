import os, sys

def loadStudents(file):
    try:
        with open(file, "r") as f:
            lines= f.readlines()
            for line in lines:
                student=line.strip().split(" ")
                #log[student[0]]=[student[1], student[2]]
                log[student[0]]={
                    "Prezime": student[1],
                    "Ime": student[2]
                }
    except IOError: 
        print("File not readable")

def loadResults(file):
    try:
        with open(path+file, "r") as f:
            labNum=int(file.split("_")[0][3:])
            lines= f.readlines()
            for line in lines:
                student=line.strip().split(" ")
                if labNum in log[student[0]]:
                    print("Student appeared in two groups of the same exercise")
                    sys.exit(1)
                log[student[0]][labNum]=student[1]            
    except IOError:
        print("File not readable")

if(len(sys.argv) != 2):
    print("Invalid nuber of arguments provided")
    sys.exit(1)

path = sys.argv[1]
dirs=os.listdir(path)

log={}

loadStudents(path + "studenti.txt")

for file in dirs:
    if(file == "studenti.txt"):
        continue
    loadResults(file)

for student in log:
    nameFormat=log[student]["Prezime"]+", "+log[student]["Ime"]
    print("JMBAG      Prezime, Ime                   ", end="")
    for i in range(len(log[student]) - 2):
        print('L{}'.format(i+1), end="  ")
    print()
    
    print('{} {:30} '.format(student, nameFormat), end="")
    for i in range(len(log[student]) - 2):
        print('{}'.format(log[student][i+1]), end=" ")
    print()