#encoding:utf-8
#实现层次聚类算法
import sys
import os
import math
import random
import numpy as np
from numpy.random import rand
import matplotlib
import matplotlib.pyplot as plt
from collections import defaultdict,Counter
def save_data(points):
    file = open('newdata.txt','w')
    for point in points:
        file.write(str(point[0])+' '+str(point[1])+'\n')
    file.close()

def drawpicture(points,k,c): #选择绘制点的形状和颜色
    kind = ['x','+','o','s','^','v','<','>','*','d']
    colors = ['b', 'c', 'y', 'r', 'm']
    for point in points:
        #print point[0],point[1]
        plt.scatter(int(point[0]),int(point[1]),marker = kind[k], color = colors[c],s = 30)
        plt.title('Result of DB_scan')
    plt.show()
def Rand_points(): #生成100*100的整数点 100个
    points = []
    for area1 in range(25):
        pointx = random.randint(10, 60)
        pointy = random.randint(10, 40)
        points.append([pointx,pointy])
    for area1 in range(35):
        pointx = random.randint(10, 60)
        pointy = random.randint(70, 120)
        points.append([pointx,pointy])
    for area1 in range(15):
        pointx = random.randint(80, 120)
        pointy = random.randint(10, 40)
        points.append([pointx,pointy])
    for area1 in range(25):
        pointx = random.randint(70, 120)
        pointy = random.randint(55, 120)
        points.append([pointx,pointy])
    print points,len(points)
    return points
if __name__ == "__main__" :
    points = []
    points = Rand_points()
    drawpicture(points,0,0)
    save_data(points)