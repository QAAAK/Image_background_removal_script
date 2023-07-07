import cv2

from rembg import remove

input_path_image = input('Enter Image address: ')
output_path_image = input('Enter Image address to save: ')

input = cv2.imread(input_path_image)
output = remove(input)

cv2.imwrite(output_path_image,output)