# Introduction #

Currently it's only been tested on Ubuntu Linux 9.04 64bit (Intel Core 2 Duo) with a Sony Playstation 3 Eye. It currently requires pygame, PIL, and opencv. There is only very basic calibration features, and is _very_ involved. At this stage it requires a lot of software-side setup work involving a lot of code editing. Hardware setup is very simple though.

# Hardware #

Mount the camera off to the side of the monitor. I have only tested with the monitor mounted 13 inches from the monitor elevated 9.5 inches from the desk with the monitor (actual LCD part) at 5 inches from the desk. The software currently assumes that the two left and right sides of the monitor are parallel and this is only possible if the webcam is mounted to be as high as half of the monitor.

It should be at a steep angle, usually beyond the monitor's usual intended viewing angle to invoke shinyness. But not directly to the side of the monitor or else there will be not enough information on the horizontal axis. With my setup, it is at roughly a 20-35 deg angle.

# Code #

The two main functions to edit are colorTargetMatch() and colorReflectionDiff. The first function is relating to the color range of your finger. Take a snapshot from the webcam (I use Gnome Cheese to take a snapshot) and open it in an image editor to extract a RGB color range of your finger. Insert the range to the colorTargetMatch function.

From this point you can attempt running the application (see Runtime for monitor configuration information). Likely when running, it will recognize your finger with a row of green dots and a red dot to the side. If the dots do not appear, reexamine the color ranges. Touch the screen and then right click on the screen as it should give you a dump on the discovered reflection diff (if the data does not appear, try again or check your color ranges). Include those numbers into the colorReflectionDiff range.

Eventually it should form a green box around the fingertips when it is touching and just have the dots if it's hovering. Adjust the ranges until it works most of the time.

# Runtime #
When running the application, it needs to be configured to the position of the webcam. This is somewhat straightforward. Follow the instructions from the command line and press the c key. Then click the top left corner of the monitor (the glowing screen part), then the bottom left, bottom right and finally top right. After that the command line will give you a block of code that you can copy and paste over the similar looking variable declarations (under colorReflectionDiff() ). This is not necessary, but will save you the hassle of recalibrating every time you launch the application.

# Usage #

Follow the directions.

# Sorry #
If you realize its not actually worth it, I'm sorry. I can't give your time back, but hey, I wasted all my time doing this too.