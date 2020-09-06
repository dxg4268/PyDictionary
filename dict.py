# Dictionary is a key value pairs
d1 = {}
print(type(d1))

d2 = {"_x":"2a", "_y":"2b", "_z":"2c"}

#print(d2)

d3 = d2.copy()

# d3['_h'] = '2g'
# d3['_i'] = '3a'
# del d3['_i']

#print(d3.get('_x'))


# Various methods of Dictionary
d3.update({'_w':'r'})
print(d3.popitem()) #Remove Last Item from dictionary
print(d3.pop('_x')) #Take keys() and remove the key, value pair
print(d3.values()) #Returns values of keys in dictionary
print(d3.keys()) 
print(d3.items())
print(d3.get('_y'))
