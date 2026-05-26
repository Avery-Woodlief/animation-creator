Welcome to the Animator Creator!
This program allows you to easily create complex or quirky animations without the use of the computation!
This project is still in developement, so please be patient for future updates, thank you :)
There are two files that the Animation Creator makes for an animation (.json) and they are:
"abstract_motion.json" and "raw.json"
"raw.json" simply uses the points selected in the Animator Creator while "abstract_motion.json" uses the changes in the coordinates.
What this means is that with "abstract_motion.json", you can put the animation anywhere on the screen for some object.
How to use "abstract_motion.json":
 1) Let the object have a starting position.
suppose the starting position is $P = (x_0, y_0)$.
 2) After the .json file is imported, each element in the list tells where P needs to go, relative to P.
That is, for the first step, call it $S_1 = (ddx, ddy)$, just add them together!
To execute the animation just do $P + S_i$ for the $i^{th}$ step of the animation, but do not change the value of P!
That is how you use the "abstract_motion.json"!
=================================================================================================================
How the files are calculated:
Given a "raw.json" file with a list of positions (for the animation), Q0, Q1, Q2, ..., QN each being equal to (xi, yi) where i is the position in the list.
"abstract_motion.json" is a list of 2 element lists, call them (ddxi, ddyi).
ddxi := (x1 - x0) + (x2 - x1) + ... + (xi - x_{i - 1})
ddyi := (y1 - y0) + (y2 - y1) + ... + (yi - y_{i - 1}), where the xi, yi are the coordinates for the point Qi in "raw.json"
