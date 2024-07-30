
#tuple
#tuple is immutable
t=("whale","shark","tortoise","humpback")
print(t)

#tuple type casting

t1=("whale","shark","stingray","killerwhale")
type_cast=list(t1)
type_cast.append("blue whale")
t=tuple(type_cast)
print(t)

#tuple slicing
print(t[0:1])
print(t[0:2])
print(t[0:3])
print(t[0:4])
print(t[0:5])
print(t[2:5])
