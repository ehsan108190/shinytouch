# Introduction #

So ShinyTouch steals from tons of things (mostly hopefully legally), and without those the project could not exist beyond a scribble on a napkin with the pencil I always carry in my right pocket.


### Python ###
Yay! Python! Great language, but sadly it's quite slow with real time image processing (hmm.. who would know that using a _scripting_ language is bad for fast processing?)

### Python Imaging Library ###
Yes, so I'm using PIL just to read pixel data from the webcam. It's a pretty large under-use, and probably why I can only squeeze 29fps with a 60fps PS3 eye on a 3.0ghz Core 2 Duo

### PyGame ###
I can't find anything easier to use than pygame, so I'll use it.

### Wii Whiteboard ###
Not johnny lee's C# one, but a port to python on sourceforge. Specifically Perspective.py and Mousecontrol.py (the latter of which is unneessary since it can be accomplished due to the TUIO protocol support) and using apps like TUIOmouse.

### Open Sound Control ###
This is used to support the communications protocol that powers TUIO support.

### TUIOtouch ###
While it doesn't use any code from TUIOtouch anymore, the TUIO system that I wrote is based off looking at it.

### OpenCV ###
Despite the powerfulness of OpenCV, I'm just using it to get webcam data. It's such an astounding underuse of the library, but I'm trying to keep the project as portable and in a sense, low-level as possible. Also, for more cross-platform-icity.

### VideoCapture ###
For windows, VideoCapture usually works better than OpenCV (on linux, there is no VideoCapture). So you can use this to get webcam data instead as it's probably lighter and better.