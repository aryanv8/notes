A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.

![Perfect Binary Tree](https://cdn.programiz.com/sites/tutorial2program/files/perfect-binary-tree_0.png "Perfect Binary Tree")

Perfect Binary Tree

All the internal nodes have a degree of 2.

Recursively, a perfect binary tree can be defined as:

1. If a single node has no children, it is a perfect binary tree of height `h = 0`,
2. If a node has `h > 0`, it is a perfect binary tree if both of its subtrees are of height `h - 1` and are non-overlapping.

![Perfect Binary Tree (Recursive Representation)](https://cdn.programiz.com/sites/tutorial2program/files/perfect-binary-tree-rec.png "Perfect Binary Tree")

Perfect Binary Tree (Recursive Representation)

---


The following code is for checking whether a tree is a perfect binary tree.
```python
# Check if the tree is perfect binary tree
def is_perfect(root, d, level=0):
    # Check if the tree is empty
    if (root is None):
        return True
    # Check the presence of trees
    if (root.left is None and root.right is None):
        return (d == level + 1)
    if (root.left is None or root.right is None):
        return False
    return (is_perfect(root.left, d, level + 1) and
            is_perfect(root.right, d, level + 1))
```

1. A perfect binary tree of height h has $2^{h + 1} – 1$ node.
2. A perfect binary tree with n nodes has height `log(n + 1) – 1 = Θ(ln(n))`.
3. A perfect binary tree of height h has `2^h` leaf nodes.
4. The average depth of a node in a perfect binary tree is `Θ(ln(n))`.


