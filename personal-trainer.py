#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication
from WindowUI import WindowUI

def main():
    app = QApplication(sys.argv)
    window = WindowUI()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
