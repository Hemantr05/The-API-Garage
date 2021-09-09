import cv2
import pytesseract
from pytesseract import Output

img = cv2.imread('imgs/demo.png')
d = pytesseract.image_to_data(img, lang='deu', output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
	(x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
	img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imwrite('imgs/demo_result2.png', img)

