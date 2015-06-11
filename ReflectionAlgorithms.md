# Introduction #

Detecting the reflection of a finger is the key innovation in ShinyTouch that allows it to capture the position and depth of the finger with one camera.

# Details #

The prototype reference implementation of the concept implements several detectors for the reflection.

  * RGB Color Range - this is the simplest, most primitive, provides semi-decent results but requires extensive manual calibration
  * Variable Color Range - the above with a color range that changes based on the horizontal location, also primitive, not that good and requires even more manual calibration
  * Color Ratios - This is the beginning of the "modern" shinytouch. It uses 3 points, from the target (finger), reflection (well, potential reflection), and background (a few pixels above the finger). it uses a fixed ratio to mix BG with Target and compares that to the color of the reflection.
  * Reverse Color Ratio - Calculate the color ratio from the BG, Target and Reflection and see if it fits the range
  * BG vs Reflection - a simple comparison between the color of the Reflection and the BG to see if its under a threshold
  * Hue Compare - In a sort of theoretical regression, it switched to comparing the color of the BG vs the reflection but this time it worked better because it compared hue rather than RGB
  * Shape Tracking. The new and likely most complicated, least configurable (thats a good thing, and the terminology i used is strange) and provides some really quite good results.