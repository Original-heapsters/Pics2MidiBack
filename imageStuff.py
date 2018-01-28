import numpy as np
import cv2
import json
from terminalplot import plot
import matplotlib as mpl
mpl.use('TkAgg')
from matplotlib import pyplot as plt

class imageStuff:
    # None can be any data type
    # {} dictionary
    def __init__(self, path=None, averageRange={}, dominantColor=None):
        self.path = path
        self.averageRange = averageRange
        self.dominantColor = dominantColor
        # self.getPoints = getPoints
        print("initialized")

    def showImage(self, name):
        print(__name__)
        # prevents method from running server side aka app.py
        if __name__ == "__main__":
            img = cv2.imread(self.path)
            cv2.imshow(name,img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return

    def averageColors(self):
        averageRange = {} #{} is dictionary
        averageRange["max"] = (255,132,56) #tuple
        averageRange["min"] = (0,10,50)
        # tuple RGB = 1,2,3
        self.averageRange = averageRange

    def dominantColor(self):
        #self.dominantColor = (0,0,0) #tuple
        return

    # convert img from RGB to GRAY with cv2 operation
    def convertToGrayScale(self):
        img = cv2.imread(self.path) # read file and save it in a variable called img
        img = cv2.cvtColor (img, cv2.COLOR_RGB2GRAY) # img contains a grayscale image
        cv2.imwrite ("gray.png", img) # write to new image called gray.png
        return

    # convert grayscale to outlines - lots of tuts to do that.
    def convertToOutlines(self):
        img = cv2.imread(self.path)
        edges = cv2.Canny(img,10,200)

        # plt.subplot(121),plt.imshow(img,cmap = 'gray')
        # plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        # plt.subplot(122),plt.imshow(edges,cmap = 'gray')
        # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

        # cv2.imshow(edges,cmap = 'gray')
        cv2.imwrite ("edges.png", edges)
        return

    # getpoints changes image, finds contours from image, adds contours to a list of x y values, plots x y values as coordinates, prints & returns list of contours as x,y coordinates
    # pass these points to midi
    def getPoints(self):
        img = cv2.imread(self.path)
        gray = cv2.cvtColor (img, cv2.COLOR_RGB2GRAY) # img contains a grayscale image
        edges = cv2.Canny(gray,100,150)

        # find contours in the edged image, keep only the largest ones, and initialize our screen contour
        #findContours(copy of img,compute hierarchy between contours, compress contours)
        img2, contours, hierarchy = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # contours is a Python list of all the contours in the image.
        # Each individual contour is a Numpy array of (x,y) coordinates of boundary points of the object.
        contours = np.vstack(contours).squeeze()
        # plt.plot(contours)
        # plt.show()
        xValues = []
        yValues = []
        points = []

        coords = list(contours) #contours is made to list
        for x,y in coords:
            xValues.append(x)
            yValues.append(-y)
            points.append((x,-y))

        plot(xValues, yValues)
        print(points)
        return points

if __name__ == "__main__":
    pathToImage = "shrek2.jpg"
    imgStuff = imageStuff(path=pathToImage)
    imgStuff.showImage(name="original")

    # imgStuff.averageColors()
    # imgStuff.dominantColor()

    imgStuff.convertToGrayScale()
    # imgStuff.showImage(name="grayscale")

    imgStuff.convertToOutlines()
    # imgStuff.showImage(name="outline")

    myPoints = imgStuff.getPoints()
    averageColors = imgStuff.averageRange
    dominantColor = imgStuff.dominantColor

    dictOfValues = {}
    dictOfValues["midiPoints"] = myPoints
    # dictOfValues["averageColors"] = averageColors
    # dictOfValues["dominantColor"] = dominantColor

    print (json.dumps(dictOfValues, indent=4))

