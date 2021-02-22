# Clock for 2x16 LCD 
## Raspberry Pi or equivalent

This is a very simple script to output the current date and time on a 2 by 16 lcd panel.  
It also blanks the LCD between 11pm and 5am. 
```
if mytime.tm_hour < 6 or mytime.tm_hour > 22:
```

To automatically update, it can be run as a cron job that updates every minute, from the root user. 

```
m h dom mon dow   command
* * *   *   * 	  python3 /foo/bar/lcdout.py
```