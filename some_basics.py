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

# This is probably a merge conflict!
f[0] = 1
g[0] = 1
