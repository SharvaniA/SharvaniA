import cv2
import sys
fileName = sys.argv[1]
# image = cv2.imread('house.jpg')
# cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('exp4.jpg', cv2.cvtColor(cv2.imread(fileName), cv2.COLOR_BGR2GRAY))
# cv2.waitKey(0)
# cv2.destroyAllWindows()














# import cv2
# import sys
# fileName = sys.argv[0]
# cv2.imshow('Original', (image := cv2.imread('house.jpg')))
# cv2.imshow('Grayscale', cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
# cv2.imwrite('house1.jpg', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# sudo apt install python3-opencv
# python3 -c "import cv2; print(cv2.__version__)"











# Converting color image into Grayscale.

# import cv2
# cv2.imshow('Original', (image := cv2.imread('house.jpg')))
# cv2.imshow('Grayscale', cv2.cvtColor(image, cv2.COLOR_BGR2GRAY))
# cv2.waitKey(0)
# cv2.destroyAllWindows()