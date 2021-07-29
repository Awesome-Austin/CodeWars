import unittest

from BinarySearchTrees import Node, Tree, cost, make_min_tree


class BinaryTreeCreatr(unittest.TestCase):
    def test_equality_leaf(self):
        """Equality -- Leaf"""
        tree1 = Tree(Node('A'))
        tree2 = Tree(Node('A'))
        self.assertEqual(True, tree1 == tree2, "Failed tree equality")

    def test_Equality_BalancedTree(self):
        """Equality -- Balanced tree"""
        tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
        tree2 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
        self.assertTrue(tree1 == tree2, "Failed tree equality")

    def test_Equality_MissingSubtrees(self):
        """Equality -- Missing subtrees"""
        tree1 = Tree(Node('B'), None, Tree(Node('C')))
        tree2 = Tree(Node('B'), None, Tree(Node('C')))
        self.assertTrue(tree1 == tree2, "Failed tree equality")

    def test_Inequality_SingleNode(self):
        """Inequality -- Single node"""
        tree1 = Tree(Node('A'))
        tree2 = Tree(Node('B'))
        self.assertTrue(tree1 != tree2, "Failed tree inequality")

    def test_Inequality_BalancedTree(self):
        """Inequality -- Balanced tree"""
        tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
        tree2 = Tree(Node('B'), Tree(Node('A')), Tree(Node('D')))
        self.assertTrue(tree1 != tree2, "Failed tree inequality")

    def test_Inequality_MissingSubtrees(self):
        """Inequality -- Missing subtrees"""
        tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
        tree2 = Tree(Node('B'), None, Tree(Node('C')))
        self.assertTrue(tree1 != tree2, "Failed tree inequality")

    def test_Inequality_SameNodesDifferentStructure(self):
        """Inequality -- Same nodes, different structure"""
        tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
        tree2 = Tree(Node('A'), None, Tree(Node('C'), Tree(Node('B')), None))
        self.assertTrue(tree1 != tree2, "Failed tree inequality")

    def test_str_Leaf(self):
        """str -- Leaf"""
        self.assertEqual(str(Tree(Node('A'))), '[A]', 'Failed str')

    def test_str_BalancedTree(self):
        """str -- Balanced tree"""
        tree1 = Tree(Node('B'), Tree(Node('A')), Tree(Node('C')))
        tree2 = Tree(Node('F'), Tree(Node('E')), Tree(Node('G')))
        tree3 = Tree(Node('D'), tree1, tree2)

        test_cases = [
            (tree1, '[[A] B [C]]'),
            (tree2, '[[E] F [G]]'),
            (tree3, '[[[A] B [C]] D [[E] F [G]]]')
        ]

        for tree, ans in test_cases:
            s = str(tree)
            self.assertEqual(s, ans, f'Failed Str')

    def test_str_MissingSubtrees(self):
        """str -- Missing subtrees"""
        tree1 = Tree(Node('B'), None, Tree(Node('C')))
        tree2 = Tree(Node('F'), Tree(Node('E')), None)
        tree3 = Tree(Node('D'), tree1, tree2)
        tree4 = Tree(Node('F'), None, None)
        tree5 = Tree(Node('D'), tree1, tree4)

        test_cases = [
            (tree1, '[_ B [C]]'),
            (tree2, '[[E] F _]'),
            (tree3, '[[_ B [C]] D [[E] F _]]'),
            (tree4, '[F]'),
            (tree5, '[[_ B [C]] D [F]]'),
        ]

        for tree, ans in test_cases:
            s = str(tree)
            self.assertEqual(s, ans, f'Failed str')

    def test_extras(self):
        test1 = Tree(Node('IW'), Tree(Node('DG')), Tree(Node('SV'), Tree(Node('NI'), Tree(Node('KC'), Tree(Node('JT'), None, Tree(Node('JU'), None, Tree(Node('JZ')))), Tree(Node('NH'))), Tree(Node('RV'), Tree(Node('OS'), None, Tree(Node('PK'), None, Tree(Node('QC')))), None)), Tree(Node('TL'), Tree(Node('TB')), Tree(Node('YX'), Tree(Node('XU'), Tree(Node('WB'), Tree(Node('TX')), None), None), None))))
        test2 = Tree(Node('ZI'), Tree(Node('IW'), Tree(Node('DG')), Tree(Node('SV'), Tree(Node('NI'), Tree(Node('KC'), Tree(Node('JT'), None, Tree(Node('JU'), None, Tree(Node('JZ')))), Tree(Node('NH'))), Tree(Node('RV'), Tree(Node('OS'), None, Tree(Node('PK'), None, Tree(Node('QC')))), None)), Tree(Node('TL'), Tree(Node('TB')), Tree(Node('YX'), Tree(Node('XU'), Tree(Node('WB'), Tree(Node('TX')), None), None), None)))), None)

        ans2 = Tree(Node('HX'), Tree(Node('ES'), None, Tree(Node('GU'))), Tree(Node('NE'), Tree(Node('KV'), Tree(Node('KD')), Tree(Node('NA'), Tree(Node('MY'), Tree(Node('KW')), None), None)), Tree(Node('ZG'), Tree(Node('WN'), Tree(Node('QJ'), Tree(Node('PO'), Tree(Node('PB'), None, Tree(Node('PI'))), None), Tree(Node('VE'), Tree(Node('RH'), None, Tree(Node('SU'))), None)), Tree(Node('XC'))), Tree(Node('ZO')))))

        test_cases = [
            (test1, Tree(Node('ES'), None, Tree(Node('GU')))),
            (test2, ans2),
        ]

        for tree, ans in test_cases:
            self.assertNotEqual(tree, ans)


class BinaryTreeCost(unittest.TestCase):

    A = Node('A', 10)
    B = Node('B', 2)
    C = Node('C', 4)
    D = Node('D', 9)
    E = Node('E', 8)

    def test_cost_leaf(self):
        """cost -- leaf"""
        tree_a = Tree(self.A)
        self.assertEqual(cost(tree_a), 10)

    def test_cost_two_nodes(self):
        """cost -- two nodes"""

        test_cases = [
            (Tree(self.B, Tree(self.A), None), 22),
            (Tree(self.A, None, Tree(self.B)), 14),
        ]
        for tree, ans in test_cases:
            self.assertEqual(cost(tree), ans)

    def test_cost_three_nodes(self):
        """cost -- three nodes"""
        test_cases = [
            (Tree(self.B, Tree(self.A), Tree(self.C)), 30),
            (Tree(self.A, None, Tree(self.C, Tree(self.B), None)), 24)
        ]

        for tree, ans in test_cases:
            self.assertEqual(cost(tree), ans)

    def test_cost_five_nodes(self):
        """cost -- five nodes"""

        test_cases = [
            (Tree(self.C, Tree(self.B, Tree(self.A), None), Tree(self.E, Tree(self.D), None)), 81),
            (Tree(self.D, Tree(self.A, None, Tree(self.C, Tree(self.B), None)), Tree(self.E)), 65),
        ]
        for tree, ans in test_cases:
            self.assertEqual(cost(tree), ans)

    def test_make_min_tree(self):
        """Example Test Cases -- make_min_tree"""

        test_case = [
            ([self.A], '[A]'),
            ([self.A, self.B], '[_ A [B]]'),
            ([self.A, self.B, self.C], '[_ A [[B] C _]]'),
            ([self.A, self.B, self.C, self.D, self.E], '[[_ A [[B] C _]] D [E]]'),
        ]

        for node_list, ans in test_case:
            tree = make_min_tree(node_list)
            self.assertEqual(str(tree), ans)


if __name__ == '__main__':
    unittest.main()
