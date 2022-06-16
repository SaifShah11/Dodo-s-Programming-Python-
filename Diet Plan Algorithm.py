M='MALE'

F='FEMALE'

Gender = input('Enter your Gender Male/Female ').upper()  

Age=int(input('Enter your Age '))

Weight=float(input('Enter your weight in Kgs '))

Height=float(input('Enter your height in centimeters '))
      
Goal=input('Do you want to Maintain or Lose weight? ')


print('\n')


#Calories Based on Assumption of Rest Only

if Gender == M:
    print('BMR (Male) =', 10*Weight + 6.25*Height - 5*Age + 5, 'Kcal')# Mifflin-St Jeor Equation

elif Gender == F:
    print('BMR (Female)=', 10*Weight + 6.25*Height - 5*Age - 161,'Kcal')# Mifflin-St Jeor Equation
else:
    print('Incorrect Gender Input')

print('\n')    

#Calories Based on Activity Level
 
    
L='LOW'
Mo='MODERATE'
H='HIGH'

print('Low= Exercise 1-2 days a week')
print('Moderate= Exercise 3-4 days a week')
print('High= Exercise 3-6 days a week')

print('\n')  

Activity=input('Enter your Activity Level (Low, Moderate, High) ').upper()

if Gender==M:

    if Activity == L:

        print('BMR (Male) =', (10*Weight + 6.25*Height - 5*Age + 5) * 1.2, 'Kcal')

    elif Activity == Mo:

        print('BMR (Male) =', (10*Weight + 6.25*Height - 5*Age + 5) * 1.375, 'Kcal')

    elif Activity == H:

        print('BMR (Male) =', (10*Weight + 6.25*Height - 5*Age + 5) * 1.55, 'Kcal')

    else:

        print('Incorrect Input')

if Gender==F:

    if Activity == L:

        print('BMR (Female)=', 10*Weight + 6.25*Height - 5*Age - 161 * 1.2, 'Kcal')

    elif Activity == Mo:

        print('BMR (Female) =', (10*Weight + 6.25*Height - 5*Age - 161) * 1.375, 'Kcal')

    elif Activity == H:

        print('BMR (Female) =', (10*Weight + 6.25*Height - 5*Age - 161) * 1.55, 'Kcal')

    else:

        print('Incorrect Input')

print('\n')


#Consumption of MacroNutrients (Diet Plan)

print('Keto Diet')
print('Moderate Carb Diet')

KET='KETO'
MCD='MODERATE'

print('\n')

Diet=input('Choose your preferred Diet (Keto, Moderate) ').upper()

print('\n')

if Diet== KET:
    if Gender== M:
        if Activity== L:

            print('Protien=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.2) *(30/100)/4, 'grams')
            print('Carbs=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.2) *(10/100)/4, 'grams')
            print('Fats=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.2) *(60/100)/9, 'grams')

            
        elif Activity== Mo:
            
            print('Protien=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.375) * (30/100)/4, 'grams')
            print('Carbs=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.375) * (10/100)/4, 'grams')
            print('Fats=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.375) * (60/100)/9, 'grams')       


        elif Activity== H:

            print('Protien=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.55) * (30/100)/4, 'grams')
            print('Carbs=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.55) * (10/100)/4, 'grams')
            print('Fats=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.55) * (60/100)/9, 'grams')
            

        else:
            print(Diet, Gender, Activity)
            print('Incorrect Input')

    elif Gender== F:
        if Activity== L:

            print('Protien=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.2) * (30/100)/4, 'grams')
            print('Carbs=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.2) * (10/100)/4, 'grams')
            print('Fats=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.2) * (60/100)/9, 'grams')

        

        elif Activity== Mo:

            print('Protien=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.375) * (30/100)/4, 'grams')
            print('Carbs=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.375) * (10/100)/4, 'grams')
            print('Fats=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.375) * (60/100)/9, 'grams')       
            

        elif Activity== H:

            print('Protien=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.55) * (30/100)/4, 'grams')
            print('Carbs=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.55) * (10/100)/4, 'grams')
            print('Fats=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.55) * (60/100)/9, 'grams')

        else:
            print(Diet, Gender, Activity)
            print('Incorrect Input')

elif Diet== MCD:
    if Gender== M:
        if Activity== L:

            print('Protien=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.2) * (30/100)/4, 'grams')
            print('Carbs=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.2) * (10/100)/4, 'grams')
            print('Fats=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.2) * (60/100)/9, 'grams')

            
        elif Activity== Mo:
            
            print('Protien=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.375) * (30/100)/4, 'grams')
            print('Carbs=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.375) * (10/100)/4, 'grams')
            print('Fats=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.375) * (60/100)/9, 'grams')       


        elif Activity== H:

            print('Protien=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.55) * (30/100)/4, 'grams')
            print('Carbs=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.55) * (10/100)/4, 'grams')
            print('Fats=',(10*Weight + 6.25*Height - 5*Age + 5) * (1.55) * (60/100)/9, 'grams')
            

        else:
            print(Diet, Gender, Activity)
            print('Incorrect Input')

    elif Gender== F:

        if Activity== L:

            print('Protien=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.2) * (30/100)/4, 'grams')
            print('Carbs=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.2) * (10/100)/4, 'grams')
            print('Fats=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.2) * (60/100)/9, 'grams')

        

        elif Activity== Mo:

            print('Protien=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.375) * (30/100)/4, 'grams')
            print('Carbs=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.375) * (10/100)/4, 'grams')
            print('Fats=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.375) * (60/100)/9, 'grams')       
            

        elif Activity== H:

            print('Protien=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.55) * (30/100)/4, 'grams')
            print('Carbs=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.55) * (10/100)/4, 'grams')
            print('Fats=',(10*Weight + 6.25*Height - 5*Age - 161) * (1.55) * (60/100)/9, 'grams')

        else:
            print(Diet, Gender, Activity)
            print('Incorrect Input')

   
else:
    print(Diet, Gender, Activity)
    print('Incorrect Input')

print('\n')

print('Thank you for your time!')
