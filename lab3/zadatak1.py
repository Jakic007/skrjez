import sys

def parse_matrix(matrixRaw):
    matrix={}
    matrix['rows'], matrix['columns'] = [int(x) for x in matrixRaw[0].split(' ')]
    for line in matrixRaw[1:]:
        values = [float(x) for x in line.split(' ')]
        if not len(values) == 3:
            print("Matrica nije valjana")
            sys.exit(1)
        row=int(values[0])
        column=int(values[1])
        value=values[2]
        matrix[(row, column)] = value
    return matrix

def multiply(matrix1, matrix2):
    check(matrix1, matrix2)

    product={}
    product['rows']=matrix1['columns']
    product['columns']=matrix2['rows']

    for i in range(1, matrix1['columns'] + 1):
        for j in range(1, matrix2['rows'] +1):
            sum=.0
            for k in range(1, matrix1['columns'] + 1):
                if not (i, k) in matrix1:
                    val1=0
                else:
                    val1=matrix1[(i,k)]
                if not (k, j) in matrix2:
                    val2=0
                else:
                    val2=matrix2[(k,j)]
            sum += val1 * val2
            product[(i,j)]=sum
    return product

def check(matrix1, matrix2):
    if(matrix1['columns'] != matrix2['rows']):
        print("Matrice nisu množive")
        sys.exit(2)

with open(sys.argv[1], "r") as file:
    array1 = []
    array2 = []
    lines= file.readlines()
    flag=0
    i=0
    for line in lines:
        if len(line.strip()) == 0 :
            flag=1
            i=0
            continue
        if(flag==0):
            array1.append(line.strip())
            i+=1
        else:
            array2.append(line.strip())
            i+=1
    matrix1=parse_matrix(array1)
    matrix2=parse_matrix(array2)

product=multiply(matrix1, matrix2)

print(product)

with open(sys.argv[2], "w") as file:
    print("{0} {1}".format(product['rows'], product['columns']), file = file)
    print("{0} {1}".format(product['rows'], product['columns']))

    for i in range(1, product['columns'] + 1):
        for j in range(1, product['rows'] + 1):
            if((i, j) in product):
                print("{0} {1} {2}".format(i, j, product[(i,j)]), file = file)
                print("{0} {1} {2}".format(i, j, product[(i,j)]))
            else:
                print("{0} {1} {2}".format(i, j, 0))