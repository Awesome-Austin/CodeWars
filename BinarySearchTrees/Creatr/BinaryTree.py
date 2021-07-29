class Tree(object):

    def __init__(self, root, left=None, right=None):
        if not root and type(root) == Node:
            raise ValueError

        if left:
            if not type(left) == Tree and left.root < root:
                raise ValueError

        if right:
            if not type(right) == Tree and root < right.root:
                raise ValueError

        self.left = left
        self.root = root
        self.right = right

    def is_leaf(self):
        return not (self.left or self.right)

    def __str__(self):
        if self.is_leaf():
            return f'[{self.root}]'

        root = f'{self.root}'
        left = f'{"_" if self.left is None else self.left}'
        right = f'{"_" if self.right is None else self.right}'

        return f'[{left} {root} {right}]'

    def __repr__(self):
        class_ = self.__class__.__name__
        if self.is_leaf():
            return f"{class_}({repr(self.root)})"

        root = f'{class_}({repr(self.root)}'
        left = f'{"None" if self.left is None else repr(self.left)}'
        right = f'{"None" if self.right is None else repr(self.right)}'

        return f'{root}, {left}, {right})'

    def __eq__(self, other):
        try:
            if self.is_leaf() and other.is_leaf():
                return self.root == other.root
            else:
                return (self.left == other.left) and (self.right == other.right)
        except AttributeError:
            return False

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.root.value < other.root.value

    def __gt__(self, other):
        return self.root.value > other.root.value


class Node(object):

    def __init__(self, value, weight=1, show_weight_in_str=False):
        self.value = value
        self.weight = weight
        self.show_weight_in_str = show_weight_in_str

    def __str__(self):
        return '{v}{w}'.format(
            v=str(self.value),
            w=f":{self.weight}" if self.show_weight_in_str else ""
        )

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __repr__(self):
        return "{class_}('{value}'{weight}{show_weight})".format(
            class_=self.__class__.__name__,
            value=self.value,
            weight=f', {str(self.weight)}' if self.weight > 1 else '',
            show_weight=f', {str(self.show_weight_in_str)}' if self.show_weight_in_str else '',
        )

