# Introduction #

A reflection should mirror (duh) the real image with the virtual image, even when the colors may be skewed or reduced. The pixels around the known position of the fingertip can be scanned to the left and right simultaneously and the size and position of each can be measured. The differences are summed and are compared.

# Difference Summing #
The basic difference summing algorithm would be something like |n-x| but it is not ideal in that a 2x size might only have a minute difference of ~5.

[r74](https://code.google.com/p/shinytouch/source/detail?r=74) uses a Ratio summing algorithm like |(n/x)-1|

Potential future versions may use a squared difference sum like |n-x|^2

other candidates are to ignore the absolute value and instead always keep the larger numeber on teh denominator or numerator.

# Auto Adjusting Center #

if the finger is at an angle too steep, there may not be 16 pixels to the immediate right of the known point of contact. The algorithm uses an automatic adjusting system for the search.

```
    fpeak = measureLength(x-xpix,fy)
    speak = measureLength(x+xpix,sy)
    flen =  fpeak+abs(measureLength(x-xpix,fy-1,yi=-1,smarty=-30))
    slen =  speak+abs(measureLength(x+xpix,sy-1,yi=-1,smarty=-30))
    
    newfy = fy + fpeak - (flen/2)
    newsy = sy + speak - (slen/2)
```