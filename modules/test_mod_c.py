import test_mod_b
import sys

print("test_mod_c  ", sys.modules)
print(dir(test_mod_b)) 
print(dir(test_mod_b.test_mod_a))

