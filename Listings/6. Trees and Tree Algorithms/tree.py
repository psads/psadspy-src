#!/usr/bin/env python3
"""Binary Tree"""

import os
import sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)


my_tree = [
    "a",  # root
    ["b", ["d", [], []], ["e", [], []]],  # left subtree
    ["c", ["f", [], []], []],  # right subtree
]

my_tree = ["a", ["b", ["d", [], []], ["e", [], []]], ["c", ["f", [], []], []]]
# print(my_tree)
# print("left subtree = ", my_tree[1])
# print("root = ", my_tree[0])
# print("right subtree = ", my_tree[2])


def make_binary_tree(root):
    return [root, [], []]


def insert_left(root, new_child):
    old_child = root.pop(1)
    if len(old_child) > 1:
        root.insert(1, [new_child, old_child, []])
    else:
        root.insert(1, [new_child, [], []])
    return root


def insert_right(root, new_child):
    old_child = root.pop(2)
    if len(old_child) > 1:
        root.insert(2, [new_child, [], old_child])
    else:
        root.insert(2, [new_child, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_value):
    root[0] = new_value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


# a_tree = make_binary_tree(3)
# insert_left(a_tree, 4)
# insert_left(a_tree, 5)
# insert_right(a_tree, 6)
# insert_right(a_tree, 7)
# left_child = get_left_child(a_tree)
# print(left_child)

# set_root_val(left_child, 9)
# print(a_tree)
# insert_left(left_child, 11)
# print(a_tree)
# print(get_right_child(get_right_child(a_tree)))


class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child

    def insert_right(self, new_node):
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child
            self.right_child = new_child

    def get_root_val(self):
        return self.key

    def set_root_val(self, new_obj):
        self.key = new_obj

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child

    def preorder(self):
        print(self.key, end=" ")
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()


# a_tree = BinaryTree("a")
# print(a_tree.get_root_val())
# print(a_tree.get_left_child())
# a_tree.insert_left("b")
# print(a_tree.get_left_child())
# print(a_tree.get_left_child().get_root_val())
# a_tree.insert_right("c")
# print(a_tree.get_right_child())
# print(a_tree.get_right_child().get_root_val())
# a_tree.get_right_child().set_root_val("hello")
# print(a_tree.get_right_child().get_root_val())
# a_tree.preorder()
# print()


def build_tree():
    tree = BinaryTree(None)
    tree.set_root_val("a")
    tree.insert_left("b")
    tree.insert_right("c")
    tree.get_left_child().insert_right("d")
    tree.get_right_child().insert_left("e")
    tree.get_right_child().insert_right("f")
    return tree


# ttree = build_tree()

# assert ttree.get_right_child().get_root_val() == "c"
# assert ttree.get_left_child().get_right_child().get_root_val() == "d"
# assert ttree.get_right_child().get_left_child().get_root_val() == "e"


from pythonds3.basic import Stack
from pythonds3.trees import BinaryTree


def build_parse_tree(fp_expr):
    fp_list = fp_expr.split()
    p_stack = Stack()
    expr_tree = BinaryTree("")
    p_stack.push(expr_tree)
    current_tree = expr_tree

    for i in fp_list:
        if i == "(":
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.left_child

        elif i in ["+", "-", "*", "/"]:
            current_tree.root = i
            current_tree.insert_right("")
            p_stack.push(current_tree)
            current_tree = current_tree.right_child

        elif i == ")":
            current_tree = p_stack.pop()

        elif i not in ["+", "-", "*", "/", ")"]:
            try:
                current_tree.root = int(i)
                parent = p_stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return expr_tree


# pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
# pt.postorder()  # defined and explained in the next section
# print()

# from contextlib import redirect_stdout
# import io

# f = io.StringIO()
# with redirect_stdout(f):
#     pt.postorder()
# assert f.getvalue() == "10 5 + 3 * "

import operator


def evaluate(parse_tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    left_child = parse_tree.left_child
    right_child = parse_tree.right_child

    if left_child and right_child:
        fn = operators[parse_tree.root]
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.root


# print(evaluate(pt))

# pt = build_parse_tree("( 3 + ( 4 * 5 ) )")
# assert evaluate(pt) == 23
# assert pt.postorder_eval() == 23


def preorder(tree):
    if tree:
        print(tree.get_root_val())
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())


def inorder(tree):
    if tree:
        inorder(tree.get_left_child())
        print(tree.get_root_val())
        inorder(tree.get_right_child())


def postorder(tree):
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.get_root_val())


