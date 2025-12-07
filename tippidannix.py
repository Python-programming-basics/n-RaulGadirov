my_dict = {1.12: 'aa', 67.9: 45, 3.11: 'ccc', 7.9: 'dd', 9.2: 'ee', 7.1: 'ff', 0.12: 'qq', 1.91: 'aa', 10.12: [1, 2, 3], 99.0: {9, 0, 1}}

a = []
for i in my_dict.keys():
    a.append(i)
print(min(a))

# #2
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618', 'email': 'helga@mail.net'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434', 'email': 'ali.ch.b@gmail.com'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059', 'email': 'roma988@mail.ru'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

s=""

for user in users:
    phone = user["phone"]
    if phone[-1] == "8":
        s+=user["name"]+" "
print(s)

# #3
users = [{'name': 'Todd', 'phone': '551-1414', 'email': 'todd@gmail.com'},
         {'name': 'Helga', 'phone': '555-1618'},
         {'name': 'Olivia', 'phone': '449-3141', 'email': ''},
         {'name': 'LJ', 'phone': '555-2718', 'email': 'lj@gmail.net'},
         {'name': 'Ruslan', 'phone': '422-145-9098', 'email': 'rus-lan.cha@yandex.ru'},
         {'name': 'John', 'phone': '233-421-32', 'email': ''},
         {'name': 'Lara', 'phone': '+7998-676-2532', 'email': 'g.lara89@gmail.com'},
         {'name': 'Alina', 'phone': '+7948-799-2434'},
         {'name': 'Robert', 'phone': '420-2011', 'email': ''},
         {'name': 'Riyad', 'phone': '128-8890-128', 'email': 'r.mahrez@mail.net'},
         {'name': 'Khabib', 'phone': '+7995-600-9080', 'email': 'kh.nurmag@gmail.com'},
         {'name': 'Olga', 'phone': '6449-314-1213', 'email': ''},
         {'name': 'Roman', 'phone': '+7459-145-8059'},
         {'name': 'Maria', 'phone': '12-129-3148', 'email': 'm.sharapova@gmail.com'},
         {'name': 'Fedor', 'phone': '+7445-341-0545', 'email': ''},
         {'name': 'Tim', 'phone': '242-449-3141', 'email': 'timm.ggg@yandex.ru'}]

s = ""

for user in users:
    if not user.get("email"):   
        s += user["name"] + " "

print(s)



# #4
num = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"
}
n = int(input("write num"))
s=''
for i in str(n):
    s+=num[int(i)]+" "
print(s)


# #5
num = {
    "CS101": {
        "code": "CS101",
        "room": "3004",
        "teacher": "Хайнс",
        "time": "8:00"
    },
    "CS102": {
        "code": "CS102",
        "room": "4501",
        "teacher": "Альварадо",
        "time": "9:00"
    },
    "CS103": {
        "code": "CS103",
        "room": "6755",
        "teacher": "Рич",
        "time": "10:00"
    },
    "NT110": {
        "code": "NT110",
        "room": "1244",
        "teacher": "Берк",
        "time": "11:00"
    },
    "CM241": {
        "code": "CM241",
        "room": "1411",
        "teacher": "Ли",
        "time": "13:00"
    }
}

n = input("write: ")
print(num[n]["code"], num[n]["room"], num[n]["teacher"], num[n]["time"])

# #6
text = input()

keys = {
    '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111',
    'A': '2', 'B': '22', 'C': '222',
    'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444',
    'J': '5', 'K': '55', 'L': '555',
    'M': '6', 'N': '66', 'O': '666',
    'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
    'T': '8', 'U': '88', 'V': '888',
    'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
    ' ': '0'
}

result = ''

for letter in text:
    upper_letter = letter.upper()
    if upper_letter in keys:
        result = result + keys[upper_letter]

print(result)
# #7
morse = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}
a = input()
s = ""
for i in a:
    s+=morse[i.upper()]+" "
print(s)
# #8
s = {}
for i in range(11,16):
    s.setdefault(i,i**2)
print(s)
# #9
dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
result={}
for i in dict1:
    if i in dict2:
        result.setdefault(i,dict1[i]+dict2[i])
    else:
        result.setdefault(i,dict1[i])
for j in dict2:
    if j not  in dict1:
        result.setdefault(j,dict2[j])
print(result)
# #10
result={}
text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
for i in text:
    result.setdefault(i,text.count(i))
print(result)
# #11
s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
result = {}
text = s.split()

for i in text:
    result.setdefault(i, s.count(i))

kolvo = max(result.values())

candidates = []
for word, count in result.items():
    if count == kolvo:
        candidates.append(word)

best = min(candidates)

print(best)


# #12
pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]
result = {}

for pet, fname, lname, age in pets:
    owner = (fname, lname, age)
    result.setdefault(owner, []).append(pet)

print(result)
# #13

s = input()
for ch in ".,!?:;":
    s = s.replace(ch, "")
result={}
text = s.split()
for i in text:
    result.setdefault(i,text.count(i))
kolvo = min(result.values())
for key,values in result.items():
    if values==kolvo:
        print(key)
print(result)
# #14
text = input().split()
seen = {}
s = ""

for word in text:
    if word not in seen:
        seen[word] = 0
        s+=word+" "
    else:
        seen[word] += 1
        new_word = f"{word}_{seen[word]}"
        s+=new_word+" "

print(s)










