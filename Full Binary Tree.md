A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no children. It is also known as **a proper binary tree**.
![[Pasted image 20230728115955.png]]
```
Let, i = the number of internal nodes
      n = be the total number of nodes
     l = number of leaves
    λ = number of levels
```
1. The number of leaves is `i + 1`.
2. The total number of nodes is `2i + 1`.
3. The number of internal nodes is (n – 1) / 2.
4. The number of leaves is `(n + 1) / 2`.
5. The total number of nodes is `2l – 1`.
6. The number of internal nodes is `l – 1`.
7. The number of leaves is at most $2^λ - 1$.

```python
# Checking full binary tree
def isFullTree(root):

    # Tree empty case
    if root is None:
        return True

    # Checking whether child is present
    if root.leftChild is None and root.rightChild is None:
        return True

    if root.leftChild is not None and root.rightChild is not None:
        return (isFullTree(root.leftChild) and isFullTree(root.rightChild))

    return False
```