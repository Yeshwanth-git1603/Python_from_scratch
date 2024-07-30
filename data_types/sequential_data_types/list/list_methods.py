list1=["whale","stingray","shark","seahorse","humpback whale","phirana","great white"]

#list functions

list1.append("killer whale")
list1.insert(8,"tiger shark")
list1.remove("tiger shark")
list1.pop(1)
list2=list1.copy()
list1.extend(list2)
print(list1)
print(list2)
list2.insert(1,"stingray")
print(list2)
print(list2[0:5])
print(list2[0::])
# to reverse the list
print(list2[::-1])
