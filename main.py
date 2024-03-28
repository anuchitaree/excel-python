from modules import read
from os import listdir
from os.path import isfile, join
from glob import glob,glob1
import pandas


# excel_data_df = pandas.read_excel("/home/anuchitaree/customapps/excel/summary/DNKI_Dec'23.xlsx", sheet_name="TIE&PE",header=None)
# row = excel_data_df.values.tolist()
# print(row[48])
path ="/home/anuchitaree/customapps/excel/summary/DNKI_Dec'23.xlsx"
read.read_excel_pandas(path)
# print('test')
# xlsxfile =[]
# for f in glob('/home/anuchitaree/customapps/excel/summary/*.xlsx'):
#     test = read.read_excel_pandas(f)
#     print(f)
    # result,file_name,data = read.file_name_separate(f)
    # print(result,file_name,data)
    # if result ==True:
    #     data_list = read.read_excel(file_name)







# path = 'D:\\Project\\excel-python'
# # wb = load_workbook(path,data_only=True)

# mywb = openpyxl.Workbook('path')
# sn = mywb.get_sheet_names()
# print(sn)


# fi = os.listdir(path)
# files = [f for f in fi if f.endswith(".xlsx")]
# print(files)

# for f in files:
#     paths = path+('\\') + f
#     print(paths)
#     # wb = openpyxl.load_workbook(paths, data_only= True)
#     # wss = wb.get_sheet_names()
#     # for s in wss:
#     #     print(s)

#     # ws = wb['Sheet1']
#     # print(ws)
#     # d = ws.cell(row =1, column=5)
#     # print(d.value)

# walmart_excel = pd.read_excel(path, sheet_name='TIE&PE')
# print(walmart_excel.iloc[0:48, 0:3])


#     # print(f)

# # ws = wb['Sheet1']
# # print(ws)
