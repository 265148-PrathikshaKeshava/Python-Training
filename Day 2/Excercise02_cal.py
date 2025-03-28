'''3. Design a simple calculator which has the following functionality:
   add, sub, mul, div, mod, sqrt, log [15]'''

print("Simple calculate:\n")
print("1. Add\n2.sub\n3.mul\n4.div\n5.mod\n6.sqrt\n7.log\n")
import math
ch = int(input("Enter your choice"))

if ch == 1:
    print("-------Addition-------")
    val1 = int(input("Enter the val1"))
    val2 = int(input("Enter the val2"))
    add = val1 + val2
    print("Add: %d" % add)
elif ch == 2:
    print("-------Sub-------")
    val1 = int(input("Enter the val1"))
    val2 = int(input("Enter the val2"))
    sub = val1 - val2
    print("Sub: %d" % sub)
elif ch == 3:
    print("-------Mul-------")
    val1 = int(input("Enter the val1"))
    val2 = int(input("Enter the val2"))
    mul = val1 * val2
    print("Mul: %d" % mul)
elif ch == 4:
    print("-------Div-------")
    val1 = int(input("Enter the val1"))
    val2 = int(input("Enter the val2"))
    div = val1 / val2
    print("Div: %.2f" % div)
elif ch == 5:
    print("-------Mod-------")
    val1 = int(input("Enter the val1"))
    val2 = int(input("Enter the val2"))
    mod = val1 / val2
    print("Mod: %d" % mod)
elif ch == 6:
    print("-------Sqrt-------")
    val1 = int(input("Enter the val1 "))
    sq = math.sqrt(val1)
    print("sqrt: %2.f" % sq)
    
elif ch == 7:
    print("-------Log-------")
    val1 = int(input("Enter the val1 "))
    add = math.log(val1)
    print("Log: %d" % add) 
else:
    print("Invalid")