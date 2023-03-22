my_dict_raw = {
    "AEIOULNSTR": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10,
    "АВЕИНОРСТ": 1,
    "ДКЛМПУ": 2,
    "БГЁЬЯ": 3,
    "ЙЫ": 4,
    "ЖЗХЦЧ": 5,
    "ШЭЮ": 8,
    "ФЩЪ": 10,
}
my_dict = {}
for row in my_dict_raw:
    for letter in row:
        key = letter.lower()
        value = my_dict_raw.get(row)
        my_dict[key] = value

# print(my_dict)
word = input("Введите слово прописными буквами: ")
word_weight = 0

for letter in word:
    word_weight += my_dict.get(letter)

print(f"Стоимость введенного слова {word_weight}")
