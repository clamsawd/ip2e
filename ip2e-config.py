#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# --------------------------------------------------------------
# ip2e (IP to email) - Create the configuration file.          |
# Created by clamsawd (clamsawd@openmailbox.org)               |
# Licensed by GPL v.3                                          |
# Last update: 29-10-2015                                      |
#                                                              |
# Dependences: curl, wget, sendEmail, libio-socket-ssl-perl    |
# Compatible with Python 3.x                                   |
# --------------------------------------------------------------
version="0.6-alpha"

#Import python-modules
import os
import sys

#Check if your system use Python 3.x
if sys.version_info<(3,0):
	print ("")
	print ("You need python 3.x to run this program.")
	print ("")
	exit(1)

#Function to clear screen
def ClearScreen():
	if os.name == "posix":
		os.system("clear")
	elif os.name == "nt":
		os.system("cls")
	else:
		print ("Error: Unable clear screen")
		
#Detect system & PATH of user folder
if os.name == "posix":
	os.chdir(os.environ["HOME"])
	print ("POSIX detected")
elif os.name == "nt":
	os.chdir(os.environ["USERPROFILE"])
	print ("Windows detected")

if not os.path.exists(".ip2e"):
	os.makedirs(".ip2e")
	os.chdir(".ip2e")
if os.path.exists(".ip2e"):
	os.chdir(".ip2e")

ClearScreen()
print ("")
print ("ip2e-config v"+version+" - Create config.file")
print ("")
FromEmail=input("Type the email sender: ")
FromEmailUser=input("Type the user of email sender: ")
FromEmailPass=input("Type the pass of email sender: ")
SmtpFromEmail=input("Type the server STMP of email sender: ")
ToEmail=input("Type the email receiver: ")

#Create 'ip2e-conf.py'
def createip2ecf():
	ip2ecf=open('ip2e-conf.py','w')
	ip2ecf.close()
def writeip2ecf():
	ip2ecf=open('ip2e-conf.py','a')
	ip2ecf.write('# sample configuration file of ip2e\n')
	ip2ecf.write('\n')
	ip2ecf.write('FromEmail="'+FromEmail+'"\n')
	ip2ecf.write('FromEmailUser="'+FromEmailUser+'"\n')
	ip2ecf.write('FromEmailPass="'+FromEmailPass+'"\n')
	ip2ecf.write('SmtpFromEmail="'+SmtpFromEmail+'"\n')
	ip2ecf.write('ToEmail="'+ToEmail+'"\n')
	ip2ecf.close()

if os.name == "posix":
	os.system("rm ip2e-conf.py")
elif os.name == "nt":
	os.system("del ip2e-conf.py")
createip2ecf()
writeip2ecf()
exec(open("ip2e-conf.py").read())

#Show the configuration
ClearScreen()
print ("")
print ("ip2e-config v"+version+" - Current config.file")
print ("")
if os.name == "posix":
	os.system("cat ip2e-conf.py")
elif os.name == "nt":
	os.system("type ip2e-conf.py")
print ("")
