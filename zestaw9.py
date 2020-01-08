
# Zadania 9.4 i 9.7

import unittest


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SingleList:
    def __init__(self, *arguments):
        self.__length = 0
        self.head = None
        self.tail = None
        for item in arguments:
            self.insert_head(item)

    def is_empty(self):
        return self.__length == 0

    def count(self):
        return self.__length

    def insert_head(self, data):
        node = Node(data)
        if self.__length == 0:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.__length = self.__length + 1

    def insert_tail(self, data):
        node = Node(data)
        if self.__length == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.__length = self.__length + 1

    def remove_head(self):
        if self.__length == 0:
            raise Exception("pusta lista")
        node = self.head
        self.head = self.head.next
        self.__length = self.__length - 1
        if self.__length == 0:
            self.tail = None
        return node.data

    def __repr__(self):
        p = self.head
        whole_list = str(p)
        while p.next is not None:
            p = p.next
            whole_list += " -> " + str(p)
        return whole_list
#do klasy SingleList dodać metodę reverse(), która odwraca kolejność elementów w liście
    def reverse(self):
        curr = self.head
        prev = None
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

class TreeNode:

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self, *val: int):
        try:
            self.root = TreeNode(val[0])
            self.root.left = TreeNode(val[2])
            self.root.right = TreeNode(val[3])
            self.root.left.left = TreeNode(val[4])
            self.root.left.right = TreeNode(val[5])
            self.root.right.left = TreeNode(val[6])
            self.root.right.right = TreeNode(val[7])
            self.root.right.right.right = TreeNode(val[8])
        except IndexError: pass

    def print_tree(self):
        def btree_print_indented(top, level=0):
            if top is None:
                return
            btree_print_indented(top.right, level + 1)
            print("%s* %s" % ('   ' * level, top))
            btree_print_indented(top.left, level + 1)

        btree_print_indented(self.root, 20)

    def __get_leaves(self):
        stack = list()
        leaves = []
        sum_nodes_data = 0

        top = self.root
        stack.append(top)
        while stack:
            node = stack.pop()
            sum_nodes_data += node.data
            if node.right or node.left:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
            else:
                leaves.append(node.data)
        return leaves, sum_nodes_data

    def calc_total(self):
        return self.__get_leaves()[1]

    def count_leafs(self):
        return len(self.__get_leaves()[0])

    def count_total(self):
        return sum(self.__get_leaves()[0])


class TestListAndTree(unittest.TestCase):
    def setUp(self):
        self.l = SingleList(2, 4, 5, 7, 2, 3, 34, 22, 11)
        self.t1 = Tree(1, 2, 5, 7, 9, 77, 23, 56, 89)
        self.t2 = Tree(99,33,5,1,2,7)

    def test_reverse(self):
        self.assertTrue(self.l.head.data == 11)
        self.l.reverse()
        self.assertTrue(self.l.head.data == 2)
        self.assertTrue(str(self.l) in "2 -> 4 -> 5 -> 7 -> 2 -> 3 -> 34 -> 22 -> 11")

    def test_tree(self):
        self.assertEqual(self.t1.count_leafs(), 4)
        self.assertEqual(self.t1.count_total(), 198)
        self.assertEqual(self.t1.calc_total(), 267)
        self.assertEqual(self.t2.count_leafs(), 3)
        self.assertEqual(self.t2.count_total(), 10)

if __name__ == '__main__':
    unittest.main()