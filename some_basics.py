#%%
# Some variables of simple types.
a = 123
b = 1.23
c = "123"
d = '123'
e = True

#%%
# Some variables of Python container types.
f = [a, b, c] 
g = (a, b, c)
h = {'a': a, b: 'b', d: e}

#%%
# Printing contents
print("f = ", f)

#%%
# Show some numpy
import numpy as np
x = np.array([1, 2, 3, 4, 5])
y = x**2
