def convertFlag(matrix):
  matrix_gabungan = []
  for i in range(4):
    if i == 0:
      matrix_gabungan = matrix[0]
    else:
      matrix_gabungan += matrix[i]
    
  print(bytearray(matrix_gabungan))

matrix = [
  [99, 114, 121, 112],
  [116, 111, 123, 105],
  [110, 109, 97, 116],
  [114, 105, 120, 125],
]

print(convertFlag(matrix))