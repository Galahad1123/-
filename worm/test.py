# coding=utf-8
import sys

import numpy as np
import pandas as pd
import pandas.errors
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from numpy import arange, meshgrid, sqrt, sin


# from openpyxl import load_workbook
#
# wb = load_workbook('Movie-Data2.xlsx')
# sheets = wb.worksheets  # 获取当前所有的sheet
# # print(sheets)
#
# # 获取第一张sheet
# sheet1 = sheets[0]
# # sheet1 = wb['Sheet']  # 也可以通过已知表名获取sheet
# print(sheet1)
#
# # 通过Cell对象读取
# cell_11 = sheet1.cell(1, 1).value
# print(cell_11)
# cell_11 = sheet1.cell(2, 2).value
# print(cell_11)
# import csv
#
# src_file = open('1000-Data2.csv', 'r', encoding='utf-8-sig')
# reader = csv.reader(src_file)
# src_list = next(reader)
# while True:
#     print(src_list)
#     try:
#         src_list = next(reader)
#     except StopIteration:
#         break
# for i in ('gbk', 'utf-8', 'gb18030', 'ansi'):
#     try:
#         data = pd.read_csv('1000-Data2.csv', encoding=i)
#         print(i + 'decode success')
#     except UnicodeDecodeError:
#         print(i + 'decode fail')

# src_datas = pd.read_csv('1000-Data2.csv', encoding='gb18030', error_bad_lines=False)
# print(src_datas)

src_datas = pd.read_csv('data/1000-Data8.csv', encoding='gb18030')
tag_col = src_datas['标签']
print(tag_col)
