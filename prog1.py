"""def find(num):
    n=len(num)+1
    total=n*(n+1)//2
    return total- sum(num)
print(find([1,2,4,5]))"""
"""def has_loop(d):
    visited=set()
    key=next(iter(d))
    while key in d:
        if key in visited:
            return True
        visited.add(key)
        key=d[key]
    return False
print(has_loop({1:2,2:3,3:4,4:2}))
        """
"""def firstchar(s):
    freq={}
    for c in s:
        freq[c]=freq.get(c,0)+1
    for c in s:
         if freq[c]==1:
             return c
    return None
print(firstchar("aabbecff"))"""
def reversevowels():
    s="hello"
    vowels="aeiouAEIOU"
    left=0
    right=len(s)-1
    s=list(s)
    while left<right:
        if s[left] not in vowels:
            left+=1
        elif s[right] not in vowels:
            right-=1
        else:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
            return "".join(s)
print(reversevowels())
