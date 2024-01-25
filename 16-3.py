prev = ''
def print_without_duplicates(message):
    global prev
    if message != prev:
        print(message)
    prev = message

print_without_duplicates("Привет")
print_without_duplicates("Не могу до тебя до звониться")
print_without_duplicates("Не могу до тебя до звониться")
print_without_duplicates("Не могу до тебя до звониться")
print_without_duplicates("Когда доедешьдо дома")
print_without_duplicates("Ага, жду")
print_without_duplicates("Ага, жду")