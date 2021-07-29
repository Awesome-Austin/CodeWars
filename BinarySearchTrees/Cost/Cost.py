from BinarySearchTrees import Tree, Node

Node.show_weight_in_str = True


# def cost(tree, d=1):
#     def _cost(tree, d):
#         yield tree.root.weight, d
#         if tree.left:
#             yield from _cost(tree.left, d+1)
#         if tree.right:
#             yield from _cost(tree.right, d+1)
#     cost_ = _cost(tree, d)
#     cost__ = list()
#     for c in cost_:
#         cost__.append(c)
#     # cost_ = list(cost_)
#     costs___ = [w * d for w, d in cost__]
#     return sum(costs___)

def cost(tree, depth=1):
    if tree is None:
        return 0
    if tree.is_leaf():
        return tree.root.weight*depth
    return tree.root.weight*depth + cost(tree.left, depth+1) + cost(tree.right, depth+1)


# def cost(tree, d=1):
#     def _cost(tree, d=1):
#         root = [(tree.root.weight, d)]
#         left = list()
#         right = list()
#         if tree.left:
#             left += _cost(tree.left, d+1)
#         if tree.right:
#             right += _cost(tree.right, d+1)
#         return root + left + right
#     costs = _cost(tree, d)
#     return sum(w*d for w, d in costs)


def make_min_tree(nodes: list):
    def _place_trees(*trees):
        left, right = sorted(trees)
        if cost(left) > cost(right):
            if left.right:
                right = _place_trees(left.right, right)
            left.right = right
            return left

        else:
            if right.left:
                left = _place_trees(right.left, left)
            right.left = left
            return right

    nodes = sorted(nodes, key=lambda x: x.value)

    tree = Tree(nodes.pop())

    while nodes:
        tree = _place_trees(Tree(nodes.pop()), tree)

    return tree


if __name__ == '__main__':
    test_cases = [
        (
            [Node('AOV', 29377), Node('AQV', 75771), Node('BBK', 69571), Node('BDD', 31658),
             Node('BDJ', 79852), Node('BIL', 73611), Node('BPS', 57459), Node('BWD', 42192),
             Node('CHO', 8712), Node('CSU', 92026), Node('CVB', 27584), Node('CWX', 24683),
             Node('CXR', 59412), Node('DDK', 58004), Node('DQT', 167), Node('DSQ', 918),
             Node('DSY', 22063), Node('ERF', 46178), Node('FDL', 90509), Node('FMH', 47300),
             Node('FOR', 95942), Node('FOS', 30050), Node('GSZ', 92926), Node('HXH', 72220),
             Node('HYJ', 78595), Node('IAD', 86012), Node('ILF', 1584), Node('JAS', 94982),
             Node('JMW', 23164), Node('JNU', 29623), Node('JUV', 22324), Node('JVO', 9920),
             Node('KAF', 87374), Node('KBD', 49928), Node('KBT', 46358), Node('KDG', 65385),
             Node('KEU', 28574), Node('KHO', 62721), Node('KSN', 85698), Node('KTF', 21115),
             Node('LAZ', 53410), Node('LDC', 99692), Node('LJX', 18777), Node('LOL', 26079),
             Node('MCX', 39614), Node('NHM', 10365), Node('NLY', 80036), Node('NNO', 27484),
             Node('NSR', 44318), Node('OMV', 64666), Node('OVB', 28031), Node('PIZ', 74919),
             Node('PLP', 30394), Node('PQI', 64347), Node('PQP', 75909), Node('PRB', 77939),
             Node('PVG', 60558), Node('PVP', 17483), Node('QCQ', 68850), Node('QCS', 81411),
             Node('QEL', 16409), Node('QJX', 32838), Node('QMO', 28032), Node('QOQ', 24757),
             Node('QRF', 90361), Node('QYB', 8951), Node('QYV', 85537), Node('RNX', 483),
             Node('ROJ', 41600), Node('SAV', 83700), Node('SCA', 7266), Node('SFU', 93844),
             Node('SRB', 31951), Node('SUG', 99938), Node('SYG', 81088), Node('TIL', 61594),
             Node('TMI', 75067), Node('UGW', 73622), Node('UHC', 11485), Node('UIQ', 25344),
             Node('VAY', 3518), Node('VLY', 77497), Node('VMU', 48442), Node('VTG', 76641),
             Node('WKL', 92524), Node('WRY', 14412), Node('WVL', 40082), Node('WWA', 43770),
             Node('XBO', 92173), Node('XCU', 1966), Node('XGX', 12368), Node('XWP', 71217),
             Node('YBM', 96665), Node('YCE', 57884), Node('YDL', 65032), Node('YET', 59833),
             Node('YXD', 7987), Node('ZAB', 66439), Node('ZAZ', 98319), Node('ZME', 22088)],
            '[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[AOV] AQV _] BBK [BDD]] BDJ _] BIL [BPS]] BWD [CHO]] CSU [_ CVB [CWX]]] CXR _] DDK [[[DQT] DSQ _] DSY _]] ERF _] FDL [FMH]] FOR [FOS]] GSZ [HXH]] HYJ _] IAD [ILF]] JAS [[JMW] JNU _]] JUV [JVO]] KAF _] KBD [KBT]] KDG [KEU]] KHO _] KSN [KTF]] LAZ _] LDC [[LJX] LOL _]] MCX [NHM]] NLY [NNO]] NSR _] OMV [OVB]] PIZ [PLP]] PQI _] PQP _] PRB _] PVG [PVP]] QCQ _] QCS [[QEL] QJX _]] QMO [QOQ]] QRF [QYB]] QYV [[RNX] ROJ _]] SAV [SCA]] SFU [SRB]] SUG _] SYG [TIL]] TMI _] UGW [[UHC] UIQ [VAY]]] VLY [VMU]] VTG _] WKL [[WRY] WVL _]] WWA _] XBO [[XCU] XGX _]] XWP _] YBM [YCE]] YDL _] YET [YXD]] ZAB _] ZAZ [ZME]]',
            26688471
        ),
    ]

    PASS_FAIL = {
        True: "Pass",
        False: "Fail"
    }

    for node_list, ans_str, ans_cost in test_cases:
        # for _ in range(10):
        tree = make_min_tree(node_list)
        str_ = str(tree)
        cost_ = cost(tree)
        print(f'string: {PASS_FAIL[str_ == ans_str]}')

        if not str_ == ans_str:
            print(f'\tYour Answer:\n{str_}')
            print(f'\tCrrt Answer:\n{ans_str}')
        print(f'\ncost: {PASS_FAIL[cost_ == ans_cost]}')

        if not cost_ == ans_cost:
            print(f'\tYour Answer:\n\t{cost_:,}')
            print(f'\tCrrt Answer:\n\t{ans_cost:,}')


# 156784995


