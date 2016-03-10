#encoding:utf-8
#实现k均值算法
import sys
import os
import math
import random
import numpy as np
from numpy.random import rand
import matplotlib
import matplotlib.pyplot as plt
def readdata():   #读取数据
    fp=open(r"Data_new.txt")
    points=[]
    for lines in fp.readlines():
        lines = lines.replace("\n","")
        points.append(lines)
        fp.close()
    print points
    return points

def drawpicture(points,k,c): #选择绘制点的形状和颜色
    kind = ['x','+','o','s','^','v','<','>','*','d']
    colors = ['b', 'c', 'y', 'r', 'm']
    for point in points:
        point = point.split()
        plt.scatter(int(point[0]),int(point[1]),marker = kind[k], color = colors[c],s = 30)
        plt.title('Result of K_means')


def cacl_distxy(point1,point2): #计算两个点距离的平方'1 2','2 3'(x1-x2)^2+(y1-y2)^2
    sum = 0
    point1 = point1.split(' ')
    point2 = point2.split(' ')
    x_sub = float(point1[0])-float(point2[0])
    y_sub = float(point1[1])-float(point2[1])
    sum += x_sub*x_sub
    sum += y_sub*y_sub
    return sum

def cacl_sse(clusters,means): #计算所有簇集的sse,mean[i]='1 3',cluster = [['1 2','2 3'],['2 3','3 4']]
    sum_sse = 0
    k = len(means)
    for i in range(k):
        length = len(clusters[i])
        for j in range(length):
            sum_sse = sum_sse + cacl_distxy(clusters[i][j],means[i])
    return sum_sse

def decide_cluster(point,means):   #根据质心决定当前点属于哪个簇 point = '2 3',means[0] = '1 3'
    dist = cacl_distxy(point,means[0])
    temp = 0
    label = 0
    k = len(means)
    for i in range(1,k):
        temp = cacl_distxy(point,means[i])
        if temp<dist:
            dist = temp
            label = i
    return label

def get_means(cluster):   #得到当前簇的质心cluster = ['1 2','2 3']
    num_points = len(cluster)
    tempx = 0
    tempy = 0
    for i in range(num_points):
        cluster_lin = cluster[i].split(' ')
        tempx = tempx + float(cluster_lin[0])
        tempy = tempy + float(cluster_lin[1])
    tempx = round(tempx/num_points,2) #保留两位小数
    tempy = round(tempy/num_points,2)
    mean_temp = str(tempx)+' '+ str(tempy)
    return mean_temp

def k_means(points,k_num): #实现k均值算法，k_num为最终的簇个数points ['1 2','2 3']
    clusters = []
    means = []
    label_cluster = 0
    old_sse = 0
    points_num = len(points)
    for m in range(k_num):
        list = []
        clusters.append(list)
    for i in range(k_num):
        index = random.randint(0, points_num)
        means.append(points[index])

    for j in range(points_num):
        label_cluster = decide_cluster(points[j],means)
        #print label_cluster
        clusters[label_cluster].append(points[j])

    new_sse = cacl_sse(clusters,means)

    while (abs(new_sse-old_sse)>1):  #迭代的sse变化量
        for i in range(k_num):
            means[i] =  get_means(clusters[i])
        old_sse = new_sse
        new_sse = cacl_sse(clusters,means)

        clusters = [] #清空每个簇
        for m in range(k_num):
            list = []
            clusters.append(list)

        for j in range(points_num): #根据新的质心获得新的簇
            label_cluster = decide_cluster(points[j],means)
            clusters[label_cluster].append(points[j])
        #print '差为',abs(new_sse-old_sse)

    #print "sse的值为",new_sse
    #print clusters
    num_c = len(clusters)
    for i in range(num_c):
        drawpicture(clusters[i],i+1,i)#选择绘制点的形状和颜色
    plt.show()
if __name__ == "__main__" :
    points = []
    #cluster = ['1 2','2 3']
    clusters = []
    temp_point = []
    cluster_id = []
    points =  readdata()
    k_means(points,4)