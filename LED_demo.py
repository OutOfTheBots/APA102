from LED import Super_LED
import time

LED = Super_LED(100)

LED.set_brightness(1)

LED.set_rainbow(5)
#LED.set_2_colour(10, 0,0,255, 255,0,0)
LED.refreash_LED()

for blah in range (2):
  for i in range (40):   
   LED.rotate_left()
   LED.refreash_LED()

  for i in range (40):   
   LED.rotate_right()
   LED.refreash_LED()
   
for blah in range (2):
 for i in range(5,30,1):
  LED.set_rainbow(i)
  LED.refreash_LED()
  time.sleep(0.1)

 for i in range(30,5,-1):
  LED.set_rainbow(i)
  LED.refreash_LED()
  time.sleep(0.1)
  
LED.set_all_1_colour(255,0,0)
LED.refreash_LED()

for blah in range(5):
 for i in range(20):
  LED.insert_pixel(50,0,0,255)
  LED.refreash_LED()
 for i in range(20):
  LED.insert_pixel(50,0,255,255)
  LED.refreash_LED()
 for i in range(20):
  LED.insert_pixel(50,255, 0, 200)
  LED.refreash_LED()
 for i in range(20):
  LED.insert_pixel(50,0, 100, 255)
  LED.refreash_LED()

for i in range(1,255,2):
  LED.set_all_1_colour(i,0,255-i)
  LED.refreash_LED()

for blah in range(3):
 for i in range(1,255,3):
  LED.set_all_1_colour(i,0,255-i)
  LED.refreash_LED()
 for i in range(1,255,3):
  LED.set_all_1_colour(255-i,i, 0)
  LED.refreash_LED() 
 for i in range(1,255,3):
  LED.set_all_1_colour(0,255-i, i)
  LED.refreash_LED() 
LED.set_2_colour(10,255,0,0,0,0,255)
wait = 0.4
for blah2 in range(3):
 for i in range(20):
  for blah in range (10):
   LED.rotate_right()
  LED.refreash_LED()
  time.sleep(wait)
  wait -= 0.018
 for i in range(20):
  for blah in range (10):
   LED.rotate_right()
  LED.refreash_LED()
  time.sleep(wait)
  wait += 0.018    
LED.set_all_1_colour(0,0,255)
LED.refreash_LED()

for blah in range (3):
 for i in range(20):
   LED.insert_pixel(50,0,255,0)
   LED.refreash_LED()
 for i in range(20):
   LED.remove_pixel(50,0,255,0)
   LED.refreash_LED()
 for i in range(20):
   LED.insert_pixel(50,0, 255, 255)
   LED.refreash_LED()
 for i in range(20):
   LED.remove_pixel(50,0,255,255)
   LED.refreash_LED()
 for i in range(20):
   LED.insert_pixel(50,255,0,0)
   LED.refreash_LED()
 for i in range(20):
   LED.remove_pixel(50,255,0,0)
   LED.refreash_LED()
 for i in range(20):
   LED.insert_pixel(50,255, 0, 200)
   LED.refreash_LED()
 for i in range(20):
   LED.remove_pixel(50,255,0,200)
   LED.refreash_LED()   
 for i in range(20):
   LED.insert_pixel(50,0, 100, 255)
   LED.refreash_LED()
 for i in range(20):
   LED.remove_pixel(50,0,100,255)
   LED.refreash_LED()  

LED.set_rainbow(10)
LED.refreash_LED()
for blah in range (5):
 for i in range (32):
  LED.set_brightness(i)
  LED.refreash_LED()
  time.sleep(0.05)
 for i in range (31,-1,-1):
  LED.set_brightness(i)
  LED.refreash_LED()
  time.sleep(0.05) 
   
LED.set_all_1_colour(0,0,0)
LED.refreash_LED()
