lst=[2,1,4,6,7,12]
def sum_even(lst):
    ans=0
    for i in lst:
        if i%2==0:
            ans+=i
        else:
            pass
    return ans
print(sum_even(lst))        
                
