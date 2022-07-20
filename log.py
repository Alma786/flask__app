# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:01:17 2022

@author: bsingh12
"""

import json
import timeit
import traceback
import sys
import unidecode

def main_writer(f,argument):
  try:
    f.write(str(argument))
  except UnicodeEncodeError:
    f.write(unidecode.unidecode(argument))


def logger(*argv,logfile="log.txt",singleLine = False):
  """
  Writes Logs to LogFile
  """
  with open(logfile, 'a+') as f:
    for arg in argv:
      if arg == "{}":
        continue
      if type(arg) == dict and len(arg)!=0:
        json_object = json.dumps(arg, indent=4, default=str)
        f.write(str(json_object))
        f.flush()
        """
        for key,val in arg.items():
          f.write(str(key) + " : "+ str(val))
          f.flush()
        """
      elif type(arg) == list and len(arg)!=0:
        for each in arg:
          main_writer(f,each)
          f.write("\n")
          f.flush()
      else:
        main_writer(f,arg)
        f.flush()
      if singleLine==False:
        f.write("\n")
    if singleLine==True:
      f.write("\n")

def tryFunc(func, func_name=None, *args, **kwargs):
  """
  Time for Successfull Runs
  Exception Traceback for Unsuccessful Runs
  """
  stack = traceback.extract_stack()
  filename, codeline, funcName, text = stack[-2]
  func_name = func.__name__ if func_name is None else func_name # sys._getframe().f_code.co_name # func.__name__
  start = timeit.default_timer()
  x = None
  try:
    x = func(*args, **kwargs)
    stop = timeit.default_timer()
    # logger("Time to Run {} : {}".format(func_name, stop - start))
  except Exception as e:
    logger("Exception Occurred for {} :".format(func_name))
    logger("Basic Error Info :",e)
    logger("Full Error TraceBack :")
    # logger(e.message, e.args)
    logger(traceback.format_exc())
  return x

def vamsi(s):
  print(s)
