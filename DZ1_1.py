import numpy as np

import math

from cv2 import cv2


N = 9

image = cv2.imread('Image.jpg')

height = image.shape[0]
width = image.shape[1]

divided_height = math.floor(height/3)
divided_width = math.floor(width/3)


start_height_offset = 0
start_width_offset = 0
end_height_offset = divided_height
end_width_offset = divided_width

for i in range(0, 9):

    if end_width_offset + divided_width > width:
        end_width_offset += width - 3 * divided_width

    elif end_height_offset + divided_height > height:
        end_height_offset += height - 3 * divided_height

    cv2.imwrite(f'{i}.jpg', image[start_height_offset:end_height_offset, start_width_offset:end_width_offset])
    
    start_width_offset = end_width_offset

    end_width_offset += divided_width

    if end_width_offset > width:
        start_width_offset = 0
        end_width_offset = divided_width

        start_height_offset = end_height_offset
        end_height_offset += divided_height
