#!/usr/bin/env python3
"""Binary Search Tree"""


class TreeNode:
    """Binary Tree  Node"""

    def __init__(
        self,
        key,
        value,
        left=None,
        right=None,
        parent=None,
    ):
        self.key = key
        self.value = value
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def is_left_child(self):
        return (
            self.parent and self.parent.left_child is self
        )

    def is_right_child(self):
        return (
            self.parent and self.parent.right_child is self
        )

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_child(self):
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
                    successor = (
                        self.parent.find_successor()
                    )
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
        elif self.has_any_child():
            if self.left_child:
                if self.is_left_child():
                    self.parent.left_child = (
                        self.left_child
                    )
                else:
                    self.parent.right_child = (
                        self.left_child
                    )
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = (
                        self.right_child
                    )
                else:
                    self.parent.right_child = (
                        self.right_child
                    )
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


class BinarySearchTree:
    """Binary Search Tree"""

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

    def _put(self, key, value, current):
        if key < current.key:
            if current.left_child:
                self._put(key, value, current.left_child)
            else:
                current.left_child = TreeNode(
                    key, value, parent=current
                )
        else:
            if current.right_child:
                self._put(key, value, current.right_child)
            else:
                current.right_child = TreeNode(
                    key, value, parent=current
                )

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            result = self._get(key, self.root)
            if result:
                return result.value
        return None

    def _get(self, key, current):
        if not current:
            return None
        if current.key == key:
            return current
        if key < current.key:
            return self._get(key, current.left_child)
        return self._get(key, current.right_child)

    def __getitem__(self, key):
        return self.get(key)

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

    def __delitem__(self, key):
        self.delete(key)

    def _delete(self, current):
        if current.is_leaf():
            if current.is_left_child():
                current.parent.left_child = None
            else:
                current.parent.right_child = None
        elif current.has_children():
            # removing a node with two children
            successor = current.find_successor()
            successor.splice_out()
            current.key = successor.key
            current.value = successor.value
        else:  # removing a node with one child
            if current.left_child:
                if current.is_left_child():
                    current.left_child.parent = (
                        current.parent
                    )
                    current.parent.left_child = (
                        current.left_child
                    )
                elif current.is_right_child():
                    current.left_child.parent = (
                        current.parent
                    )
                    current.parent.right_child = (
                        current.left_child
                    )
                else:
                    current.replace_value(
                        current.left_child.key,
                        current.left_child.value,
                        current.left_child.left_child,
                        current.left_child.right_child,
                    )
            else:
                if current.is_left_child():
                    current.right_child.parent = (
                        current.parent
                    )
                    current.parent.left_child = (
                        current.right_child
                    )
                elif current.is_right_child():
                    current.right_child.parent = (
                        current.parent
                    )
                    current.parent.right_child = (
                        current.right_child
                    )
                else:
                    current.replace_value(
                        current.right_child.key,
                        current.right_child.value,
                        current.right_child.left_child,
                        current.right_child.right_child,
                    )
