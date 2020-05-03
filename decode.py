# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 21:52:22 2020
269,229
@author:Aya Samir Abohadima
"""
def serchHigh(array1,element):
    for i in range(0,len(array1)):
        if(element<array1[i]):
            return i
    return -1
def decodeArithmatic(seq,currenrcolor,block,codes):
    index=0
    flattenImg=np.array([])
    for i in range(0,codes.size):
        code=codes[i]
        
        for j in range(0,block):
            highcode=serchHigh(seq,code)
            
            flattenImg=np.insert(flattenImg,index,currenrcolor[highcode-1])
            code=(code-seq[highcode-1])/(seq[highcode]-seq[highcode-1])
            index=index+1
    return flattenImg
# main
# imports
import numpy as np 
import cv2 as cv
from pathlib import Path
#input file & param 
probFile=input("Please enter file of probability in type .npy 1 d array in length 226 :\n")
codeFile=input("Please enter file of probability codes in type .npy 1 d array  :\n")
fristDiminstion=int(input("Please enter frist dimension of image :\n"))
secondDiminstion=int(input("Please enter second dimension of image :\n"))
blockSize=int(input("Please enter a block size:\n"))
#check inputs
if(fristDiminstion>0 and secondDiminstion >0 and Path(codeFile).is_file() and Path(probFile).is_file() ):
    propability=np.load(probFile)
    codes=np.load(codeFile)
    #array declaration
    eleminateprobability=[]
    currentColor=[]
    sequance=[]
    j=0
    #(269, 229)
    # eleminate zeroes
    for i in range(0,256):
        if(propability[i]!= 0):
            eleminateprobability.insert(j,propability[i])
            currentColor.insert(j,i)
            j=j+1
    #sequance ranges
    sequance.insert(0,0)
    for i in range(1,j+1):
        sequance.insert(i,sequance[i-1]+eleminateprobability[i-1])
    flattenImage=decodeArithmatic(sequance,currentColor,blockSize,codes)
    flattenImg=np.array([])
    for i in range(0,fristDiminstion* secondDiminstion):
        flattenImg=np.insert(flattenImg,i,flattenImage[i])
        
        
    image=flattenImg.reshape(fristDiminstion, secondDiminstion).astype(np.uint8) 
    cv.imwrite('imageAfterDecoding.jpg', image) 
    
    
    print("the decoded image in file named imageAfterDecoding.jpg in the same folder of code ")
    
else:
    print ('you enter invalid inputs please, try again and enter valid')    
