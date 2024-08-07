#create matrix 
print("Enter Row and Col value for A")
rows_A = int(input("Enter the number of rows: "))
cols_A = int(input("Enter the number of cols: "))

print("Enter Row and Col value for B")
rows_B = int(input("Enter the number of rows: "))
cols_B = int(input("Enter the number of cols: "))

def create_matrix(r_value, c_value):
  """This function return a matrix of any size"""
  matrix = []
  for i in range(r_value):
    row = list(map(int,input(f"Enter {r_value} value for row {i+1} separated by space: ").split()))
    matrix.append(row)
  return matrix

#create 2 matrix
matrix_A = create_matrix(rows_A,cols_A)
print("------------Enter value in matrix B-----------")
matrix_B = create_matrix(rows_B,cols_B)


def matrix_multiply(matrix_A, matrix_B):
    """This function return result of multiplication of two matrix A and B"""
    col_A = len(matrix_A[0])
    row_A = len(matrix_A)
    col_B = len(matrix_B[0])
    row_B = len(matrix_B) 

    if col_A == row_B:
        result = [[0]*col_B for _ in range(row_A)]
    else:
        print("Warning! Multiplication not possible")

    
    for i in range(row_A):
        for j in range(col_B):
            for k in range(col_A):
                result[i][j] += matrix_A[i][k]*matrix_B[k][j]
                
    return result            

print(f"multiplication of two matrix is {matrix_multiply(matrix_A, matrix_B)}")



