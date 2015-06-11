# Introduction #

there are a few simple guidelines for placing a webcam on the monitor. This depends on numerous factors including screen width, camera resolution, monitor gloss factor, and intended accuracy/precision.


# Details #

For the ShinyTouch system, accuracy (the rate of determining correctly a touch event) is inversely proportional to precision (here, it's described as the described as the resolution of the touch surface, especially for horizontal resolution). (it's actually closer to a cosine/sine relationship, but ShinyTouch is yet to attain such meticulous models of the situations it exists in and only uses linear approximations of various effects).

Increasing the distance of the webcam from the monitor decreases the angle of incidence, and increasing shyness, yet simultaneously decreasing the horizontal and vertical resolution of the image of the surface.

The most important aspect of the ShinyTouch system is the angle of which the camera is positioned at the monitor. I use the angle measurement as the angle from the very edge (closest to the webcam) of the surface. If the monitor is matte, the angle must be considerably closer to 0, while if it is extremely glossy, then the angle can be significantly higher. There is generally no limit to how shiny it can be to be acceptable, however if it is too reflective, the algorithm might confuse the reflection for the finger, and if so, then consider increasing the angle to compensate and make them effectively distinguishable.

# Summary #
This is a general summary fo the correlations and advice.
  * The angle of the point of contact and webcam is correlated with the shinyness
  * ShinyTouch exploits shinyness
  * Surfaces must be sufficiently shiny, most are
  * The distance of the webcam from the intended event surface correlates directly with shinyness
  * If things are too shiny and the algorithm confuses the reflection for the target, consider increasing the angle
  * If the surface is not shiny enough, consider adding a thin acrylic sheet over it, or some other shiny, transparent material.