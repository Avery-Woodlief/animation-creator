# Welcome to the Animator Creator!

This program allows you to easily create complex or quirky animations without heavy computation!

This project is still in development, so please be patient for future updates. Thank you :)

To run the program, make sure to go into the 'settings/' folder and do 'python3 config.py' to intit the config.json file

There are two `.json` files that the Animator Creator makes:

- `abstract_motion.json`
- `raw.json`

`raw.json` simply uses the points selected in the Animator Creator, while `abstract_motion.json` uses the *sum of changes* in the coordinates up to that point.

What this means is that with `abstract_motion.json`, you can place the animation anywhere on the screen for some object.

## How to use `abstract_motion.json`

1. Let the object have a starting position.

Suppose the starting position is:

$$
P = (x_0, y_0)
$$

2. After the `.json` file is imported, each element in the list tells where $P$ needs to go relative to $P$ for that step.

For the first step, call it:

$$
S_1 = (dx, dy)
$$

then for the object to go from P to the first step, just add them together!

To execute the animation at each step, compute:

$$
P + S_i
$$

for the $i^{th}$ step of the animation, but do **not** change the value of $P$.

That is how you use `abstract_motion.json`!

<br>

## **How the files are calculated**

Given a `raw.json` file with a list of positions for the animation:

$$
Q_0, Q_1, Q_2, \dots, Q_N
$$

where each:

$$
Q_i := (x_i, y_i)
$$

`abstract_motion.json` is a list of 2-element lists:

$$
(dx_i, dy_i)
$$

where:

$$
dx_i := (x_1 - x_0) + (x_2 - x_1) + \dots + (x_i - x_{i-1}) = x_i - x_0
$$

and:

$$
dy_i := (y_1 - y_0) + (y_2 - y_1) + \dots + (y_i - y_{i-1}) = y_i - y_0
$$
