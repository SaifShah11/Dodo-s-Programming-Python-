while True:
    
    print('Welcome to Income Tax Collection')

    print()

    income=float(input('ENTER YOUR INCOME: '))

    print()

    tax=income*35/100

    disposable= income-tax

    if income<=10000:
        print('Income Tax is not Applicable')

    else:
        print('35% Tax =',tax)

        print()

        print('Disposable Income =', disposable)

    print()

    response=input('Do you want to Re-Calculate your Income Tax? (Y/N) ')

    if response == 'n' or response == 'N':
        break

print()

print('Thank you for your time!')
            

    
    
