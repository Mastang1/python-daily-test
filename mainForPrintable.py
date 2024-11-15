strFoo = '123abc   ABC'

bytessss = bytes([1,2,3,4,5,6,7])
strTest = bytessss.decode()

print(str.isascii(strTest), len(strTest))

# subset of all printable characters
import string
printset = set(string.printable)
isprintable = set("fdfsd"+strTest).issubset(printset)

print(isprintable)
