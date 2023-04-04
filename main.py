# -*- coding: UTF-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import jiami.jiami_ui
import jiami.SHA1
import jiami.MD5
import jiami.HMAC
import jiami.DES
import jiami.AES


class pages_windows(jiami.jiami_ui.Ui_MainWindow, QMainWindow):
    def __init__(self):
        super(pages_windows, self).__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.pushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.pushButton_12.clicked.connect(lambda: self.sha1())
        self.pushButton_8.clicked.connect(lambda: self.md5())
        self.pushButton_17.clicked.connect(lambda: self.hmac())
        self.pushButton_18.clicked.connect(lambda: self.desj())
        self.pushButton_19.clicked.connect(lambda: self.desm())
        self.pushButton_21.clicked.connect(lambda: self.aesj())
        self.pushButton_20.clicked.connect(lambda: self.aesm())


    def sha1(self):
        sha1 = jiami.SHA1.Sha1_a()
        sha1.data = self.textEdit_10.toPlainText()
        miw = sha1.encrypt()
        self.textEdit_9.setText(miw)
        sha1.data = ''

    def md5(self):
        md5 = jiami.MD5.Md5_a()
        md5.data = self.textEdit_3.toPlainText()
        miw = md5.encrypt()
        self.textEdit_2.setText(miw)
        md5.data = ''

    def hmac(self):
        hmac = jiami.MD5.Md5_a()
        hmac.data = self.textEdit_19.toPlainText()
        hmac.key = self.textEdit_21.toPlainText()
        miw = hmac.encrypt()
        self.textEdit_20.setText(miw)
        hmac.data = ''
        hmac.key = ''

    def desj(self):
        desj = jiami.DES.Des_a()
        desj.s = self.textEdit_23.toPlainText()
        desj.secret_key = self.textEdit_24.toPlainText()
        miw = desj.des_encrypt()
        self.textEdit_22.setText(miw.decode('utf-8'))
        desj.s = ''
        desj.secret_key = ''

    def desm(self):
        desm = jiami.DES.Des_a()
        desm.data = self.textEdit_26.toPlainText()
        desm.key = self.textEdit_27.toPlainText()
        minw = desm.des_decrypt()
        self.textEdit_25.setText(minw.decode('utf-8'))
        desm.data = ''
        desm.key = ''

    def aesj(self):
        aesj = jiami.AES.Aes_a()
        text = self.textEdit_32.toPlainText()
        key = self.textEdit_30.toPlainText()
        miw = aesj.encrypt(text,key)
        self.textEdit_33.setText(miw)

    def aesm(self):
        aesm = jiami.AES.Aes_a()
        miwen = self.textEdit_31.toPlainText()
        key = self.textEdit_28.toPlainText()
        minw = aesm.decrypt(key,miwen)
        self.textEdit_29.setText(minw)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_widow = pages_windows()
    main_widow.show()
    sys.exit(app.exec_())
