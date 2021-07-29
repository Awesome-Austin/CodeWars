class SomeClass:
    pass

import sys, os
CLASS = SomeClass

with open(os.path.abspath(sys.modules[CLASS.__module__].__file__)) as f:
    print(f.read())
