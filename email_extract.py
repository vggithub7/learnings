# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 19:26:38 2020
@author: lab
"""

import urllib.request 
  
# Importing module required for 
# regular expressions 
import re 
  
# Assign urlopen to a file object variable 
fhand = urllib.request.urlopen('https://cit.ac.in/departments/cse/academic') 
c=0  
for line in fhand: 
    # Getting the text file 
    # content line by line. 
    s = line.decode().strip() 
  
    # regex for extracting all email-ids 
    # from the text file 
    reg = re.findall(r"[A-Za-z0-9._%+-]+"
                     r"@[A-Za-z0-9.-]+"
                     r"\.[A-Za-z]{2,4}", s) 
  
    # printing the list output 
    
    for i in reg:
        if len(i)!=0:
            print(i)
            c=c+1
print(c)        
    #print(reg) 
