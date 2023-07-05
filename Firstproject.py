def grayscale(image_matrix):
  for row in range(len(image_matrix)):
    for column in range(len(image_matrix[0])):
      value=image_matrix[row][column]
      average=(value[0]+value[1]+value[2])//3
      image_matrix[row][column][0]=average
      image_matrix[row][column][1]=average
      image_matrix[row][column][2]=average
  return image_matrix


   

def red_stripes(image_matrix):
    for row in range(len(image_matrix)):
      if row % 100 <50:
        for column in range(len(image_matrix[0])):
          image_matrix[row][column][0]=255.         # Maximize R
    return image_matrix


