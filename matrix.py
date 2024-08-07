#create matrix 
rows = int(input("Enter the number of rows"))
cols = int(input("Enter the number of cols"))

def create_matrix(r_value, c_value):
  """This function return a matrix of any size"""
  matrix = []
  for i in range(r_value):
    row = list(map(int,input(f"Enter {r_value} value for row {i+1} separated by space: ").split()))
    matrix.append(row)
  return matrix
print(create_matrix(rows,cols))  