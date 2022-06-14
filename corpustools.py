# Form implementation generated from reading ui file 'texttool.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#!/usr/bin/env img
# Author: Wei Ma
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.



import os
from tkinter import font

from pandas.core import groupby
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from pandas.core.algorithms import duplicated
from pandas.core.frame import DataFrame
from chosewords import choseTword
from corpustool import check
import re
from collections import Counter, defaultdict
import xlwt
import operator #用来对二维列表中的排序
import pandas as pd



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(824, 528)
        MainWindow.setFixedSize(824, 528)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 160, 471))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.textEdit_openfiles = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.textEdit_openfiles.setObjectName("textEdit_openfiles")
        self.verticalLayout.addWidget(self.textEdit_openfiles)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.lineEdit_fileinfo = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_fileinfo.setObjectName("lineEdit_fileinfo")
        self.verticalLayout.addWidget(self.lineEdit_fileinfo)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(163, 0, 20, 481))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(180, 10, 631, 471))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_check = QtWidgets.QWidget()
        self.tab_check.setObjectName("tab_check")
        self.textEdit_check = QtWidgets.QTextEdit(self.tab_check)
        self.textEdit_check.setGeometry(QtCore.QRect(10, 50, 601, 381))
        self.textEdit_check.setObjectName("textEdit_check")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_check)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 601, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.pushButton_check = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_check.setObjectName("pushButton_check")
        self.horizontalLayout_2.addWidget(self.pushButton_check)
        self.tabWidget.addTab(self.tab_check, "")
        self.tab_getlabel = QtWidgets.QWidget()
        self.tab_getlabel.setObjectName("tab_getlabel")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab_getlabel)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 251, 431))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_getlabels = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_getlabels.setObjectName("pushButton_getlabels")
        self.verticalLayout_2.addWidget(self.pushButton_getlabels)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.comboBox_labels = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_labels.setObjectName("comboBox_labels")
        self.verticalLayout_2.addWidget(self.comboBox_labels)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.textEdit_labelwords = QtWidgets.QTextEdit(self.verticalLayoutWidget_2)
        self.textEdit_labelwords.setObjectName("textEdit_labelwords")
        self.verticalLayout_2.addWidget(self.textEdit_labelwords)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.tab_getlabel)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(270, 10, 351, 431))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.textEdit_colorwords = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.textEdit_colorwords.setObjectName("textEdit_colorwords")
        self.verticalLayout_3.addWidget(self.textEdit_colorwords)
        self.tabWidget.addTab(self.tab_getlabel, "")
        self.tab_analyse = QtWidgets.QWidget()
        self.tab_analyse.setObjectName("tab_analyse")
        #self.progressBar_analyse = QtWidgets.QProgressBar(self.tab_analyse)
        #self.progressBar_analyse.setGeometry(QtCore.QRect(10, 410, 601, 23))
        #self.progressBar_analyse.setProperty("value", 0)
        #self.progressBar_analyse.setObjectName("progressBar_analyse")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_analyse)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 23))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout.addWidget(self.label_8)
        self.lineEdit_separator = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_separator.setObjectName("lineEdit_separator")
        self.horizontalLayout.addWidget(self.lineEdit_separator)
        self.textEdit_analyse = QtWidgets.QTextEdit(self.tab_analyse)
        self.textEdit_analyse.setGeometry(QtCore.QRect(10, 40, 611, 351))
        self.textEdit_analyse.setObjectName("textEdit_analyse")
        self.pushButton_analyse = QtWidgets.QPushButton(self.tab_analyse)
        self.pushButton_analyse.setGeometry(QtCore.QRect(500, 10, 101, 24))
        self.pushButton_analyse.setObjectName("pushButton_analyse")
        self.tabWidget.addTab(self.tab_analyse, "")
        self.tabWidget.raise_()
        self.verticalLayoutWidget.raise_()
        self.line.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 824, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        #self.action_close = QtGui.QAction(MainWindow)
        #self.action_close.setObjectName("action_close")
        self.action_set = QtGui.QAction(MainWindow)
        self.action_set.setObjectName("action_set")
        self.action_appear = QtGui.QAction(MainWindow)
        self.action_appear.setObjectName("action_appear")
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.menu.addAction(self.action_open)
        #self.menu.addAction(self.action_close)
        self.menu_2.addAction(self.action_set)
        self.menu_3.addAction(self.action_appear)
        self.menu_4.addAction(self.action_about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.font = QtGui.QFont()


        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "已标注语料工具"))
        MainWindow.setWindowIcon(QIcon('./res/qt.png'))
        self.label.setText(_translate("MainWindow", "已打开的语料文件："))
        self.label_2.setText(_translate("MainWindow", "共有："))
        self.label_3.setText(_translate("MainWindow", "KB的数据将被处理。"))
        self.label_4.setText(_translate("MainWindow", "待检查文件为："))
        self.pushButton_check.setText(_translate("MainWindow", "检查该语料"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_check), _translate("MainWindow", "语料检查"))
        self.pushButton_getlabels.setText(_translate("MainWindow", "获取标签"))
        self.label_5.setText(_translate("MainWindow", "点击按钮获取语料中的标签。"))
        self.label_6.setText(_translate("MainWindow", "符合该标签的词："))
        self.label_7.setText(_translate("MainWindow", "该词性下分色显示："))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_getlabel), _translate("MainWindow", "标签获取分色显示"))
        self.label_8.setText(_translate("MainWindow", "选择或输入分隔符："))
        self.pushButton_analyse.setText(_translate("MainWindow", "统计"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_analyse), _translate("MainWindow", "语料信息统计"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "工具界面"))
        self.menu_4.setTitle(_translate("MainWindow", "帮助"))
        self.action_open.setText(_translate("MainWindow", "打开"))
        #self.action_close.setText(_translate("MainWindow", "关闭"))
        self.action_set.setText(_translate("MainWindow", "整体设置"))
        self.action_appear.setText(_translate("MainWindow", "界面参数"))
        self.action_about.setText(_translate("MainWindow", "关于工具"))



        self.action_open.triggered.connect(self.openFile)
        self.pushButton_check.clicked.connect(self.checkcorpus)
        self.pushButton_getlabels.clicked.connect(self.findlabel)
        self.comboBox_labels.currentIndexChanged.connect(self.selectwords)
        self.comboBox_labels.currentIndexChanged.connect(self.wordProcess)
        self.pushButton_analyse.clicked.connect(self.txtinfo)
        #self.pushButton_analyse.clicked.connect(self.onStart)
        self.font.setFamily('Microsoft Himalaya')
        self.font.setPointSize(14)
        self.textEdit_colorwords.setFont(self.font)
        self.textEdit_labelwords.setFont(self.font)
        self.textEdit_check.setFont(self.font)
        self.textEdit_analyse.setFont(self.font)
   

    def openFile(self):
        try:
            fname = QtWidgets.QFileDialog.getOpenFileName(None, "打开文件", './')
            #self.fnm = fname
            global filepath 
            filepath = fname[0]
            if filepath:
                size = os.path.getsize(filepath) / 1024
                #print(filepath)
                #print(size)
                self.textEdit_openfiles.setText("已打开文件:" + filepath)
                self.lineEdit_fileinfo.setText(str(size)) 
                #with open(fname[0],'r+',encoding='utf8',errors="ignore") as f:
                    #self.fileContent.append(f.read())
                    #txtCon = "".join(self.fileContent)
                    #self.txtFile.setHtml("\n"+txtCon)                    
        except Exception:
            self.textEdit_openfiles.setText("未能获取到有效地址，请重新选择文件。")

    def checkcorpus(self):
        try:
            linelist = []
            with open(filepath, 'r',encoding='utf-8') as fo:
                lines = fo.readlines()
                for line in lines:
                    linelist += line.split()
                worddic = Counter(linelist)
                #print(worddic)
                self.textEdit_check.append('文件中找到以下语料标注问题：\n')
                for wordlb, numw in worddic.items():
                    if check(wordlb) != '':
                        line, nwordlb = check(wordlb)
                        if line != '':
                            self.textEdit_check.append(nwordlb + '***' + line)
        except:
            self.textEdit_check.setText("未能获取到有效地址，请重新选择文件。")


    def findlabel(self):
        global labelall
        global textlines
        textlines = []
        try:
            if filepath:
                pattern = r'_[a-z]+'
                labellist = []
                with open(filepath, 'r',encoding='utf-8') as fo:
                    lines = fo.readlines()
                    for line in lines:
                        textlines.append(line.strip())
                        labellist += re.findall(pattern, line)
                    labelall =  list(set(labellist))
            self.comboBox_labels.addItems(labelall)
            self.label_5.setText("已经获取到标签,请通过下拉框选择：")
        
        except:
            self.textEdit_labelwords.setText("未能获取到文件地址，请重新打开语料文件。")

    def selectwords(self, tag):
        try:
            tag =  self.comboBox_labels.currentText()
            self.textEdit_labelwords.setPlainText(f'你找到了标签为{tag}的词：\n')
            tag = tag.split('_')[1]
            #print(f"this is tag: {tag}")
            for line in textlines:
                wordlabels = line.split()
                #print(wordlabels)
                for wordlabel in wordlabels:
                    labelindex = wordlabel.rfind('_')
                    if labelindex != -1 and len(wordlabel) != 0:
                        word, label = wordlabel.split('_', 1)
                        if len(label) != 0 and tag in wordlabel:
                            self.textEdit_labelwords.append(word)
        except:
            self.textEdit_labelwords.append("未能获得有效标签，请重新获取标签。")

    def choseFont(self):
        try:
            font , ok = QtWidgets.QFontDialog.getFont()
            if ok:
                self.textEdit_labelwords.setCurrentFont(font)
        except:
            self.textEdit_labelwords.setText("发生内部错误。。。")



    def wordProcess(self):
        
        wtype = self.comboBox_labels.currentText()
        self.textEdit_colorwords.append(f'当前标签为{wtype}\n')
        #for label in labelall:
        #print(fname[0])
        try:
            #print(wtype)
        # self.fnm = fname
            if filepath:
                outl, outv, outr = choseTword(filepath, wtype, 'out_test.html')
                #self.txtFile.setText("\n" + outline)
                self.textEdit_colorwords.setFontFamily('Microsoft YaHei UI')
                for i in range(len(outl)):
                    a =( "<tr><td><font color='green' size='20'>%s</font></td>\
                        <td><font color='red' size='20'>%s</font></td> \
                        <td><font color='blue' size='20'>%s</font></td></tr><br>"  % (outl[i], outv[i],outr[i]))
                    
                    self.textEdit_colorwords.append(a)
        except :
            self.textEdit_colorwords.append("请通过菜单栏中语料检查先获取文本中的标签。")



