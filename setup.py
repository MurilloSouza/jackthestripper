#!/usr/bin/python
#coding=utf-8

__AUTHOR__	= "Arc4nj0"
__VERSION__	= "0.0.9"
__DATE__	= "30/11/2015"
__FACE__    = "www.fb.com/Arc4nj0"

import os 
import sys 
import argparse


def install(): 

	print "Install the following dependencies"
	# INSTALL SSLSTRIP 
	os.system("sudo apt-get git")
	os.system("git clone https://github.com/moxie0/sslstrip")
	os.system("sudo python2 sslstrip/setup.py build")
	os.system("sudo python2 sslstrip/setup.py install") 

	# INSTALL ETTERCAP
	os.system ("sudo apt-get install ettercap-text-only") 

	# INSTALL ARPSPOOF
	os.system ("sudo apt-get install dsniff"); 


install() 
