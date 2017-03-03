'''
Created on 27 Jan 2017

@author: Tao
'''
from setuptools import setup
setup(name="SwE_A3",
      version="0.1",
      description="Assignment3",
      url="",
      author="Tao Li",
      author_email="taoli1021@gmail.com",
      licence="GPL3",
      packages=['assignment3'],
      entry_points={
          'console_scripts':['runMywork=assignment3.runmycode:mymain']
            }
    )