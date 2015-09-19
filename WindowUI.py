#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import QString
from PyQt4.QtGui import QWidget, QMessageBox, QDesktopWidget, QVBoxLayout
from Exercise import Exercise
from ExerciseUI import ExerciseUI

class WindowUI(QWidget):
    
  def __init__(self):
    super(WindowUI, self).__init__()
    self.initUI()

  def initUI(self):               
    self.resize(250, 150)
    self.center()
    self.setWindowTitle('Personal Trainer')
    
    self.exercises = [
      ExerciseUI(Exercise({
        'id': QString('regular_push_up'),
        'label': QString('Regular Push-up'),
        'steps': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
        'unit': ''})),
      ExerciseUI(Exercise({
        'id': QString('diamond_push_up'),
        'label': QString('Diamond Push-up'),
        'steps': [5, 10, 15, 20, 25, 30, 35, 40, 45, 50],
        'unit': ''})),
      ExerciseUI(Exercise({
        'id': QString('one_hand_push_up'),
        'label': QString('One-handed Push-up'),
        'steps': [3, 4, 6, 5, 7, 8, 10, 12, 14, 16],
        'unit': ''})),                
      ExerciseUI(Exercise({
        'id': QString('pull_up'),
        'label': QString('Pull-up'),
        'steps': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
        'unit': ''})),
      ExerciseUI(Exercise({
        'id': QString('crunch'),
        'label': QString('Crunch'),
        'steps': [30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
        'unit': ''})),        
      ExerciseUI(Exercise({
        'id': QString('running'),
        'label': QString('Running'),
        'steps': [30, 40, 50, 60, 70, 80, 90, 100, 110, 120],
        'unit': 'min'}))
      ]

    vbox = QVBoxLayout()
    for exercise in self.exercises:
      vbox.addWidget(exercise)
      self.setLayout(vbox)
    
    self.show()
        
  def closeEvent(self, event):
    reply = QMessageBox.question(self, 'Message',
      'Are you sure to quit?', QMessageBox.Yes | 
      QMessageBox.No, QMessageBox.No)
    if reply == QMessageBox.Yes:
      event.accept()
    else:
      event.ignore()
      
  def center(self):      
    qr = self.frameGeometry()
    cp = QDesktopWidget().availableGeometry().center()
    qr.moveCenter(cp)
    self.move(qr.topLeft())      
