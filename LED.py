# Copyright (c) 2017 Out of the BOTS
# http://outofthebots.com.au/
# Author: Shane Gingell
#
# Redistribution and use in source and binary forms, with or without 
# modification, are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, 
#    this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice, 
#    this list of conditions and the following disclaimer in the documentation 
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND 
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
# OR TORT INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import spidev #import SPI package

spi = spidev.SpiDev()     #create an instance 
spi.open(0, 0)            #open coms on BUS 0
spi.max_speed_hz = 488000 #Max buad rate

start_bytes = [0,0,0,0]       #32 bits to signal the start of LED data stream
end_bytes = [255,255,255,255] #32 bits to signal the end of LED data strem
extra_bits = 0b11100000       #3 bits needed at the begining 32bit data for each LED

#Super LED use BGR colour space
red = [0,0,255]         #BGR for red
green = [0,255,0]       #BGR for green
blue = [255,0,0]        #BGR for blue
yellow = [0, 255, 255]  #BGR for yellow
purple = [255, 0, 200]  #BGR for purple
orange = [0, 100, 255]  #BGR for orange
black = [0,0,0]         #BGR for black (turn power off)

rainbow_list = [red, orange, yellow, green, blue, purple] #list of colours to form rainbow colour pattern

class Super_LED :

  def __init__(self, number_LEDs):    
	global no_LEDs                #global varable to store number of LEDs
	global LED_list               #global buffer to store current colors of all LEDs
	no_LEDs = number_LEDs         
	LED_list = [black] * no_LEDs  #initilize LED buffer
	self.set_brightness(31)       #initilize LED brightness (scale of 0-31)
  
  #set brightness
  def set_brightness (self,brightness):
    global global_byte 
    global_byte = extra_bits | brightness #set global_byte combined 3 extra_bits and brightness
  
  #writes LED buffer to physical LEDs
  def refreash_LED (self):    
	spi.xfer2(start_bytes)     #send 3 start bytes to signal start of LED data tream
	for i in range(no_LEDs):   #cycle through total number of LEDs
	  spi.xfer2([global_byte]) #send global_byte
	  spi.xfer2(LED_list[i])   #send 3 bytes og BGR
	spi.xfer2(end_bytes)       #send 3 end bytes
  
  #sets single pixel colour in LED buffer  
  def set_pixel(self, position, blue, green, red):
    LED_list[position] = [blue, green, red]  #update LED buffer
  
  #sets alternating 2 colours to LED buffer
  def set_2_colour(self, lenght, blue1, green1, red1, blue2, green2, red2):    
	colour_number = 0
	count = 1	
	colour1 = [blue1, green1, red1]   #create 3 byte BGR list of first colour
	colour2 = [blue2, green2, red2]   #create 3 byte BGR list of second colour
	for i in range(no_LEDs):          #cycle through all LEDs
	  if colour_number == 0 : LED_list[i] = colour1
	  else : LED_list[i] = colour2    #if number = 0 then write first colour to LED buffer else write second colour
	  if count == lenght :	          #swtich between colour ever number of lenght count
		if colour_number == 0 :	    
		  colour_number =1		  
		  count = 0		
		else :			  
		  colour_number = 0
		  count = 0
	  count += 1		   
  
  #sets same colour to whole LED buffer
  def set_all_1_colour (self, blue, green, red):    
	for i in range(no_LEDs):            #cycle through the whole LED buffer
	  LED_list[i] = [blue, green, red]  #upade LED buffer with BGR data
  
  #sets rainbow colours to LED buffer
  def set_rainbow (self, lenght=1):    
	count = 1
	pos = 0
	for i in range(no_LEDs):           #cycle through the LED buffer
	  LED_list[i] = rainbow_list[pos]  #udate the LED buffer with colour
	  if count == lenght :	           #cycle though all the rainbow colours
		pos += 1
		count = 0
	  count +=1
	  if pos > 5 : pos = 0
  
  #rotates to the left all values in LED buffer
  def rotate_left (self):
    store_pixel = LED_list[no_LEDs-1]                           #store last pixel
    for i in range(no_LEDs-1,0,-1): LED_list[i] = LED_list[i-1] #move all pixls down buffer
    LED_list[0] = store_pixel	                                #write the stored pixel at beginning
  
  #rotates to the right all values in LED buffer
  def rotate_right (self):                                      
	store_pixel = LED_list[0]                                   #store first pixel
	for i in range(0, no_LEDs, 1): LED_list[i-1] = LED_list[i]  #move all pixel up the buffer
	LED_list[no_LEDs-1] = store_pixel                           #write stored pixl at the end
  
  #inserts a pixel into LED buffer  
  def insert_pixel(self, position, blue, green, red):    
	for i in range(position): LED_list[i] = LED_list[i+1]                 #move pixels before the insert down
	for i in range(no_LEDs-1, position, -1) : LED_list[i] = LED_list[i-1] #move pixels above insert up
	LED_list[position]=[blue, green, red]                                 #write the insert pixel
  
  #removes 2 pixels from LED biffer and added a pixel at beginning and end
  def remove_pixel (self, position, blue, green, red):    
	for i in range(position, 0, -1):LED_list[i] = LED_list[i-1]        #move all pixels below up
	for i in range(position, no_LEDs-1, 1):LED_list[i] = LED_list[i+1] #move all pixels above down
	LED_list[0] = [blue, green, red]                                   #write pixel at begining
	LED_list[no_LEDs-1] = [blue, green, red]                           #write pixel at end
	
 
  


 

	

