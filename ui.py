from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
import csv

def main():
   app   = QApplication(sys.argv)
   table    = QTableWidget()
   tableItem   = QTableWidgetItem()

   data = []
   pathname = "pathtoyourfile"
   filename = 'filename'
   with open(pathname+filename, 'r') as csvFile:
      reader = csv.reader(csvFile)
      for row in reader:
         data.append(row)
 
# initiate table
   table.setWindowTitle("QTableWidget ")
   table.resize(600, 400)
   table.setRowCount(len(data))
   table.setColumnCount(len(data[1]))
   table.setHorizontalHeaderLabels("label1;label2".split(";"))

   # setting data
   # table.setItem(0,0, QTableWidgetItem("Item (1,1)"))
   for i in range(len(data)):
      for j in range(len(data[1])):
         table.setItem(i,j, QTableWidgetItem(data[i][j]))

   # show table
   table.show()
   return app.exec_()
 
if __name__ == '__main__':
   # gettingdata()
   main()
