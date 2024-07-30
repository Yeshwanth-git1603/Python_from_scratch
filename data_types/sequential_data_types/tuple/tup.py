
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
