print('welcome to dumi ATM')
restart = 'Y'
chances = 3
balance = 100000.00
while chances >= 0:
    pin = int(input('what is your pin number'))
    if pin == 1234:
        print('PIN CORRECT')
        print('please press 1 to check your balance')
        print('please press 2 to make a withdrawal from your account')
        print('please press 3 to make a deposit')
        print('please press 4 to remove card \n')

        option = int(input('What would you like to do? '))
        if option == 1:
            print(f'Your balance is ${balance} ')
            restart = input('would you like to perform another transaction? \n click Y or yes for yes! and n, N, no and NO for no! ')
            if restart in ('n', 'NO', 'no', 'N'):
                print('THANK YOU')

            elif restart in ('Y', 'yes'):
                print('OK')
                restart = ('Y')




        elif option == 2:
            withdrawal = float(input('How much would you like to withdraw? 1000 \n 2000 \n 5000 \n 10000 \n 20000. \n For other amount, enter 1'))
            if withdrawal in (1000, 2000, 5000, 10000, 20000):
                new_balance = balance - withdrawal
                print(f'your balance is now ${new_balance}')
                restart = input('would you like to perform another transaction? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('THANK YOU')
                break
            elif withdrawal != (1000, 2000, 5000, 10000, 20000):
                print('Invalid amount, try again \n')
                restart = 'Y'
            if withdrawal == 1:
                make_withdrawal = float(input('Please enter the desired amount.'))
            if make_withdrawal <= 100000:
                current_balance = balance - make_withdrawal
                print(f'Your new balance is ${current_balance} ')
                restart = input('would you like to perform another transaction? ')
                if restart in ('n', 'NO', 'no', 'N'):
                    print('THANK YOU')
                break


        elif option == 3:
            deposit = float(input('How much would you like to pay in? '))
            current_balance = balance + deposit
            print(f'Your balance is now ${current_balance}')
            restart = input('would you like to perform another transaction? ')
            if restart in ('n', 'NO', 'no', 'N'):
                print('THANK YOU')
            break

        elif option == 4:
            print('Wait while we retrieve your card')
            print('Please take your card \n Thank you!')
            break

        else:
            print('Please enter the correct pin. \n')
            restart = 'Y'

    elif pin != 1234:
        print('INCORRECT PIN')
        restart = 'Y'
        chances -= 1
        if chances == 0:
           print('No more tries')
           break





