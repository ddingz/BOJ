def self_number():
    self_set=set(range(1,10001))
    not_self=set()
    for i in range(1,10001):
        for j in str(i):
            i+=int(j)
        not_self.add(i)
    #A.difference(B) set의 차집합(A-B)
    self_set=self_set.difference(not_self)
    return self_set
show=self_number()
for i in sorted(show):
    print(i)