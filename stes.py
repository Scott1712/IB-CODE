#14/05/26

friends = {"Sarah","Tom","Emma","Alex"}  #Important

print(friends)

print("Scott" in friends)            #Important

if "Tom" in friends:            #Important
    print("They are a friend")
else:
    print("They are not a friend")

print(friends)
friends.add("Scott")             #Important
print(friends)

friends.discard("Alex")         #Important
print(friends)

close = {"Sarah","Scott"}
print(close <= friends)         #Important (Subset?)

extras = {"Andy","Matteo"}
everyone = friends | extras             #Important (Union)
print(everyone)

kinda = friends - close             #Important (In one, but not other)
print(kinda)