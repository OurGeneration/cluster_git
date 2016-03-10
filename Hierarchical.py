#encoding:utf-8
#实现层次聚类（Hierarchical）算法
import sys
import os
import math
import random
import numpy as np
from numpy.random import rand
import matplotlib
import matplotlib.pyplot as plt
from operator import itemgetter
from collections import OrderedDict,Counter
def drawpicture(points,k,c): #选择绘制点的形状和颜色
    kind = ['x','^','o','s','v','+','<','>','*','d']
    colors = ['b','g','c', 'y', 'r', 'm','b','g','c']
    for point in points:
        plt.scatter(point[0],point[1],marker = kind[k], color = colors[c],s = 40)
        plt.title('Result of Hierarchical')

def readdata():
    points = [[int(point.split(' ')[0]), int(point.split(' ')[1])] for point in open("Data_new.txt","r")]
    return points
def Hierarchical(points):
# 初始时每个点为一个簇
    clusters = [index for index in range(len(points))]
    Dic_dist = {}
    for index1,point1 in enumerate(points):
        for index2,point2 in enumerate(points):
            if (index1 < index2):
                # 计算点对之间的距离
                distance = pow(abs(point1[0]-point2[0]),2) + pow(abs(point1[1]-point2[1]),2)
                Dic_dist[str(index1)+"&"+str(index2)] = distance
    # 按距离降序将各个点对排序
    print Dic_dist
    Dic_dist = OrderedDict(sorted(Dic_dist.iteritems(), key=itemgetter(1), reverse=True))
    Cluster_num = len(clusters)
    #当簇数变为所有点的10%时，停止
    remain_num = int(Cluster_num*0.1)

    while Cluster_num > remain_num:
        # 选取下一个距离最近的点对
        pointAB,distance = Dic_dist.popitem()
    
        pointA = int(pointAB.split('&')[0])
        pointB = int(pointAB.split('&')[1])
        Cluster_A = clusters[pointA]
        Cluster_B = clusters[pointB]

        # 当前距离最近两点若不在同一簇中，将点B所在的簇中的所有点合并到点A所在的簇中，此时当前簇数减1
        if(Cluster_A != Cluster_B):
            for index in range(len(clusters)):
                if clusters[index] == Cluster_B:
                    clusters[index] = Cluster_A
            Cluster_num -= 1
    return clusters

 # 选取规模最大的k个簇进行打印
def printcluster(clusters,points,cluster_final):
    final_cluster = Counter(clusters).most_common(cluster_final)
    final_cluster = [onecount[0] for onecount in final_cluster]
    remain_Points = [points[index] for index in range(len(points)) if clusters[index] not in final_cluster]
    # 打印规模最大的k个簇中的点
    for i in range(cluster_final):
        cluster_i = [points[index] for index in xrange(len(points)) if clusters[index]==final_cluster[i]]
        drawpicture(cluster_i,i,i)
    drawpicture(remain_Points,cluster_final,cluster_final)
    plt.show()

if __name__=="__main__":
    points = []
    clusters = []
    points = readdata()
    clusters = Hierarchical(points)
    printcluster(clusters,points,4)