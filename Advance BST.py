# Finding Max & Min Depth of Binary Tree
# Finding Least Common Ancestor of BST (with Inorder walk)

import sys
import time
import random
import math

# # total arguments
# n = int(sys.argv[1000])
# print("The number of elements is :", n )

var = (sys.getrecursionlimit())
sys.setrecursionlimit(10000000)


file = open("numbers.txt","r")
re = file.readlines()
arr_numbers = []

for line in re:
    arr_numbers.append(int(line.rstrip()))
# print(arr_numbers)


class Node:
    def __init__(self, key=None, left=None, right=None, parent=None):
        self.key = key
        self.left = left
        self.parent = parent
        self.right = right


class Binary_Search_Tree:
    def __init__(self):
        self.root = None

    def insertion(self, root, val):
        if root == None:
            self.root = Node(key=val)
        else:
            if val > root.key:
                if root.right == None:
                    root.right = Node(key=val, parent=root)
                else:
                    self.insertion(root.right, val)

            elif val < root.key:
                if root.left == None:
                    root.left = Node(key=val, parent=root)
                else:
                    self.insertion(root.left, val)
            else:
                print("Value already exist")

    def printTree(self, root):
        if root is None:
            return
        q = []
        q.append(root)
        while q:
            count = len(q)
            while count > 0:
                temp = q.pop(0)
                if temp.key == None:
                    print(None, end=' ')
                else:
                    print(temp.key, end=' ')
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                count -= 1
            print('')

    def minDepth(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        if root.left == None:
            return bi.minDepth(root.right) + 1
        if root.right == None:
            return bi.minDepth(root.left) + 1

        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1


    def maxDepth(self, root):
        if root == None:
            return 0
        l_height = self.maxDepth(root.left)
        r_height = self.maxDepth(root.right)

        if (l_height > r_height):
            return l_height + 1
        else:
            return r_height + 1


def findLCA(root, n1, n2):

    if root is None:
        return None

    if root.key == n1 or root.key == n2:
        return root

    left_lca = findLCA(root.left, n1, n2)
    right_lca = findLCA(root.right, n1, n2)

    if left_lca and right_lca:
        return root

    return left_lca if left_lca is not None else right_lca


# Driver program to test above function
bi = Binary_Search_Tree()
for i in arr_numbers:
    bi.insertion(bi.root, i)
print('\nIn-order Tree Walk ::')
bi.printTree(bi.root)


print('\n{:<20} {}'.format('Minimum Depth of BST :', bi.minDepth(bi.root)))
print('{:<20} {}'.format('Maximum Depth of BST :', bi.maxDepth(bi.root)))


l, m = map(int, input('Enter nodes with single space in between them : ').split())
lca = findLCA(bi.root,l,m).key
print('Least Common Ancestor for given Nodes :',lca,'\n')