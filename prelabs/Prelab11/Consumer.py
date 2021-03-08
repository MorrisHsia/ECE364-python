#! /user/local/bin/python3.7

#######################################################
#   Author:     Tsung Lin Hsia
#   email:      thsia@purdue.edu
#   ID:         ee364g21
#   Date:       3/31/2019
#######################################################

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from Prelab11.BasicUI import *
import re

class Consumer(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(Consumer, self).__init__(parent)
        self.setupUi(self)
        self.componentCount=[self.txtComponentCount_1,self.txtComponentCount_2,self.txtComponentCount_3,self.txtComponentCount_4,self.txtComponentCount_5,self.txtComponentCount_6,self.txtComponentCount_7,self.txtComponentCount_8,self.txtComponentCount_9,self.txtComponentCount_10,self.txtComponentCount_11,self.txtComponentCount_12,self.txtComponentCount_13,self.txtComponentCount_14,self.txtComponentCount_15,self.txtComponentCount_16,self.txtComponentCount_17,self.txtComponentCount_18,self.txtComponentCount_19,self.txtComponentCount_20]
        self.componentName=[self.txtComponentName_1,self.txtComponentName_2,self.txtComponentName_3,self.txtComponentName_4,self.txtComponentName_5,self.txtComponentName_6,self.txtComponentName_7,self.txtComponentName_8,self.txtComponentName_9,self.txtComponentName_10,self.txtComponentName_11,self.txtComponentName_12,self.txtComponentName_13,self.txtComponentName_14,self.txtComponentName_15,self.txtComponentName_16,self.txtComponentName_17,self.txtComponentName_18,self.txtComponentName_19,self.txtComponentName_20]
        #enable btn clear
        self.btnClear.clicked.connect(self.Clear)
        #enable save, disable load
        self.txtStudentName.textChanged.connect(self.DataEntry)#textChanged can detet whenever the text changed but textEdited can only detect mouse and keyborad changed, not the xml
        self.txtStudentID.textChanged.connect(self.DataEntry)
        self.chkGraduate.stateChanged.connect(self.DataEntry)
        for i in self.componentCount:
            i.textChanged.connect(self.DataEntry)
        for i in self.componentName:
            i.textChanged.connect(self.DataEntry)
        #enable btn save
        self.btnSave.clicked.connect(self.saveInXML)
        #enable btn load
        self.btnLoad.clicked.connect(self.loadData)

    def saveInXML(self):
        name=self.txtStudentName.text()
        id=self.txtStudentID.text()
        if self.chkGraduate.isChecked() == True:
            status='true'
        else:
            status='false'
        college=self.cboCollege.currentText()
        #CPName=deepcopy(self.componentName)
        #CPCount=deepcopy(self.componentCount)
        #for (i,item) in enumerate(CPName):
         #   if len(item.text()):
          #      CPName[i] = item.text
           # else:
            #    CPName[i] = ""
        #for (i,item) in enumerate(CPCount):
         #   if len(item.text()):
          #      CPCount[i] = item.text
           # else:
            #    CPCount[i] = ""
        CPName=[]
        CPCount=[]
        for i in self.componentName:
            if len(i.text()) != 0:
                CPName.append(i.text())
        for i in self.componentCount:
            if len(i.text()) != 0:
                CPCount.append(i.text())
        CPlist=list(zip(CPName,CPCount))

        with open('target.xml','w') as file:
            file.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            file.write('<Content>\n')
            file.write('    <StudentName graduate="{}">{}</StudentName>\n'.format(status,name))
            file.write('    <StudentID>{}</StudentID>\n'.format(id))
            file.write('    <College>{}</College>\n'.format(college))
            file.write('    <Components>\n')
            for (cname,ccount) in CPlist:
                file.write('        <Component name="{}" count="{}" />\n'.format(cname,ccount))
            file.write('    </Components>\n')
            file.write('</Content>')

    def loadDataFromFile(self, filePath):
        """
        Handles the loading of the data from the given file name. This method will be invoked by the 'loadData' method.
        
        *** YOU MUST USE THIS METHOD TO LOAD DATA FILES. ***
        *** This method is required for unit tests! ***
        """

        with open(filePath,"r") as file:
            content = file.readlines()[2:]
        complist=[]
        for line in content:
            line = line.strip()
            if 'StudentName' in line:
                if 'true' in line:
                    self.chkGraduate.setChecked(True)
                    line=line.replace("<StudentName graduate=\"true\">",'')
                    line=line.replace("</StudentName>",'')
                else:
                    self.chkGraduate.setChecked(False)
                    line=line.replace("<StudentName graduate=\"false\">", '')
                    line=line.replace("</StudentName>",'')
                self.txtStudentName.setText(line)
            elif 'StudentID' in line:
                line=line.replace('<StudentID>','')
                line=line.replace('</StudentID>','')
                self.txtStudentID.setText(line)
            elif 'College' in line:
                line=line.replace('<College>','')
                line=line.replace('</College>','')
                index = self.cboCollege.findText(line)
                self.cboCollege.setCurrentIndex(index)
            elif 'count' in line:
                cp = re.search('<Component name="(.*)" count="(.*)" />',line)
                complist.append((cp.group(1),cp.group(2)))
        for i,(name,count) in enumerate(complist):
            self.componentName[i].setText(name)
            self.componentCount[i].setText(count)






    def DataEntry(self):
        self.btnSave.setEnabled(True)
        self.btnLoad.setEnabled(False)

    def Clear(self):
        self.txtStudentName.clear()
        self.txtStudentID.clear()
        self.chkGraduate.setChecked(0)
        self.cboCollege.setCurrentIndex(0)
        for i in self.componentCount:
            i.clear()
        for j in self.componentName:
            j.clear()
        #self.btnClear.setEnabled(True)
    def loadData(self):
        """
        *** DO NOT MODIFY THIS METHOD! ***
        Obtain a file name from a file dialog, and pass it on to the loading method. This is to facilitate automated
        testing. Invoke this method when clicking on the 'load' button.

        You must modify the method below.
        """
        filePath, _ = QFileDialog.getOpenFileName(self, caption='Open XML file ...', filter="XML files (*.xml)")

        if not filePath:
            return

        self.loadDataFromFile(filePath)






if __name__ == "__main__":
    currentApp = QApplication(sys.argv)
    currentForm = Consumer()

    currentForm.show()
    currentApp.exec_()