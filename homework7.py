grades=[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students={'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
s=sorted(students)
print(s)
a=(sum(grades[0]))/(len(grades[0]))
b=(sum(grades[1]))/(len(grades[1]))
c=(sum(grades[2]))/(len(grades[2]))
d=(sum(grades[3]))/(len(grades[3]))
e=(sum(grades[4]))/(len(grades[4]))
z=[a]+[b]+[c]+[d]+[e]
print(z)
p=zip(s,z)
g=list(p)
print(dict(g))







