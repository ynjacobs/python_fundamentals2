print('please enter temp in fahrenheit')
enter = input()
def fahr_to_cel(enter):
    return ((int(enter) - 32) * 5/9)

print('that is {} degrees celcius'.format(fahr_to_cel(enter)))