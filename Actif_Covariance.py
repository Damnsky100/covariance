import numpy as np
import pandas as pd
import statistics


A =[22,24,21,27,34]
B =[24,21,20,7,26]

def average(lst):
    return sum(lst) / len(lst)

def pct(lst):
    pct_list = []
    for observation in range(len(lst)):
        if observation != 0 :
         pct_list.append((lst[observation]-lst[observation-1])/lst[observation-1])
    return pct_list


def matrix2(): #Matrice de rendement - moyenne de chaque asset
    mat = pd.DataFrame(data = {'assetA': A, 'assetB': B})
    temp2=[]
    mat2 = pd.DataFrame()
    for x in range(len(mat.columns)): #On veut énumérer le nombre d'asset qu'on a
        for asset in range(len(pct(mat.iloc[:, x]))):
            temp2.append(pct(mat.iloc[:, x])[asset] - average(pct(mat.iloc[:, x]))) # on isole notre asset
            
        mat2[mat.columns[x]]= temp2
        temp2 = []

    return mat2


def cov(): # we get the covariance between the two assets
        
    matrice_res = matrix2() #Verify our array
    matrice_inv = pd.DataFrame()


    for row in range(len(matrice_res.index)):
        matrice_inv[row] = matrice_res.iloc[row, :]

    return matrice_inv.dot(matrice_res)/len(matrice_res.index)


