# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 17:37:52 2020

@author: dell
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:43:18 2020

@author: dell
"""
import sys
import numpy as np
import math as ma
import pandas as pd
def main():
    script=sys.argv[0]
    filename=sys.argv[1]
   # w=sys.argv[3]
    wt=sys.argv[2]
    wt=wt.split(",") 
    wt=[float(i) for i in wt]
         
    w=sys.argv[3]
    dataset=pd.read_csv(filename)
    t=dataset.iloc[:,:]
    r=dataset.iloc[:,0].values
    d=dataset.iloc[:,1:].values
 #   d=d.as_matrix()
    
    sum=0
    p=[0]*100
    col = len(d[0])
    row = len(d)
    for i in range (0,col):
        sum+=float(wt[i]) 
    for i in range (0,col):
        wt[i]=float(wt[i]/sum)    
    for i in range(0,col):
        for j in range(0,row):
         #   print(d[j][i])
            p[i]=p[i]+(d[j][i]**2)
            
    for i in range(0,col):
        p[i]=ma.sqrt(p[i])    
    
    for i in range(0,col):         #normalised vectorization
        for j in range(0,row):
            d[j][i]=d[j][i]/p[i]
    for i in range (0,col):
        for j in range(0,row):
            d[j][i]=wt[i]*d[j][i]        
            
    idealbest=[]
    idealworst=[]
           
  
    for i in range(0,col):
       if(w[i]=='+'):
        #idealbest[i]=max(d[i])
        #idealbest[i]=min(d[i])
         idealbest.append([max(s) for s in zip(*d)][i])
         idealworst.append([min(s) for s in zip(*d)][i])
       else:
        #idealbest[i]=min(d[i])
        #idealworst[i]=max(d[i])
         idealbest.append([min(s) for s in zip(*d)][i])
         idealworst.append([max(s) for s in zip(*d)][i])
    
    q=[0]*1000
    
    lst = [] 
    a=[0]*100   
    b=[0]*100
    for i in range(0,row):
        for j in range (0,col):
            a[i] = a[i]+(d[i][j]-idealworst[j])**2
            b[i] = b[i]+(d[i][j]-idealbest[j])**2
    spos=[0]*100
    sneg=[0]*100
    for i in range(0,row):
        a[i]=np.sqrt(a[i])
        b[i]=np.sqrt(b[i])
    for i in range(0,row):
        q[i]=(a[i]/(a[i]+b[i]))
        #print(r[0][i])
        print(q[i])
    
    print(r)

#q.sort(reverse = True) 
main()
    
      
        
        
    