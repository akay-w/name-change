# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:26:31 2019

@author: a-whalen
"""

import tkinter as tk
from tkinter.filedialog import askdirectory
import os
import xlsxwriter

root = tk.Tk()
root.withdraw()

directory = askdirectory()
filelist = []
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith("sdlxliff"):
            filelist.append(os.path.join(os.path.normpath(root), file))

workbook = xlsxwriter.Workbook("File_list.xlsx")
worksheet = workbook.add_worksheet()
wrap_text = workbook.add_format()
wrap_text.set_text_wrap()
worksheet.set_column(0, 2, 50)
worksheet.write(0, 0, "Original Filename", wrap_text)
worksheet.write(0, 1, "Edited Filename", wrap_text)

def replace_non_ascii(s):
    return ''.join([i if ord(i) < 128 else '' for i in s])

row = 1
col = 0
for filepath in filelist:
    origfile = os.path.basename(filepath)
    newfile = replace_non_ascii(origfile)
    newfilepath = filepath.replace(origfile, newfile)
    os.rename(filepath, newfilepath)
    worksheet.write(row, col, origfile, wrap_text)
    worksheet.write(row, col+1, newfile, wrap_text)
    row += 1

workbook.close()
