fruits=["kiwi","orange","banana"]
for index,fruit in enumerate(fruits):
    print(index,fruit)
for index,fruit in enumerate(fruits,start=2):
    print(index,fruit)
fruits=("mango","grapes","apple")
for index,fruit in enumerate(fruits):
    print(index,fruit)
word="python"
for index,character in enumerate(word):
    print(index,character)
test_cases = ["login","signup","checkout"]
for test_no,test in enumerate(test_cases):
    print(f"Executing testcases {test_no}: {test}")
a=["god","is","great"]
b=enumerate(a)
next_val = next(b)
next_value1 = next(b)
next_value2=next(b)
print(next_val)
print(next_value1)
print(next_value2)
characters = ["apple","kiwi","mango","kiwi","apple","grapes","mango"]
character_map={character:[] for character in set(characters)}
for index,character in enumerate (characters):
    character_map[character].append(index)
print(character_map)