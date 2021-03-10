import sys
import math
import cv2 as cv
import numpy as np
sumof = []

def main(argv):
    
    default_file = 'lines.jpg'
    filename = argv[0] if len(argv) > 0 else default_file
    # Loads an image
    src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_GRAYSCALE)
    # Check if image is loaded fine
    if src is None:
        print ('Error opening image!')
        print ('Usage: hough_lines.py [image_name -- default ' + default_file + '] \n')
        return -1

    dst = cv.Canny(src, 50, 200, None, 3)
    
    # Copy edges to the images that will display the results in BGR
    cdst = cv.cvtColor(dst, cv.COLOR_GRAY2BGR)
    gray = cv.GaussianBlur(cdst, (7, 7), 0)
    cdstP = np.copy(gray)
    
    lines = cv.HoughLines(dst, 1, np.pi / 180, 150, None, 0, 0)

    if lines is not None:
        for i in range(0, len(lines)):
            rho = lines[i][0][0]
            theta = lines[i][0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x0 = a * rho
            y0 = b * rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            pt1 = (x1, y1)
            pt2 = (x2, y2)
            cv.line(gray, pt1, pt2, (0,0,255), 3, cv.LINE_AA)
            #sumof.append(int(math.sqrt((x1-x2)**2 + (y1-y2)**2)))
            linesP = cv.HoughLinesP(dst, 1, np.pi / 180, 50, None, 50, 10)
    
    if linesP is not None:
        for i in range(0, len(linesP)):
            l = linesP[i][0]
            cv.line(cdstP, (l[0], l[1]), (l[2], l[3]), (0,0,255), 3, cv.LINE_AA)
            sumof.append(int(math.sqrt((l[0]-l[2])**2 + (l[1]-l[3])**2)))
    
    #cv.imshow("Source", src)
    #cv.imshow("Detected Lines (in red) - Standard Hough Line Transform", cdst)
    cv.imshow("Detected Lines (in red) - Probabilistic Line Transform", cdstP)
    cv.imwrite('detected_new.jpg', cdstP)
    #print(sumof)
    print(len(sumof))
    cv.waitKey()
    return 0

if __name__ == "__main__":
    main(sys.argv[1:])