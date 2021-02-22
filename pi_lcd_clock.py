from RPLCD.i2c import CharLCD
import datetime
import time

date = datetime.datetime.now()
date = date.strftime("|(:%a %b %d:)||=--%I:%M %p--=|")

mytime = time.localtime()
if mytime.tm_hour < 6 or mytime.tm_hour > 22:
        
    off  = CharLCD(i2c_expander='PCF8574', address=0x3f, port=1, backlight_enabled=False)
    off.close()
       # print ('It is night-time')
else:
    lcd = CharLCD(i2c_expander='PCF8574', address=0x3f, port=1,
              cols=16, rows=2, dotsize=8,
              auto_linebreaks=True)
    lcd.write_string(date)
        #print ('It is day-time')

    lcd.close()
