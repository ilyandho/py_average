count = 0
numbers = []

cont = True

print('\n\t\tWelcome to ilyandho\'s summing program\n')
print('''* Enter numbers to find their average\n** Enter 'done','DONE','d', 'D' to quit and get results\n''')

while cont:
    number = input('Enter a number: ')
    if number == 'done' or number == 'd' or number == 'D':

        print('\n\t\t************** Results **************\n')

        print('Count:', count)
        print('Total:', sum(numbers))

        try:
            print('Maximum value:', max(numbers))
            print('Minimum value:', min(numbers))
            print('Average:', sum(numbers)/count)
        except:
            print('Average: You didn\'t enter any numeic value')
            print('Maximum value: No value was entered')
            print('Minimum value:No value was entered')
        print('\nQuitting ...')
        print('\nThanks for using my program')
        cont = False
    else:
        try:
            number = float(number)
            numbers.append(number)
            count = count+1

        except:
            print('\nInvalid input...Enter a numeric value\n')
