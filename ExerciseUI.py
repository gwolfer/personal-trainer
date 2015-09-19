#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import QString
from PyQt4.QtGui import QWidget, QLabel, QGridLayout, QGroupBox, QPushButton, QProgressBar

class ExerciseUI(QGroupBox):

  def __init__(self, exercise):
    super(ExerciseUI, self).__init__()
    self.exercise = exercise
    self.initUI()

  def initUI(self):
    self.setTitle(self.exercise.label)
    
    self.level = QLabel(QString('Lvl. %d' % self.exercise.level))

    self.progressbar = QProgressBar()
    self.progressbar.setMinimum(0)
    self.progressbar.setMaximum(100)
    self.progressbar.setValue(self.exercise.progress)

    grid = QGridLayout()
    grid.addWidget(self.level, 0, 0)
    grid.addWidget(self.progressbar, 0, 1, 1, 9)
    for (index, step) in enumerate(self.exercise.steps):
      btn = QPushButton(QString('+') + QString.number(step))
      grid.addWidget(btn, 1, index)
      btn.clicked.connect(self.buttonClicked)

    self.setLayout(grid)

  def buttonClicked(self):
    sender = self.sender()
    step = int(str(sender.text()).lstrip('+'))
    self.exercise.add(step)
    self.level.setText(QString('Lvl. %d' % self.exercise.level))
    self.progressbar.setValue(self.exercise.progress)

