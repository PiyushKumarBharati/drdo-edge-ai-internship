friends=["ashwani","mayank","neeraj","yash"]
lucky_number=[28,1,67,49,10,45]

print(friends[1:])

print(friends[1:3])

print(friends[-4])
# friends.extend(lucky_number)

friends.insert(3,"prince")

friends.remove("yash")
print(friends)

print(friends.count("ashwani"))

friends2=friends.copy()   #deep copy

friends2.remove("prince")
print(friends2)
print(friends)

friends3=friends  #shallow copy

friends3.remove("prince")

print(friends3)
print(friends)