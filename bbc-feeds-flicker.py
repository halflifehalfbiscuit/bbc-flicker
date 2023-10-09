#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet
import bbc_feeds
import os
import sys 
import time
import logging
import spidev as SPI
sys.path.append("..")
from lib import LCD_1inch69
from PIL import Image, ImageDraw, ImageFont

# Raspberry Pi pin configuration:
RST = 27
DC = 25
BL = 18
bus = 0 
device = 0 
logging.basicConfig(level = logging.DEBUG)


# display with hardware SPI:
''' Warning!!!Don't  creation of multiple displayer objects!!! '''
#disp = LCD_1inch69.LCD_1inch69(spi=SPI.SpiDev(bus, device),spi_freq=10000000,rst=RST,dc=DC,bl=BL)
disp = LCD_1inch69.LCD_1inch69()
# Initialize library.
disp.Init()
# Clear display.
disp.clear()


Font1 = ImageFont.truetype("../Font/Font01.ttf", 25)
Font2 = ImageFont.truetype("../Font/Font01.ttf", 35)
Font3 = ImageFont.truetype("../Font/Font02.ttf", 20)
#Font4 = ImageFont.truetype("../Font/DejaVuSans-Bold.ttf ", 20)

infin = 0
while infin <1:

	stories= bbc_feeds.news().all(limit=20)

	for story in stories:
	    s_title = story.title
	    s_summary = story.summary 
	
	s_range = range(20)
	for i in s_range:
	   logging.info("Loading News Feed...")
	   ImagePath = "../pic/bbc-news.jpg"
	   image1 = Image.open(ImagePath)        
	   disp.ShowImage(image1)
	   draw = ImageDraw.Draw(image1)
	   draw.text((15,25),stories[i].title[0:30], fill = "BLACK", font=Font3)
	   draw.text((15,50),stories[i].title[30:60], fill = "BLACK", font=Font3)
	   draw.text((15,75),stories[i].title[60:90], fill = "BLACK", font=Font3)
	   draw.text((15,100),stories[i].title[90:120], fill = "BLACK", font=Font3)
	   draw.text((15,125),stories[i].summary[0:30], fill = "BLUE", font=Font3)
	   draw.text((15,150),stories[i].summary[30:60], fill = "BLUE", font=Font3)
	   draw.text((15,175),stories[i].summary[60:90], fill = "BLUE", font=Font3)
	   draw.text((15,200),stories[i].summary[90:120], fill = "BLUE", font=Font3)
	   draw.text((15,225),stories[i].summary[120:150], fill = "BLUE", font=Font3)
	   image1=image1.rotate(0)
	   disp.ShowImage(image1)
	   time.sleep(60)
	   disp.clear()

	sports_stories= bbc_feeds.sports().all(limit=20)

	for story in sports_stories:
	    s_title = story.title
	    s_summary = story.summary 

	s_range = range(20)
	for i in s_range:
	   logging.info("Loading Sports Feed...")
	   ImagePath = "../pic/pique.jpg"
	   image1 = Image.open(ImagePath)        
	   disp.ShowImage(image1)
	   draw = ImageDraw.Draw(image1)
	   draw.text((15,25),sports_stories[i].title[0:30], fill = "BLACK", font=Font3)
	   draw.text((15,50),sports_stories[i].title[30:60], fill = "BLACK", font=Font3)
	   draw.text((15,75),sports_stories[i].title[60:90], fill = "BLACK", font=Font3)
	   draw.text((15,100),sports_stories[i].title[90:120], fill = "BLACK", font=Font3)
	   draw.text((15,125),sports_stories[i].summary[0:30], fill = "BLUE", font=Font3)
	   draw.text((15,150),sports_stories[i].summary[30:60], fill = "BLUE", font=Font3)
	   draw.text((15,175),sports_stories[i].summary[60:90], fill = "BLUE", font=Font3)
	   draw.text((15,200),sports_stories[i].summary[90:120], fill = "BLUE", font=Font3)
	   draw.text((15,225),sports_stories[i].summary[120:150], fill = "BLUE", font=Font3)
	   image1=image1.rotate(0)
	   disp.ShowImage(image1)
	   time.sleep(60)
	   disp.clear()

	tech_stories= bbc_feeds.news().tech(limit=20)

	for story in tech_stories:
	    s_title = story.title
	    s_summary = story.summary 
	
	s_range = range(20)
	for i in s_range:
	   logging.info("Loading Tech Feed...")
	   ImagePath = "../pic/pi.jpg"
	   image1 = Image.open(ImagePath)        
	   disp.ShowImage(image1)
	   draw = ImageDraw.Draw(image1)
	   draw.text((15,25),tech_stories[i].title[0:30], fill = "BLACK", font=Font3)
	   draw.text((15,50),tech_stories[i].title[30:60], fill = "BLACK", font=Font3)
	   draw.text((15,75),tech_stories[i].title[60:90], fill = "BLACK", font=Font3)
	   draw.text((15,100),tech_stories[i].title[90:120], fill = "BLACK", font=Font3)
	   draw.text((15,125),tech_stories[i].summary[0:30], fill = "BLUE", font=Font3)
	   draw.text((15,150),tech_stories[i].summary[30:60], fill = "BLUE", font=Font3)
	   draw.text((15,175),tech_stories[i].summary[60:90], fill = "BLUE", font=Font3)
	   draw.text((15,200),tech_stories[i].summary[90:120], fill = "BLUE", font=Font3)
	   draw.text((15,225),tech_stories[i].summary[120:150], fill = "BLUE", font=Font3)
	   image1=image1.rotate(0)
	   disp.ShowImage(image1)
	   time.sleep(60)
	   disp.clear()

disp.module_exit()
logging.info("quit:")




