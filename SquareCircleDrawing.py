#!/bin/python3
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
            
    def squarePoint(square,point):
        corner=0
        area=0
        while corner<4:
            if inrange(point, square[corner%4], square[(corner+1)%4]):
                area += specialcase(point, square[corner%4], square[(corner+1)%4])
                corner+=1
            else:
                area += normalsolve(point, square[corner%4], square[(corner+1)%4])
                corner+=1
        
        return area  
                
        
        
        
    def normalsolve(point, c1, c2):
        recArea = getrectanglearea(point, c1, c2)
        t1 = getarea(c1, point)
        t2 = getarea(c2, point)
        t3 = getarea(c1, c2)
        totalarea = recArea - t1 - t2 - t3
        return abs(int(totalarea))
    
    def specialcase(point,c1,c2):
        t1 = getarea(c1,c2)
        t2 = getarea(c1,point)
        t3 = getarea(c2,point)
        area = t1-t2-t3
        rec1 = getarea([c1[0],c2[1]],point)
        rec2 = getarea([c2[0],c1[1]],point)
        if rec1 < rec2:
            area-=rec1*2
        else:
            area-=rec2*2
        return abs(area)
        
    def getarea(p1,p2):
        res = [0,0]
        res = pointsub(p1,p2)
        area = abs(res[0]*res[1])
        if area == 0:
            area = res[0]*res[0] 
            if area == 0:
                area = res[1]*res[1]
        return area/2
    
        
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
    
    def squareFill(square, boardset):
        row = 0
        point = 0
        area = int(getarea(square[0], square[2]))
        while row < boardset[1]:
            while point < boardset[0]:
                if int(squarePoint(square, [row * 4, point * 4])) == area:
                    index = row*w+point
                    print
                    markboard(boardset[2], index)
                point += 1
            point = 0
            row += 1
                
    
    # def correctsign(square, point):
    #     if point[0] > square[0][0] and point[0] > square[2][0]:
    #         point[0] = -point[0]
    #     if point[0] < square[0][0] and point[0] < square[2][0]:
    #         point[0] = -point[0]
    #     if point[1] > square[0][1] and point[1] > square[2][1]:
    #         point[1] = -point[1]
    #     if point[1] < square[0][1] and point[1] < square[2][1]:
    #         point[1] = -point[1]
    #     return point
    board = board_construct(w,h)
    boardset = [w,h,board]
    circleset = [circleX, circleY, r]
    circledraw(circleset, boardset)
    #display_board(boardset)
    c1 = [x1*4,y1*4]
    c2 = [0,0]
    c3 = [x3*4,y3*4]
    c4 = [0,0]
    center=[0,0]
    square=[c1,c2,c3,c4,center]
    getcorners(square)
    squareFill(square, boardset)
    display_board(boardset)
    for point in square:
        markboard(boardset,point)