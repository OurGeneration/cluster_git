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
def readdata():
    points = [[int(point.split(' ')[0]), int(point.split(' ')[1])] for point in open("Data_new.txt","r")]
    return points

def drawpicture(points,k,c): #选择绘制点的形状和颜色
    kind = ['x','+','o','s','^','v','<','>','*','d']
    colors = ['b', 'c', 'y', 'r', 'm']
    for point in points:
        #print point[0],point[1]
        plt.scatter(int(point[0]),int(point[1]),marker = kind[k], color = colors[c],s = 30)
        plt.title('Result of DB_scan')

def DB_scan(points):
    # 计算每个数据点相邻的数据点，邻域定义为以该点为中心以边长为2*EPs的网格
    Eps = 10
    adj_points = defaultdict(list)
    #print adj_points
    for index1,point1 in enumerate(points):
        for index2,point2 in enumerate(points):
            if (index1 < index2):
                if(abs(point1[0]-point2[0])<=Eps and abs(point1[1]-point2[1])<=Eps):
                    adj_points[index1].append(index2)
                    adj_points[index2].append(index1)
    print adj_points
    # 定义邻域内相邻的数据点的个数大于4的为核心点
    MinPts = 4
    core_points = [point_index for point_index,adj_point_index in adj_points.iteritems() if len(adj_point_index)>=MinPts]

    # 邻域内包含某个核心点的非核心点，定义为边界点
    Boundary_Pindex = []
    for point_index,adj_point_index in adj_points.iteritems():
        if (point_index not in core_points):
            for one_adj in adj_point_index:
                if one_adj in core_points:
                    Boundary_Pindex.append(point_index)
                    break

    # 噪音点既不是边界点也不是核心点
    noise_Pindex = [point_index for point_index in range(len(points)) if point_index not in core_points and point_index not in Boundary_Pindex]
    clusters = [index for index in range(len(points))]
    # 各个核心点与其邻域内的所有核心点放在同一个簇中
    for point_index,adj_Pindex in adj_points.iteritems():
        for adj_Pindex1 in adj_Pindex:
            if (point_index in core_points and adj_Pindex1 in core_points and point_index < adj_Pindex1):
                for index in range(len(clusters)):
                    if clusters[index] == clusters[adj_Pindex1]:
                        clusters[index] = clusters[point_index]

    # 边界点跟其邻域内的某个核心点放在同一个簇中
    for point_index,adj_Pindex in adj_points.iteritems():
        for adj_Pindex1 in adj_Pindex:
            if (point_index in Boundary_Pindex and adj_Pindex1 in core_points):
                clusters[point_index] = clusters[adj_Pindex1]
                break
    return clusters

# 打印规模最大的k个簇中的点
def printcluster(clusters,points,cluster_final):
    final_cluster = Counter(clusters).most_common(cluster_final)
    final_cluster = [onecount[0] for onecount in final_cluster]
    remain_Points = [points[index] for index in range(len(points)) if clusters[index] not in final_cluster]
    for i in range(cluster_final):
        cluster_i = [points[index] for index in range(len(points)) if clusters[index]==final_cluster[i]]
        print '规模最大的簇',i,cluster_i
        drawpicture(cluster_i,i,i)
    #打印剩余的点
    print "剩余的点",remain_Points
    drawpicture(remain_Points,cluster_final,cluster_final)
    plt.show()

if __name__ == "__main__" :
    clusters = []
    points = readdata()
    clusters = DB_scan(points)
    printcluster(clusters,points,4)