# preorder(pt)


def postordereval(tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }
    result_1 = None
    result_2 = None
    if tree:
        result_1 = postordereval(tree.get_left_child())
        result_2 = postordereval(tree.get_right_child())
        if result_1 and result_2:
            return operators[tree.get_root_val()](result_1, result_2)
        else:
            return tree.get_root_val()


# assert postordereval(pt) == 23


def print_exp(tree):
    result = ""
    if tree:
        result = "(" + print_exp(tree.get_left_child())
        result = result + str(tree.get_root_val())
        result = result + print_exp(tree.get_right_child()) + ")"
    return result


# print(print_exp(pt))


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, value):
        if self.root:
            self._put(key, value, self.root)
        else:
            self.root = TreeNode(key, value)
        self.size = self.size + 1

    def _put(self, key, value, current_node):
        if key < current_node.key:
            if current_node.left_child:
                self._put(key, value, current_node.left_child)
            else:
                current_node.left_child = TreeNode(
                    key, value, parent=current_node
                )
        else:
            if current_node.right_child:
                self._put(key, value, current_node.right_child)
            else:
                current_node.right_child = TreeNode(
                    key, value, parent=current_node
                )

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value
        return None

    def _get(self, key, current_node):
        if not current_node:
            return None
        if current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return bool(self._get(key, self.root))

    def delete(self, key):
        if self.size > 1:
            node_to_remove = self._get(key, self.root)
            if node_to_remove:
                self._delete(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError("Error, key not in tree")

    def _delete(self, current_node):
        if current_node.is_leaf():  # removing a leaf
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_children():  # removing a node with two children
            successor = current_node.find_successor()
            successor.splice_out()
            current_node.key = successor.key
            current_node.value = successor.value
        else:  # removing a node with one child
            if current_node.left_child:
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_value(
                        current_node.left_child.key,
                        current_node.left_child.value,
                        current_node.left_child.left_child,
                        current_node.left_child.right_child,
                    )
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_value(
                        current_node.right_child.key,
                        current_node.right_child.value,
                        current_node.right_child.left_child,
                        current_node.right_child.right_child,
                    )

    def __delitem__(self, key):
        self.delete(key)


class TreeNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def is_left_child(self):
        return self.parent and self.parent.left_child is self

    def is_right_child(self):
        return self.parent and self.parent.right_child is self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_a_child(self):
        return self.right_child or self.left_child

    def has_children(self):
        return self.right_child and self.left_child

    def replace_value(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        if self.left_child:
            self.left_child.parent = self
        if self.right_child:
            self.right_child.parent = self

    def find_successor(self):
        successor = None
        if self.right_child:
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor

    def find_min(self):
        current = self
        while current.left_child:
            current = current.left_child
        return current

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_a_child():
            if self.left_child:
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def __iter__(self):
        if self:
            if self.left_child:
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.right_child:
                for elem in self.right_child:
                    yield elem


# my_tree = BinarySearchTree()
# my_tree["a"] = "a"
# my_tree["q"] = "quick"
# my_tree["b"] = "brown"
# my_tree["f"] = "fox"
# my_tree["j"] = "jumps"
# my_tree["o"] = "over"
# my_tree["t"] = "the"
# my_tree["l"] = "lazy"
# my_tree["d"] = "dog"

# print(my_tree["q"])
# print(my_tree["l"])
# print("There are {} items in this tree".format(len(my_tree)))
# my_tree.delete("a")
# print("There are {} items in this tree".format(len(my_tree)))

# for node in my_tree:
#     print(my_tree[node], end=" ")
# print()

# assert my_tree["a"] == None
# assert my_tree["b"] == "brown"
# assert len(my_tree) == 8

