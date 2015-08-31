import numpy as np
import cv2

def getSubPixelBoundary(img):
	subPixel = np.zeros(shape=(img.shape[0]*2-1,img.shape[1]*2-1))
	for (x,y),value in np.ndenumerate(subPixel):
		if (x%2==1 and y%2==0) and (img[(x+1)/2][y/2] != img[(x-1)/2][y/2] ):
			subPixel[x][y]=1
		elif (x%2==0 and y%2==1) and (img[x/2][(y+1)/2] != img[x/2][(y-1)/2] ):
			subPixel[x][y]=1
		elif x%2==1 and y%2==1:
			subPixel[x][y] = img[x/2][y/2]
	fillGaps(subPixel)
	return subPixel

def fillGaps(subPixel):
	for x in range(0,subPixel.shape[0]-2,2):
		for y in range(0,subPixel.shape[1]-2,2):
			if subPixel[x+1][y] == 1 and subPixel[x-1][y] == 1 or subPixel[x][y+1] == 1 and subPixel[x][y-1] == 1:
		   		subPixel[x][y]=1
	return subPixel

def getJunctionPoints(subPixel):
	junc = np.zeros(shape=subPixel.shape)
	for x in range(0,subPixel.shape[0]-2,2):
		for y in range(0,subPixel.shape[1]-2,2):
			if subPixel[x+1][y]+subPixel[x-1][y]+subPixel[x][y-1]+subPixel[x][y+1] > 2:
				junc[x][y]=1
	return junc

#ExtractBoundaryPieces
	

imgPath = 'pikachu.jpg'
img = cv2.imread(imgPath, cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (0,0), fx=0.1, fy=0.1)
sub = getSubPixelBoundary(img)
junc = getJunctionPoints(sub)
cv2.imshow('sub',sub)
cv2.imshow('junc',junc)
cv2.waitKey(0)
cv2.destroyAllWindows()