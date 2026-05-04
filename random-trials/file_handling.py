with open('Trials/companies.txt', 'r+') as file:
    data = file.read()
    print(data)
    chars_written = file.write('Nvidia ')
    print(chars_written)