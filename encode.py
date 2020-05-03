# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 20:32:53 2020

@author: Aya Samir Abohadima
"""
# to find index of array
def findindex(array1,element):
    for i in range(0,len(array1)):
        if(array1[i]==element):
            return i
    return -1

# to encode 
def calArithmaticCode(currentcolor,sequance,blockSize,flattenarray):
    index=0
    codes=[]
    for j in range (0,flattenarray.size//blockSize):
        fcurrent=0
        lcurrent=sequance[len(sequance)-1]
        for i in range(0,blockSize):
            frist=fcurrent
            fcurrent=(lcurrent-fcurrent)*sequance[findindex(currentcolor,flattenarray[index])]+fcurrent
           
            lcurrent=(lcurrent-frist)*sequance[findindex(currentcolor,flattenarray[index])+1]+frist
           
            index=index+1
            
        codes.insert(j,fcurrent)
    return codes
#imports
from pathlib import Path
import numpy as np
import cv2 as cv
#inputs
typeofFloat= input("Please enter a float type:\n")
image = input("Please enter a image file name :\n")
blockSize=int(input("Please enter a block size number:\n"))
#checks typeofFloat !='float32' and typeofFloat != 'float64' and  typeofFloat != 'float16' 
if ((typeofFloat =='float32' or typeofFloat == 'float64' or  typeofFloat == 'float16') and blockSize>0  and Path(image).is_file()):
    img=cv.imread(image)
    grayImage=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    
    print (grayImage.shape)
    
    flattenArray=grayImage.flatten()
     
    if(flattenArray.size%blockSize!=0):
        for i in range(flattenArray.size,flattenArray.size+blockSize-flattenArray.size%blockSize):
            flattenArray=np.insert(flattenArray,i,0)
    
    probability=[]
    eleminateprobability=[]
    currentColor=[]
    sequance=[]
    for i in range(0,256):
        probability.insert(i,0)
    
    for i in range(0,flattenArray.size):
        probability[flattenArray[i]]= probability[flattenArray[i]]+1.0/flattenArray.size
    j=0
    for i in range(0,256):
        if(probability[i]!= 0):
            eleminateprobability.insert(j,probability[i])
            currentColor.insert(j,i)
            j=j+1
    sequance.insert(0,0)
    for i in range(1,j+1):
        sequance.insert(i,sequance[i-1]+eleminateprobability[i-1])
    codes=calArithmaticCode(currentColor,sequance,blockSize,flattenArray)
    outCode=np.array(codes,dtype=typeofFloat)
    np.save("codes",outCode)
    np.save("prob",probability)  
    print("codes in file codes.npy in  and probability in file prob1.npy the same code folder save the name to enter when decode .")  
else:
    print("you enter not invalid input ,please try again with valid ")        
    
