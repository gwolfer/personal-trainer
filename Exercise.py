#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime
from math import log

class Exercise(object):
    
  def __init__(self, params):
    self.__id = params['id']
    self.__history = []
    self.__total = 0
    
    self._label = params['label']
    self._steps = params['steps']    
    
    self.__load()
    
  def __load(self):
    try:
      with open('records/%s.rec' % self.__id, 'r') as f:
        for line in f:
          (timestamp, step) = line.rstrip('\n').split('|')
          step = int(step)
          self.__total += step
          self.__history.append({'timestamp': timestamp, 'step': step})
    except Exception as e:
      print e

  def add(self, step):
    timestamp = datetime.now()
    self.__total += step
    self.__history.append({'timestamp': timestamp, 'step': step})
    try:
      with open('records/%s.rec' % self.__id, 'a') as f:
        f.write('%s|%d\n' % (timestamp, step))
    except Exception as e:
      print e

  @property
  def label(self):
    return self._label

  @property
  def steps(self):
    return self._steps

  @property
  def level(self):
    if not self.__total:
      return 0
    return int(log(self.__total, 2))

  @property
  def progress(self):
    if not self.__total:
      return 0	  
    return int((float(self.__total) / (2 ** self.level) - 1) * 100)
