#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 23 21:27:12 2021

@author: johanndrayne
"""

import PyPDF2
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

pdf_file = '/Users/johanndrayne/Downloads/FY20_Financial_Information_Act_Report.pdf'
pdfFileObj = open(pdf_file, 'rb')
 
# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
 
# printing number of pages in pdf file
# print(pdfReader.numPages)
 
# creating a page object
# from page 46 - 148


# extracting text from page
data = pd.DataFrame({'name':[], 'salary':[], 'expense':[]})



for page in range(46, 148, 1):

    pageObj = pdfReader.getPage(page)
    pagetxt = pageObj.extractText()
     
    begin = 0
    finished_prof = 0
    prof = []
    for i in pagetxt.split('\n'):
    
        if begin == 1:
    
            if finished_prof == 1:
    
                name = ''
                pay = prof[-2].replace(',','')
                exp = prof[-1].replace(',','')
                for n in prof[0:-2]:
                    name = name + n + ' '
                new_row = pd.DataFrame({'name':[name], 'salary':[pay], 'expense':[exp]})
                data = data.append(new_row, ignore_index=True)
               
                
                prof = []
                finished_prof = 0
                
            if len(i.split()) != 0 and i.split() != ['Remuneration', 'Expenses*']:
                
    
                if finished_prof == 0 and (i.split()[-1] == '-' or i.split()[-1].replace(',','').isnumeric()): 
                    for k in i.split():
                        prof.append(k)
                    finished_prof = 1
                    
    
                else:
                    for k in i.split():
                        prof.append(k)               
                    finished_prof = 0
                    
                    
     
        if i == "  Remuneration Expenses* ":
            begin = 1
    



# closing the pdf file object
pdfFileObj.close()



data['salary'] = data['salary'].astype('int')
data.hist(column='salary', bins = 300)
plt.xlabel('Salary ($)')
plt.ylabel("Number Of Professors")