#  defaultdict 这个真是个好东西啊 需要经常使用， defaultdict 的一个特征是它会自动初始化
# 每个 key 刚开始对应的值，所以你只需要关注添加元素操作了。
    def txtinfo(self):
        try:
        #self.textEdit.append("以下是词频")
            cipinlist = []
            txt_dict = defaultdict(list)
            wordlbn_dict = defaultdict(list)
            #words_dic = defaultdict(list)
            #lbs_dic = defaultdict(list)
            
            with open(filepath, 'r', encoding='utf-8') as fo:
                lines = fo.readlines()
                for line in lines:
                    wordlbs = line.strip().split()
                    #print(wordlbs)
                    
                    for wordlb in wordlbs:
                        labels = []
                        #print(wordlb.split('_'))
                        l, nwlb = check(wordlb)
                        #print(nwlb)
                        if (len(nwlb.split()) % 2) == 0:
                            for wb in nwlb.split():
                                word, lb = wb.split('_')
                                word = self.is_Tibetan(word)
                                txt_dict[word].append(lb)
                                cipinlist.append([word,lb])
                                #cipinlist.append([word,lb,numw])
                                #self.textEdit.append(wline)
                        else:
                            word, lb = nwlb.split('_')
                            word = self.is_Tibetan(word)
                            txt_dict[word].append(lb)
                            cipinlist.append([word,lb])
            #cipinlist.sort(key=operator.itemgetter(2), reverse=True)
                #wordlb_dic[word] = lb
            #wlpd = pd.DataFrame(data = cipinlist, columns=['词', '词性'])

            #将词和词性的词典txt_dict进行排序，排序依据的是词性的总数量len(x[1])，也就是词出现的个数。
            txt_dict2 = sorted(txt_dict.items(), key=lambda x:len(x[1]), reverse=True)
            #词频统计结果写入excel
            for dicword, labellist in txt_dict2:
                cl = Counter(labellist)
                wordlbn_dict['词'].append(dicword)
                wordlbn_dict['词频数'].append(sum(cl.values()))
                #词性数量以词性计数获得的词典长度为准，这里把词典转化为列表，更准确
                wordlbn_dict['词性数'].append(len(list(cl)))
                wordlbn_dict['词性'].append(dict(cl))

            #2022年1月5日使用了pandas处理词频，啊。。。真香。。。
            df = pd.DataFrame(cipinlist, columns=['词', '词性'])
            df['数量'] = 1
            #df['词数量'] = df['词'].map(df['词'].value_counts())
            #print(df) 
            #print('###################')
            #group3 = df.groupby(['词','词性']).sum()
            group3 = df.groupby(['词','词性']).sum()
            #print(len(group3))
            df_gp3 = pd.DataFrame(group3)
            df_gp3 = df_gp3.sort_values(by='词', ascending=False)
            #print(df_gp3)
            #self.textEdit_analyse.append(str(df_gp3))

            group2 = df.groupby('词性').sum()
            #print(len(group2))
            df_gp2 = pd.DataFrame(group2)
            df_gp2 = df_gp2.sort_values(by='数量',  ascending=False)
            #print(df_gp2)

            group1 = df.groupby('词').sum()
            #print(len(group1))
            df_gp1 = pd.DataFrame(group1)
            df_gp1 = df_gp1.sort_values(by='数量',  ascending=False)
            #print(df_gp1)

            df_gp4 = pd.DataFrame.from_dict(wordlbn_dict) 
            df_gp4 = df_gp4.sort_values(by='词性数',  ascending=False)

            path = os.getcwd()        
            if not os.path.exists(path + '/output'):
                os.makedirs(path + '/output')
            #book.save('output/cipin_out.xls')
            #df_gp.to_excel('output/cipin_out.xls', sheet_name='sheet3')
            #book.save('output/cipin_out.xls')
            outpath = 'output/cipin_out.xlsx'
            writer = pd.ExcelWriter(outpath)
            df_gp1.to_excel(writer, sheet_name='词频统计')
            df_gp2.to_excel(writer, sheet_name='标签统计')
            df_gp3.sort_values(by='词', ascending=False).to_excel(writer, sheet_name='词性统计1')
            df_gp4.to_excel(writer, sheet_name='多词性统计', index=0)

            #self.textEdit_analyse.setFontFamily('Microsoft YaHei UI')
            
            #将多词性标签写入到文本文件当中
            df_gp4.to_csv('output/oneword_result.txt', sep='\t', index=0)

            #从文本中读取前10行写入textEdit_analyse，本来要用self.textEdit_analyse.append(str(df_gp4.head(10)))
            #奈何不太好用
            with open('output/oneword_result.txt', 'r', encoding='utf-8') as fo:
                self.textEdit_analyse.append("<font  color='blue' size='10'>词性数量排在前10的信息如下：</font>")
                for line in fo.readlines()[:10]:
                    newline = "<font  color='green' size='8'>%s</font>" %(line)
                    self.textEdit_analyse.append(newline)


            print("啊 真香。。。！")
            writer.save()
            writer.close()
            self.textEdit_analyse.append(f"Excel文件：已将统计结果保存至在output文件夹下的cipin_out.xlsx中")
            self.textEdit_analyse.append("文本统计结果在output文件夹下的oneword_result.txt文件。")
            


            #self.textEdit_analyse.append(df_gp3)
            #sheet3 = book.add_sheet(u'单词词性统计结果', cell_overwrite_ok=True)
            #tagslist.sort(key=operator.itemgetter(1), reverse=True)
            #for i in group:
                #i.to_excel(writer, index=False, sheet_name='sheet3')
        except:
            self.textEdit_analyse.append("读取语料信息失败，请检查是否存在该文件或者语料内容格式。")


    #该函数用来判断单词是否为藏文，取第一个字符在字符集中比较，如果是就
    #判断后面是否有音节符，如果没有就加上
    def is_Tibetan(self, word):
        #必须考虑word为空的情况
        if word:
            if u'\u0F00' <= word[0] <= u'\u0FFF':
                if word[-1] != '་':
                    boword = word + '་'
                    return boword
                else:
                    boword = word
                    return boword
            else:
                return word 
        else:
            return word

'''
    进度条，后期再考虑吧。。。
    def onStart(self,task_number,total_task_number,i):
        
        self.progressBar_analyse.setValue(str(task_number), str(total_task_number),i + 1)  # 更新进度条的值
        QtWidgets.QApplication.processEvents()  # 实时刷新显示0F00-0FFF
'''
