from unittest import TestCase
from BefungeInterpreter import interpret


class Test(TestCase):
    def test_from_description(self):
        test, ans = ('>987v>.v\nv456<  :\n>321 ^ _@', '123456789')
        self.assertEqual(interpret(test), ans)

    def test_hello_world(self):
        test, ans = ('>25*"!dlroW olleH":v\n                v:,_@\n                >  ^', 'Hello World!\n')
        self.assertEqual(interpret(test), ans)

    def test_factorial(self):
        test, ans = ('08>:1-:v v *_$.@ \n  ^    _$>\\:^', '40320')
        self.assertEqual(interpret(test), ans)

    def test_quine(self):
        test, ans = ('01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@', '01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@')
        self.assertEqual(interpret(test), ans)

    def test_sieve_of_Eratosthenes(self):
        test ='2>:3g" "-!v\\  g30          <\n' \
              ' |!`"&":+1_:.:03p>03g+:"&"`|\n' \
              ' @               ^  p3\\" ":<\n' \
              '2 2345678901234567890123456789012345678'
        ans = '23571113171923293137'

        self.assertEqual(interpret(test), ans)

    def test_random_direction(self):
        test, ans = ('v@.<\n >1^\n>?<^\n >2^', ['1', '2'])
        self.assertIn(interpret(test), ans)
