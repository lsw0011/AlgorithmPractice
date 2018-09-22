#link to problem https://www.hackerrank.com/contests/w29/challenges/a-circle-and-a-square
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    wh = input().split()
    w = int(wh[0])
    h = int(wh[1])

    circleXCircleY = input().split()
    circleX = int(circleXCircleY[0])
    circleY = int(circleXCircleY[1])
    r = int(circleXCircleY[2])

    x1Y1X3Y3 = input().split()

    x1 = int(x1Y1X3Y3[0])
    y1 = int(x1Y1X3Y3[1])

    x3 = int(x1Y1X3Y3[2])
    y3 = int(x1Y1X3Y3[3])

    def board_construct(w,h):
        board = ['.']*w*h;
        return board
    
    def display_board(boardset):   #boardset = [w,h,board]
        row = 0
        while row < boardset[1]:
            start = boardset[0] * row
            print(''.join(board[start:start+boardset[0]]))
            row+=1
        return 
    
    def circledraw(circleset, boardset): #circle = [circleX,circleY,radius] boardset = [w,h,board]
        center = circleset[0:2]
        r = circleset[2]
        for y in range(boardset[1]):
            for x in range(boardset[0]):
                xleg = x - center[0]
                yleg = y - center[1]
                if xleg*xleg+yleg*yleg <= r*r:
                    index = y*w +x
                    markboard(boardset,[x,y])
                    
    def markboard(boardset, point):
        index = boardset[0] * point[1] + point[0]
        boardset[2][index] = '#'
        
    def getcorners(square):
        midslope = pointsub(square[0],square[2])
        midslope = pointhalf(midslope)
        square[4] = pointadd(square[0],midslope)
        square[1] = [(square[4][0]-midslope[1]),(square[4][1]+midslope[0])]
        square[3] = [(square[4][0]+midslope[1]),(square[4][1]-midslope[0])]
        

    def inrange(point, corner1, corner2):
        x = False
        y = False
        if corner1[0] < point[0] and point[0] < corner2[0]:
            x = True
        if corner1[0] > point[0] and point[0] > corner2[0]:
            x = True
        if corner1[1] < point[1] and point[1] < corner2[1]:
            y = True
        if corner1[1] > point[1] and point[1] > corner2[1]:
            y = True
        if x == True and y == True:
            return True
        else:
            return False
            
    def checkArea(square,point):
        center = square[4]
        corner=0
        area=0
        while corner<4:
            c1 = square[corner%4]
            c2 = square[(corner+1)%4]
            if specialcasecheck(c1, c2, point):
                rectangle = getspecialrectangle(c1,c2)
                cpoint = centerpoint(rectangle, square)
                area += specialarea(c1, c2, point, cpoint)
            else:
                area += normalsolve(point, c1, c2)
            corner+=1
        return area  
                
    def squaretriangle(c1,c2):
        dimensions = pointsub(c1, c2)
        area = abs(int(dimensions[0]*dimensions[1]/2))
        if area == 0:
            area = dimensions[0]*dimensions[0]+dimensions[1]*dimensions[1]//2
        return abs(int(dimensions[0]*dimensions[1]/2))
        
    def normalsolve(point, c1, c2):
        rec = getrectanglecorners(point, c1, c2)
        r1 = getrectangle(rec[0],rec[2])
        t1 = gettriangle(c1, point)
        t2 = gettriangle(c2, point)
        t3 = squaretriangle(c1, c2)
        totalarea = r1 - t1 - t2 - t3
        return abs(int(totalarea))
    
    def getsquare(c1, c3):
        d = pointsub(c1, c3)
        a = (d[0]*d[0]+d[1]*d[1])/2
        return a
        
        
        
    
    def getrectanglecorners(point, c1, c2):
        xValues = [point[0], c1[0], c2[0]]
        yValues = [point[1], c1[1], c2[1]]
        maxmax = [max(xValues), max(yValues)]
        minmin = [min(xValues), min(yValues)]
        maxmin = [maxmax[0], minmin[1]]
        minmax = [minmin[0], maxmax[1]]
        rectangle = [maxmax, maxmin, minmin, minmax]
        return rectangle
    
    def getspecialrectangle(c1,c2):
        xValues = [c1[0], c2[0]]
        yValues = [c1[1], c2[1]]
        maxmax = [max(xValues), max(yValues)]
        minmin = [min(xValues), min(yValues)]
        maxmin = [maxmax[0], minmin[1]]
        minmax = [minmin[0], maxmax[1]]
        rectangle = [maxmax, maxmin, minmin, minmax]
        return rectangle

    def specialcasecheck(c1, c2, point): #checks to see if a corner of the rectangle falls on the center
        rectangle = getspecialrectangle(c1, c2)
        maxmax = rectangle[0]
        minmin = rectangle[2]
        if minmin[0] <= point[0] and point[0] <= maxmax[0]:
            if minmin[1] <= point[1] and point[1] <= maxmax[1]:
                return True
        return False
    
    def centerpoint(rectangle, square):
        center = square[4]
        flag = True
        curindex = 0
        index = 0
        for point in rectangle:
            dimensions = pointsub(point, center)
            dist = dimensions[0]*dimensions[0]+dimensions[1]*dimensions[1]
            if flag:
                minimum = dist
                flag = False
            elif minimum > dist:
                minimum = dist
                index = curindex
            curindex += 1
        return rectangle[index]
        
            
    def specialarea(c1, c2, point, centerpoint):
        t1 = gettriangle(c1, point)
        t2 = gettriangle(c2, point)
        r1 = getrectangle(point, centerpoint)
        t3 = squaretriangle(c1, c2)
        area = t3-t1-t2-r1
        return abs(area)
        
    
    def gettriangle(corner, point):
        dimensions = pointsub(corner, point)
        return abs(int(dimensions[0]*dimensions[1]/2))
    
    def getrectangle(corner, point):
        dimensions = pointsub(corner, point)
        return abs(int(dimensions[0]*dimensions[1]))
            
        
    def getrectanglearea(point, c1, c2):
        xValues = [point[0], c1[0], c2[0]]
        yValues = [point[1], c1[1], c2[1]]
        maxVals = [max(xValues), max(yValues)]
        minVals = [min(xValues), min(yValues)]
        dimensions = pointsub(maxVals, minVals)
        area = dimensions[0] * dimensions[1]
        return abs(area)
    
    def pointsub(p1,p2):
        res = [0,0]
        res[0] = p2[0]-p1[0]
        res[1] = p2[1]-p1[1]
        return res
    
    def pointadd(p1,p2):
        res = [0,0]
        res[0] = p2[0]+p1[0]
        res[1] = p2[1]+p1[1]
        return res
    
    def pointhalf(p1):
        p1[0]=p1[0]//2
        p1[1]=p1[1]//2
        return p1
    def getmaxs(points):
        xvals = [points[0][0], points[1][0], points[2][0], points[3][0]]
        yvals = [points[0][1], points[1][1], points[2][1], points[3][1]]
        return [max(xvals)//4, max(yvals)//4]
    def getmins(points):
        xvals = [points[0][0], points[1][0], points[2][0], points[3][0]]
        yvals = [points[0][1], points[1][1], points[2][1], points[3][1]]
        return [min(xvals)//4, min(yvals)//4]
    
    def squarefill(square, boardset, squarearea):
        width = boardset[0]
        height = boardset[1]
        row = 0
        maxvals = getmaxs(square)
        minvals = getmins(square)
        while row < height:
            if row < minvals[1]:
                row+=1
                continue
            if row > maxvals[1]:
                break
            column = 0
            while column < width:
                if column < minvals[0]:
                    column+=1
                    continue
                if column > maxvals[0]:
                    break
                point = [column*4, row*4]
                area = checkArea(square, point)
                if area == squarearea:
                    markboard(boardset, [column, row])
                column += 1
            row += 1
            
        

                
    board = board_construct(w,h)
    boardset = [w,h,board]
    circleset = [circleX, circleY, r]
    circledraw(circleset, boardset)
    c1 = [x1*4,y1*4]
    c2 = [0,0]
    c3 = [x3*4,y3*4]
    c4 = [0,0]
    center=[0,0]
    square=[c1,c2,c3,c4,center]
    getcorners(square)
    squarearea = getsquare(square[0],square[2])
    squarefill(square, boardset, squarearea)
    display_board(boardset)