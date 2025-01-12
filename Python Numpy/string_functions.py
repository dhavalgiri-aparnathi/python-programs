import numpy as np

var = np.char.lower('HELLO')
var2 = np.char.upper('this is Upper Case')
var3 = np.char.strip('   this is a stripped string   ')
var4 = np.char.title('this is just some random string in title case')
var5 = np.char.capitalize('this is a capitalized string')

print(var)
print(var2)
print(var3)
print(var4)
print(var5)
