#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import RPi.GPIO as GPIO
import time

import sys
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

import os
import picamera

import pygame
from pygame.locals import *

#Initialisation
pygame.init()
son = pygame.mixer.Sound("ALARME.wav")


# Déclaration variables + set des ports

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
 
GPIO_PIR = 7
print "PIR Module Test (CTRL-C to exit)"
GPIO.setup(GPIO_PIR,GPIO.IN)   
GPIO.setup(12,GPIO.IN)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
t0  = 0
tmoins1 = 0
camera=picamera.PiCamera()
bouton=GPIO.input(12)

def arret():
	sys.exit(0)
def video():
	
	son.play()
	dureeVideo=10

	#nomVideo = time.strftime("%d.%m.%Y-%Hh%Mm%Ss")
	print(nomVideo)

	camera.start_recording(nomVideo+".h264")
	print("REC...")
	time.sleep(dureeVideo)
	camera.stop_recording()

	commande = "MP4Box -add "+nomVideo+".h264 " + nomVideo+".mp4"
	os.system(commande)

def led():
	GPIO.output(21,GPIO.HIGH)
	GPIO.output(20,GPIO.HIGH)
	GPIO.output(16,GPIO.HIGH)
	GPIO.output(26,GPIO.HIGH)
	GPIO.output(19,GPIO.HIGH)
	GPIO.output(13,GPIO.HIGH)
	
def led_init():
	GPIO.output(21, GPIO.LOW) 
	GPIO.output(20, GPIO.LOW) 
	GPIO.output(16, GPIO.LOW)
	GPIO.output(26, GPIO.LOW) 
	GPIO.output(19, GPIO.LOW) 
	GPIO.output(13, GPIO.LOW)  
	


def email():
	#nomVideo = time.strftime("%d.%m.%Y-%Hh%Mm%Ss")
	fromaddr = "rasberrypi341@gmail.com"
	toaddr = "proprietairedetecteur@gmail.com"
	 
	msg = MIMEMultipart()
	 
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "MOUVEMENT DETECTE"
	 
	body = "Bonjour, \n Un mouvement vient d'être détecté ! \n Vous retrouverez ci-joint une photo de la détection"
	 
	msg.attach(MIMEText(body, 'plain'))
	 
	filename = str(nomVideo)+".mp4"
	attachment = open(filename, "rb")
	 
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	 
	msg.attach(part)
	 
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "detecteur")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	print("message envoye")
	server.quit()

try:
	
	led_init()
	print "Attente du capteur"
 
	while GPIO.input(GPIO_PIR)==1:
		t0  = 0
	print "  Prêt"
#	while GPIO.input(12)==True :
#	i=1
#	t0 = GPIO.input(GPIO_PIR)
	nomVideo = time.strftime("%d.%m.%Y-%Hh%Mm%Ss")
	while True:	
		t0=GPIO.input(GPIO_PIR)
		if t0==1 and tmoins1==0:
			
			print "  Mouvement détecté"
			print("allumage LED")
			led()
			video()
			email()
			tmoins1=1
			
		elif t0==0 and tmoins1==1:
			
			print "  Prêt"
			led_init()
			son.stop()
			tmoins1=0
 
		
		time.sleep(0.01)
 
except KeyboardInterrupt:
	print "  Quit"
	GPIO.cleanup()
	
	
	
	

		

			
		



	
	
