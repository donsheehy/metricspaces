===========
The Problem
===========


.. What is the problem you are trying to solve?

There are many cases where one would like to compute with metric spaces.
This library is designed to be lightweight and versatile.

The primary design goals are:

- It should handle both Euclidean metrics (via numpy) and those defined by a provided distance function.

- It should interface seamlessly with net-tree, cover tree, and greedy tree code among others.

- It should have support for data collection like counting distances computed.

- It should handle the caching of distances.

- It should be able to use approximate distances.

- It should support alternative distance comparison methods.

- It should cache upper and lower bounds on distances in settings where distance comparison suffices.

Not all of these features are currently implemented.
