import re
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi
class Main(QDialog):
    global array7
    array7 = []
    def __init__(self):
        super(Main, self).__init__()
        loadUi('Form.ui', self)
        self.setWindowTitle('Работа с файлами в Python')
        self.pushButton_run.clicked.connect(self.run)
        self.pushButton_clean.clicked.connect(self.clean)
        self.pushButton_load.clicked.connect(self.load)
        self.pushButton_export.clicked.connect(self.export)


    def run(self):
        stroke = array7[1].copy()
        max = self.find_max()
        self.textEdit_array.insertPlainText('Max = ' + str(max[0]) + ' [' + str(max[1]) + ',' + str(max[2]) + ']\n' + '\n')
        min = self.find_min()
        self.textEdit_array.insertPlainText('Min = ' + str(min[0]) + ' [' + str(min[1]) + ',' + str(min[2]) + ']\n' + '\n')

              #  Если условие выполнено
        if (max[1] == min[1] + 1) | (max[2] == min[2] + 1):

            for i in range(len(array7)):
                array7[1][i] = array7[0][i]

            for i, val in enumerate(stroke):
                array7[0][i] = val

            for i, iVal in enumerate(array7):
                for j, jVal in enumerate(iVal):
                    self.textEdit_array.insertPlainText(str(array7[i][j]) + " ")
                self.textEdit_array.insertPlainText('\n')
        return array7

    def find_min(self):
        col = 0
        row = 0
        itr = 0
        min_num = array7[0][0]
        for i in array7:
            for j in i:
                if j < min_num:
                    min_num = j
                    row = itr
                    col = i.index(j)
            itr += 1
        return [min_num, row, col]

    def find_max(self):
        col = 0
        row = 0
        itr = 0
        max_num = array7[0][0]
        for i in array7:
            for j in i:
                if j > max_num:
                    max_num = j
                    row = itr
                    col = i.index(j)
            itr += 1
        return [max_num, row, col]

    def clean(self):
        self.textEdit_array.setPlainText('')


    def export(self):
        # ar = self.run()
        out_file = open(u'F:\PSU\Python\ZSA_Lab5\output.txt', 'w')  # открываем файл в режиме записи
        for row in array7:  # перебираем каждую строку массива
            for num in row:  # перебираем каждое значение строки
                out_file.write("%d " % num)  # записываем это значение
            out_file.write('\n')  # дописываем перевод на новую строку


    def load(self):
        global path_to_file
        path_to_file = QFileDialog.getOpenFileName(self, 'Открыть файл', '',
                                                   "Text Files (*.txt)")[0]

        if path_to_file:
            file = open(path_to_file, 'r')

            f = file.read()
            # выводим считанные данные на экран
            self.textEdit_array.insertPlainText("Полученные данные: \n" +
                                               f + "\n")

            array = []
            for num in re.findall(r'\b[0-9]+\b', f):
                array.append(num)
            sub = []
            for i in array:
                sub.append(int(i))
                if len(sub) > 4:
                    array7.append(sub)
                    sub = []


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()