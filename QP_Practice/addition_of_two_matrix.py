def addTwoMatrix(matrix1,matrix2) :

    result = []
    n = len(matrix1)
    print("len :",n)
    for i in range(n) :
        addition = [] 
        for j in range(n) :
            addition.append(matrix1[i][j] + matrix2[i][j])
        result.append(addition)
        
    return result
def main():
    size = int(input("Enter size of matrices: "))
    
    matrix1 = []
    print("Enter the elements of the first matrix:")
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(int(input()))
        matrix1.append(row)
        
    matrix2 = []
    print("Enter the elements of the second matrix:")
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(int(input()))
        matrix2.append(row)
    
    result = addTwoMatrix(matrix1, matrix2)
    print("Addition of two matrices:")
    for row in result:
        print(*row)

main()
