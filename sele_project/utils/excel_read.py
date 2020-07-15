import pandas as pd

class ParseExcel():
    def __init__(self, path):
        self.workbook = pd.ExcelFile(path)
        self.sheets = [self.workbook.parse(i, header=None) for i in self.workbook.sheet_names]
    def getDataFromSheet(self, i = 0):
        dataList = list(self.sheets[i].iloc[:,0])
        return dataList
    def getDataFromSheetMul(self, i = 0):
        dataList0 = list(self.sheets[i].iloc[:,0])
        dataList1 = list(self.sheets[i].iloc[:,1])
        result = [[i, j] for i,j in zip(dataList0, dataList1)]
        return result

if __name__ == '__main__':
    path = './../data/test.xls'
    print(ParseExcel(path).getDataFromSheet())

