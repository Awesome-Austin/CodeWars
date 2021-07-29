# Binary Search Trees

A Tree consists of a root, which is of type `Node`, and possibly a left subtree of type `Tree` and possibly a right subtree of type `Tree`.

If the left subtree is present, then all its nodes are less than the parent tree's root and if the right tree is present, then all its nodes are greater than the parent tree's root.

In this kata, classes `Tree` and `Node` have been provided.

However, the methods `__eq__`, `__ne__`, and `__str__` are missing from the Tree class.

Your job is to provide the implementation of these methods.

The example test cases should provide enough information to implement these methods correctly.

## Example
As an illustrative example, here is the string representation of a tree that has two nodes, `B` at the root and `C` at the root of the right subtree.

The left subtree is missing and the right subtree is a leaf, i.e., has no subtrees:

    '[_ B [C]]'

This tree is obtained by evaluating the following expression:

    Tree(Node('B'), None, Tree(Node('C'))))

Notice in particular that:
* when one subtree, but not both, is missing, an underscore is in its place
* a single space separates the root node from the subtrees
* when both subtrees are missing, the root node is enclosed in brackets.
