d1 = {'a': 5, 'b': 10}
d2 = {'b': 7, 'c': 3}
merged={}
for key in d1:
    merged[key]=d1[key]
for key in d2:
    if key in merged:
        merged[key]=max(merged[key],d2[key])
    else:
        merged[key]=d2[key]
print(merged)               