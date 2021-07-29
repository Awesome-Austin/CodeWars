class Tree(object):

    def __init__(self, root, left=None, right=None):

        self.left = left
        self.root = root
        self.right = right

    def is_leaf(self):
        return not (self.left or self.right)

    def printString(self, tree):
        if tree is None:
            return "_ "
        if tree.left is None and tree.right is None:
            return "[" + str(tree.root.value) + ":" + str(tree.root.weight) + "] "
        return "[" + self.printString(tree.left) + str(tree.root.value) + ":" + str(
            tree.root.weight) + " " + self.printString(tree.right)[:-1] + "] "

    def __str__(self):
        return self.printString(self)[:-1]

    def isEqual(self, tree1, tree2):
        if tree1 is None and tree2 is None:
            return True
        if tree1 is None and tree2:
            return False
        if tree1 and tree2 is None:
            return False
        if tree1.root.value != tree2.root.value:
            return False
        return self.isEqual(tree1.left, tree2.left) and self.isEqual(tree1.right, tree2.right)

    def __eq__(self, other):
        return self.isEqual(self, other)

    def __ne__(self, other):
        return not self.isEqual(self, other)


class Node(object):

    def __init__(self, value, weight=1):
        self.value = value
        self.weight = weight

    def __str__(self):
        return str(self.value)

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value


def cost(tree, depth=1):
    if tree is None:
        return 0
    if tree.is_leaf():
        return tree.root.weight * depth
    return tree.root.weight * depth + cost(tree.left, depth + 1) + cost(tree.right, depth + 1)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i].weight > right[j].weight:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


def insert(root, node):
    x = root

    y = None

    while x is not None:
        y = x
        if node < x.root:
            x = x.left
        else:
            x = x.right

    if node < y.root:
        y.left = Tree(node)

    else:
        y.right = Tree(node)


def make_min_tree(node_list):
    return findOptimalCost(node_list)


def findOptimalCost(freq):
    n = len(freq)
    cost = [[0] * (n + 1) for _ in range(n + 1)]
    roots = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n):
        cost[i][i] = freq[i].weight
        roots[i][i] = freq[i].value

    arr = [[0 for _ in range(n + 1)] for i in range(n + 1)]
    start = 0
    d = 1
    while d != n:
        end = d - start
        while end != n + 1:
            s = 0
            for k in range(start, end):
                s += freq[k].weight
            arr[start][end] = s
            start += 1
            end += 1
        start = 0
        d += 1
    print(arr)

    for size in range(1, n + 1):
        for i in range(n - size + 2):
            j = min(i + size - 1, n - 1)
            cost[i][j] = float('inf')
            for r in range(i, j + 1):
                total = 0
                # for k in range(num, j + 1):
                #   total += freq[k].weight
                total = arr[i][j + 1]
                if r != i:
                    total += cost[i][r - 1]
                if r != j:
                    total += cost[r + 1][j]
                if total < cost[i][j]:
                    cost[i][j] = total
                    roots[i][j] = r + 1

    for i in range(len(roots)):
        roots[i] = roots[i][:-1]
        roots[i].insert(0, 0)
    freq.insert(0, 0)
    tree = recursive(roots, freq, 0, n)
    freq.remove(0)
    return tree


def recursive(roots, nodes, i, j):
    if roots[i][j] == 0:
        return None
    return Tree(nodes[roots[i][j]], recursive(roots, nodes, i, roots[i][j] - 1),
                recursive(roots, nodes, roots[i][j], j))


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