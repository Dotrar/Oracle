#!/usr/local/bin/python3

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtQml import *

from src.OracleKeypad import *
from src.Oracle import * 

if __name__ == '__main__':
    import sys

    sys_argv = sys.argv
    sys_argv += ['--style', 'universal']
    
    app = QGuiApplication(sys_argv)
    qmlRegisterType(OracleKeypad, 'OracleKeypad', 1, 0, 'OracleKeypad')
    qmlRegisterType(Oracle, 'Oracle', 1, 0, 'Oracle')
    engine = QQmlApplicationEngine()
    engine.load(QUrl.fromLocalFile("qml/main.qml"))
    if len(engine.rootObjects()) == 0:
        sys.exit(-1)
    sys.exit(app.exec_())
