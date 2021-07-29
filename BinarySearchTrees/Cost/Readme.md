# Minimal Cost Binary Search Trees

The description that follows presumes that you have completed [Binary Search Trees](http://www.codewars.com/kata/binary-search-trees).

Before starting on this kata, fill in the code for Tree's `__eq__`, `__ne__`, and `__str__` methods as described and verified by that kata.

Imagine you have a binary search tree and after some time you notice that some of the nodes are accessed more frequently than others. 

The time it takes to access a node depends on how deep the node is in the tree, so ideally you would want nodes that are accessed often placed close to the root.

The purpose of the this kata is to "balance" the tree such that the average cost of accessing nodes is minimized.

Each node has a weight attribute which could represent how often the node is accessed.
 - For each node in a tree, one can associate a cost, which is the weight of the node times its depth.
 - The depth of the `root` node is defined to be `1`, and the depth of a node directly below a node of depth `d` is `d + 1`.
 - The cost of a tree is simply the sum of the costs of its nodes.

## Challenge 
### Part 1
Your first task is to write a function `cost` that takes a tree as argument and returns the cost of the tree.

### Part 2
Now we are getting to the more challenging part of this kata.

Your final task is to write a function `make_min_tree` that takes a non-empty list of nodes as argument and returns a tree with minimal cost.

The list passed as argument is sorted in ascending order.

No two nodes in the list are equal (under the definition of "equal" provided by `__eq__` and `__ne__`).

For this last part, your code will be tested with lists up to a length of `100`.

#### Note:
My algorithm is quadratic in space and cubic in time, but I am not sure it cannot be done better.


## Ref
https://www.codewars.com/kata/571a7c0cf24bdf99a8000df5/python