import copy
#Grayscale image filter O(N^2) complexity
def grayscale(image_matrix):
  for row in range(len(image_matrix)):
    for column in range(len(image_matrix[0])):
      value=image_matrix[row][column]
      average=(value[0]+value[1]+value[2])//3
      image_matrix[row][column][0]=average
      image_matrix[row][column][1]=average
      image_matrix[row][column][2]=average
  return image_matrix


   
#Red stripes image filter 
def red_stripes(image_matrix):
    for row in range(len(image_matrix)):
      if row % 100 <50:
        for column in range(len(image_matrix[0])):
          image_matrix[row][column][0]=255.         # Maximize R
    return image_matrix


#Color inverter image filter O(N^2) complexity
def invert_colors(image_matrix):
  for row in range(len(image_matrix)):
    for column in range(len(image_matrix[0])):
      value=image_matrix[row][column]
      inverted_0=255-value[0]
      inverted_1=255-value[1]
      inverted_2=255-value[2]
      image_matrix[row][column][0]=inverted_0
      image_matrix[row][column][1]=inverted_1
      image_matrix[row][column][2]=inverted_2
  return image_matrix

#Flip image filter O(1) complexity
def flip(image_matrix):
  output_value=image_matrix[::-1]
  return output_value
  
#sepia image filter O(N^2) complexity
def sepia(image_matrix):
  for row in range(len(image_matrix)):
    for column in range(len(image_matrix[row])):
      value=image_matrix[row][column]
      sepia_0=(float(value[0]) * .393) + (float(value[1]) * .769) + (float(value[2]) * .189)
      sepia_1=(float(value[0]) * .349) + (float(value[1]) * .686) + (float(value[2]) * .168)
      sepia_2=(float(value[0]) * .272) + (float(value[1]) * .534) + (float(value[2]) * .131)
      image_matrix[row][column][0]=int(sepia_0)
      image_matrix[row][column][1]=int(sepia_1)
      image_matrix[row][column][2]=int(sepia_2)
      if image_matrix[row][column][0]>255:
        image_matrix[row][column][0]=255
      if image_matrix[row][column][1]>255:
        image_matrix[row][column][1]=255
      if image_matrix[row][column][2]>255:
        image_matrix[row][column][2]=255
  return image_matrix


