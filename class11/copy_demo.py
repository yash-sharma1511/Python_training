import copy
original = {
    'name': 'Alice',
    'scores': [95, 88, 76]
}
shallow = original.copy()
deep = copy.deepcopy(original)
shallow['scores'].append(100)
print("After modifying shallow['scores']:")
print("Original:", original) 
print("Shallow:", shallow)     
print("Deep:", deep)           
