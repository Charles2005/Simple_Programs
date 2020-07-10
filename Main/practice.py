import math
import datetime
import cmath
import random
import time

# Basic Data types Programs
def main():

# Letter counter app
    print("Welcome to the Letter Counter App")
# Get user Input
    name = input("What is your name?: ").title()
    print("Hello " + name)

    print("I will count the number of times that a specific letter occurs in a message.")
    message = input("Please enter a message: ")
    count = input("Which letter would you like to count the occurrences of?: ")
# To lower case
    message = message.lower()
    count = count.lower()
#Get count and display result
    count_letter = message.count(count)
    print(name + ", your message has " + str(count_letter) + " " + count + "'s in it")


def conversion():
# Miles per hour conversion app
    print("Welcome to the Miles Per hour Conversion App")
# Get user
    speed = float(input("What is your speed miles per hour?: "))
# Conversion formula for mph to mps
    formula = speed * 0.4474
    formula = round(formula, 2)
# Display answer
    print("Your speed in meters per second is " + str(formula))


def temp_conversion():

# Temperature conversion app
    print("Welcome to the Temperature Conversion App")
# Get user
    temp = float(input("What is the given temperature in degrees Fahrenheit?: "))
# Formulas
    celsius_formula = (temp - 32 ) / 1.8
    kelvin_formula = (temp + 459.67) * 5/9
    temp = round(temp, 4)
    celsius_formula = round(celsius_formula, 4)
    kelvin_formula = round(kelvin_formula, 4)
# Conversions
    print("Degrees Fahrenheit:\t" + str(temp))
    print("Degrees in Celsius:\t" + str(celsius_formula))
    print("Degrees in Kelvin:\t" + str(kelvin_formula))


def right_triangle():
# Right Triangle app
    print("Welcome to the Right Triangle Solver App")
# Get user
    first_leg = float(input("What is the first leg of the triangle?: "))
    second_leg = float(input("What is the second leg of the triangle?: "))
# Formulas
    formula = (first_leg)**2 + (second_leg)**2
    hypotenuse_formula = math.sqrt(formula)
    hypotenuse_formula = round(hypotenuse_formula,3)
    area = 1/2 * first_leg * second_leg
# Answer
    print("For a triangle with legs of " + str(first_leg) + " and " + str(second_leg) + " the hypotenuse is " + str(hypotenuse_formula))
    print("For a triangle with legs of " + str(first_leg) + " and " + str(second_leg) + " the area is " + str(area))


def mult_exp_table():
    # Multiplication/Exponent table app
    print("Welcome to the Multiplication/Exponent Table App")
    # Get user
    name = input("What is your name?: ").title()
    num = float(input("What number would you like to work with?: "))
    message = name.title() + ", Math is cool!"
    # Formula in multiplication and Answer
    print("\nMultiplication table for " + str(num))
    print("1.0 " + "* " + str(num) + " = " + str(round(1*num, 4)))
    print("2.0 " + "* " + str(num) + " = " + str(round(2.0*num, 4)))
    print("3.0 " + "* " + str(num) + " = " + str(round(3.0*num, 4)))
    print("4.0 " + "* " + str(num) + " = " + str(round(4.0*num, 4)))
    print( "5.0 " + "* " + str(num) + " = "+ str(round(5.0*num, 4)))
    print("6.0 " + "* " + str(num) +  " = " + str(round(6.0*num, 4)))
    print( "7.0 " + "* " + str(num) + " = " + str(round(7.0*num, 4)))
    print( "8.0 " + "* " + str(num) + " = " + str(round(8.0*num, 4)))
    print( "9.0 " + "* " + str(num) + " = " + str(round(9.0*num, 4)))
    print("10.0 " + "* " + str(num) +  " = " + str(round(10.0*num, 4)))

    #Exponent
    print("\nExponent table for " + str(num))
    print("1.0 " + "** " + str(num) + " = " + str(round(1.0**num, 4)))
    print("2.0 " + "** " + str(num) + " = " + str(round(2.0**num, 4)))
    print("3.0 " + "** " + str(num) + " = " + str(round(3.0**num, 4)))
    print("4.0 " + "** " + str(num) + " = " + str(round(4.0**num, 4)))
    print( "5.0 " + "** " + str(num) + " = "+ str(round(5.0**num, 4)))
    print("6.0 " + "** " + str(num) +  " = " + str(round(6.0**num, 4)))
    print( "7.0 " + "** " + str(num) + " = " + str(round(7.0**num, 4)))
    print( "8.0 " + "** " + str(num) + " = " + str(round(8.0**num, 4)))
    print( "9.0 " + "** " + str(num) + " = " + str(round(9.0**num, 4)))
    print("10.0 " + "**" + str(num) +  " = " + str(round(10.0**num, 4)))

    # print message
    print("\n"  + message)
    print("\n\t"  + message.lower())
    print("\n\t\t"  + message.title())
    print("\n\t\t\t"  + message.upper())
    pass


# List programs


def sorter():
    # Grade Sorter App
    print("Welcome to the Grade Sorter App")
    grades = []
# Get user info
    first_grade = input("\nWhat is your first grade (0-100)?: ")
    grades.append(first_grade)
    second_grade = input("What is your second grade (0-100)?: ")
    grades.append(second_grade)
    third_grade = input("What is your third  grade (0-100)?: ")
    grades.append(third_grade)
    fourth_grade = input("What is your fourth grade (0-100)?: ")
    grades.append(fourth_grade)
# To the add the grades to the list
    print("Your grades are: " + str(grades))
# Sort the list
    grades.sort(reverse= True)
    print("\nYour grades from highest to lowest are: " + str(grades))
# Lowest will remove
    print("\nThe lowest two lowest grades will now be dropped.")
    lowest_grade = grades.pop(3)
    second_low = grades.pop(2)
    print("Removed Grade: " + str(lowest_grade))
    print("Removed Grade: " + str(second_low))
# display remaining grade and the highest grade
    print("\nYor remaining grades are: " + str(grades))
    print("Nice work! Your highest grade is a " + str(grades[0]))


def summ():
    # Types of lists program
    print("\tSummary Table")
    num_string = ["55","60","70","30"]
    print('\nThe variable num_string is a ' + str(type(num_string)))
    print('It contains the elements: ' + str(num_string))
    print('The element '+ str(num_string[0]) + ' is a ' + str(type(num_string[0])))

    # int summ
    num_int = [5,3,4,6]
    print('\nThe variable num_int is a ' + str(type(num_int)))
    print('It contains the elements: ' + str(num_int))
    print('The element '+ str(num_int[2]) + ' is a ' + str(type(num_int[2])))

    # float summ
    floats = [55.5,44.5,64.3,56.5]
    print('\nThe variable floats is a ' + str(type(floats)))
    print('It contains the elements: ' + str(floats))
    print('The element '+ str(floats[1]) + ' is a ' + str(type(floats[1])))

    # nested list
    nested_list = [[3, 4, 5], [5, 6, 7], [7, 8, 9]]
    print('\nThe variable nested_list is a ' + str(type(nested_list)))
    print('It contains the elements: ' + str(nested_list))
    print('The element ' + str(nested_list[2]) + ' is a ' + str(type(nested_list[2])))

    # Sorting
    print('\nNow sorting num_string and num_int...')
    num_string.sort()
    num_int.sort()
    print(num_string)
    print(num_int)
    print('\nStrings are sorted alphabetically while integers are sorted numerically!')


def grocery_list_app():
    # Grocery list App
    foods = ['Meat', 'Cheese']
    print('Welcome to Grocery list app!')
    time = datetime.datetime.now()
    month = str(time.month)
    day = str(time.day)
    hour = str(time.hour)
    minute = str(time.minute)
    print('Current Date and Time:' + month + "/" + day + " " + hour + ":" + minute)
    print('You currently have Meat and Cheese in your list.')
    # User Add food
    food = input('Type of food to add to the grocery list: ').title()
    foods.append(food)
    food = input('Type of food to add to the grocery list: ').title()
    foods.append(food)
    food = input('Type of food to add to the grocery list: ').title()
    foods.append(food)
    print('Here is your grocery list: ')
    print(foods)
    # Sort the list
    foods.sort()
    print('Here is your grocery list: ')
    print(foods)
    # Simulate list
    print('\nSimulating grocery shopping...')
    print('\nCurrent grocery list: ' + str(len(foods)) + ' Items')
    print(foods)
    # Buying foods
    buy = input('What foods did you just buy: ').title()
    foods.remove(buy)
    print('Removing ' + buy + 'from list')
    # 4items
    print('\nCurrent grocery list: ' + str(len(foods)) + ' Items')
    print(foods)
    buy = input('What foods did you just buy: ').title()
    foods.remove(buy)
    print('Removing ' + buy + 'from list')
    # 3 items
    print('\nCurrent grocery list: ' + str(len(foods)) + ' Items')
    print(foods)
    buy = input('What foods did you just buy: ').title()
    foods.remove(buy)
    print('Removing ' + buy + 'from list')
    # 2 items
    print('\nCurrent grocery list: ' + str(len(foods)) + ' Items')
    print(foods)
    no_food = foods.pop()
    print('\nSorry the store is out of ' + no_food)
    another = input('What food would you like instead: ')
    foods.append(another)
    print('Here is what remains on your grocery list:')
    print(foods)


def basketball_roster():
    # Basketball roster program
    print('Welcome to the Basketball Roster Program')
    roster = []
    # Get Roster
    point_guard = input('\nWho is your point guard?: ').title()
    roster.append(point_guard)
    shooting_guard = input('Who is your shooting guard?: ').title()
    roster.append(shooting_guard)
    small_forward = input('Who is your small forward?: ').title()
    roster.append(small_forward)
    power_forward = input('Who is your power forward?: ').title()
    roster.append(power_forward)
    center = input('Who is your center?: ').title()
    roster.append(center)
    # list of roster
    print('\n\tYour starting 5 for the upcoming basketball season:')
    print('\t Point guard:' + (" ") + point_guard)
    print('\t Shooting guard:' + (" ") + shooting_guard)
    print('\t Small Forward:' + (" ") + small_forward)
    print('\t Power Forward:' + (" ") + power_forward)
    print('\t Center:' + (" ") + center)
    # Remove small forward
    roster.remove(small_forward)
    print('\nOh no ' + small_forward + ' is injured')
    print('Your roster only has ' + str(len(roster)) + ' players')
    sub = input('Who will take ' + small_forward + "'s spot?:").title()
    roster.append(sub)

    # list of roster
    print('\n\tYour starting 5 for the upcoming basketball season:')
    print('\t Point guard:' + (" ") + point_guard)
    print('\t Shooting guard:' + (" ") + shooting_guard)
    print('\t Small Forward:' + (" ") + sub)
    print('\t Power Forward:' + (" ") + power_forward)
    print('\t Center:' + (" ") + center)

    # Message
    print('\nGood luck ' + sub + ' you will do great')
    print('Your roster now has ' + str(len(roster)) + (' players'))


def favorite_teachers():
    # Favorite Teachers Program
    print('Welcome to the Favorite Teachers Program')
    fav_teachers = []
    first_teacher = input('\nWho is your favorite Science Teacher: ').title()
    fav_teachers.append(first_teacher)
    second_teacher = input('Who is your favorite Math Teacher: ').title()
    fav_teachers.append(second_teacher)
    third_teacher = input('Who is your favorite English Teacher: ').title()
    fav_teachers.append(third_teacher)
    fourth_teacher = input('Who is your favorite Filipino Teacher: ').title()
    fav_teachers.append(fourth_teacher)
    # Teachers Ranking
    print('\nYour favorite teachers are ranked are: ' + str(fav_teachers))
    fav_teachers.sort()
    print('Your favorite teachers alphabetically are: ' + str(fav_teachers))
    fav_teachers.sort(reverse= True)
    print('Your favorite teachers in reverse alphabetical order are: ' + str(fav_teachers))
    fav_teachers.sort()

    # Top teachers
    print('\nYour top two teachers are: ' + str(fav_teachers[0]) + " " + str(fav_teachers[1]))
    print('Your next two favorite teachers are:' + str(fav_teachers[2])+ " " + str(fav_teachers[3]))
    print('Your last favorite teacher is: ' + str(fav_teachers[3]))
    print('You have a total of ' + str(len(fav_teachers)) + ' teachers')
    # Removed Teacher
    removed = fav_teachers.pop(0)
    print('\nOops, ' + str(removed)+ 'is no longer your first favorite teacher')
    new = input('Who is your new favorite teacher: ')
    fav_teachers.append(new)
    print('\nYour favorite teachers are ranked are: ' + str(fav_teachers))
    fav_teachers.sort()
    print('Your favorite teachers alphabetically are: ' + str(fav_teachers))
    fav_teachers.sort(reverse= True)
    print('Your favorite teachers in reverse alphabetical order are: ' + str(fav_teachers))
    fav_teachers.sort()
    print('\nYour top two teachers are: ' + str(fav_teachers[0]) + " " + str(fav_teachers[1]))
    print('Your next two favorite teachers are:' + str(fav_teachers[2])+ " " + str(fav_teachers[3]))
    print('Your last favorite teacher is: ' + str(fav_teachers[3]))
    print('You have a total of ' + str(len(fav_teachers)) + ' teachers')

# For loops programs

def binary_hex_converter():
    # Binary/Hexadecimal Converter App
    print('Welcome to the Binary/Hexadecimal Converter App')
    # Get user info
    user = int(input('\nCompute binary and hexadecimal values up to the following decimal: '))
    decimal_list = list(range(1,user+1))
    binary = []
    hexadecimal = []
    for dex in range(user):
        binary.append(bin(dex))
        hexadecimal.append(hex(dex))
    print("Generating lists... Complete!")

    # Making slices
    print('\nUsing slices, we will now show a portion of each list')
    dec_start =int(input('What decimal num would you like to start at?: '))
    dec_stop =int(input('What decimal number would you like to stop at?:'))
    # Getting the output
    print('\nDecimal values from ' + str(dec_start) + ' to ' + str(dec_stop))
    for num in decimal_list[dec_start-1:dec_stop]:
        print(num)
    print('\nBinary values from ' + str(dec_start) + ' to ' + str(dec_stop))
    for num in binary[dec_start-1:dec_stop]:
        print(num)
    print('\nHexadecimal values from ' + str(dec_start) + ' to ' + str(dec_stop))
    for num in hexadecimal[dec_start - 1:dec_stop]:
        print(num)
    # list Generated
    input('Press Enter to see all values from 1 '+ ' to ' + str(user))
    print('Decimal ----Binary------Hexadecimal')
    print('------------------------------------')
    for d,b,h in zip(decimal_list, binary, hexadecimal):
        print(str(d) + '-----' + str(b) + '------' + str(h))


def quadratic_equation_solver():
    # Quadratic Equation Solver App
    print('Welcome to the Quadratic Equation Solver App')
    print('\nA quadratic equation is of the form ax^2 + bx + c = 0')
    print('Your solutions can be real or complex numbers.')
    print('A complex number has two parts: a + bj')
    print('Where a is the real portion and bj is the imaginary portion.')

    # Get user info
    equations =int(input('\nHow many equations would you like to solve today?:'))
    # loop
    for num in range(equations):
        print('Solving Equation #' + str(num+1))
        print('--------------------------')
        # Getting value
        value_a = float(input('Please enter your value of a(coefficient of x^2): '))
        value_b = float(input('Please enter your value of b(coefficient of x): '))
        value_c = float(input('Please enter your value of c(coefficient): '))
        formula1 =(-value_b + cmath.sqrt(value_b**2 - 4*value_a*value_c))/(2*value_a)
        formula2 = (-value_b - cmath.sqrt(value_b ** 2 - 4 * value_a * value_c)) / (2 * value_a)
        print('The solution to ' + str(value_a) + 'x^2 '+' + ' + str(value_b) + 'x ' + ' + ' + str(value_c) + ' are ')
        print('\n\tx1 = ' + str(formula1))
        print('\tx2 = ' + str(formula2))
    print('Thank you for using the Quadratic Equation Solver App. Goodbye.')


def factorial_calc():
    # Factorial Calculator
    print('Welcome to Factorial Calculator App')
    # Get user input
    num= int(input('\nWhat number would you like to compute the factorial of?: '))
    print(str(num) + '!= ', end='')
    for number in range(1, num):
        print(number, end="*")
    print(num)
    # Formula
    formula = math.factorial(num)
    print('Here is the result from the math library: ')
    print('The factorial of ' + str(num) + ' is ' + str(formula) + '!')
    # Own formula
    own_formula = 1
    for i in range(1,num+1):
        own_formula *= i
    print("\nHere is the result from my own algorithm: ")
    print('The factorial of ' + str(num) + ' is ' + str(own_formula) + '!')
    # Summary
    print('\nIt is shown twice that ' + str(num) + '!' + ' = ' + str(formula))


def fibonacci_calc():
    # Fibonacci Calculator
    print('Welcome to the Fibonacci Calculator App')
    # Get user info
    digits = int(input('\nHow many digits of the Fibonacci Sequence would you like to compute?: '))
    # list
    numbers = [1,1]
    for element in range(digits-2):
        fib = numbers[element] + numbers[element+1]
        numbers.append(fib)
    # Display output
    print('\nThe first ' + str(digits) + ' numbers of the Fibonacci sequence are: ')
    for number in numbers:
        print(number)
    # Compute for golden Ratio
    golden = []
    print('The corresponding Golden Ratio values are: ')
    for i in range(len(numbers)-1):
        ratio = numbers[i+1]/numbers[i]
        golden.append(ratio)
    # Display Golden Ratio
    print('The corresponding Golden Ratio values are: ')
    for ratio in golden:
        print(ratio)
    print("\nThe ratio of consecutive Fibonacci terms approaches Phi; 1.618...")


def average_calculator():
   # Average Calculator app
    print('Welcome to the Average Calculator App')
    # Get user input
    grades = []
    name = input('What is your name?: ').title()
    input_grades = int(input('How many grades would you like to enter?: '))
    # Adding grades to list
    for grade in range (1,input_grades+1):
        add_grades = int(input('Enter grade: '))
        grades.append(add_grades)
    # Sorting list
    grades.sort(reverse= True)
    print('\nGrades Highest to Lowest:')
    for grade in grades:
        print(grade)
    # Summary and Getting Average
    avg = sum(grades)/ len(grades)
    avg = round(avg, 2)
    print('\n' + name + ' Grades Summary:')
    print('\tTotal number of Grades: ' + str(input_grades))
    print('\tHighest Grade: ' + str(max(grades)))
    print('\tLowest Grade: ' + str(min(grades)))
    print('\tAverage: ' + str(avg))

    # Desired avg
    desired_avg = float(input('\nWhat is your desired average: '))
    want_grade = desired_avg*(len(grades)+1) - sum(grades)
    want_grade = round(want_grade, 2)
    print('Goodluck Mike!\nYou will need to get a ' + str(want_grade) + ' on your next assignment to earn ' + str(desired_avg) + ' average.')

    # New
    new_grades = grades[:]
    print('\nLets see what your average could have been if you did better/worse on an assignment')
    grade_change = int(input('What grade would you like to change: '))
    new_grades.remove(grade_change)
    new_grade = int(input('What grade would you like to change ' + str(grade_change) + ' to: '))
    new_grades.append(new_grade)
    # New sorted Grades
    new_grades.sort(reverse= True)
    print('\nGrades Highest to Lowest:')
    for grade in new_grades:
        print(grade)
    # New summary
    new_avg = sum(new_grades)/ len(new_grades)
    new_avg = round(new_avg, 2)
    print('\n' + name + ' Grades Summary:')
    print('\tTotal number of Grades: ' + str(input_grades))
    print('\tHighest Grade: ' + str(new_grades[0]))
    print('\tLowest Grade: ' + str(new_grades.pop()))
    print('\tAverage: ' + str(new_avg))
    print('\nYour new Average would be a ' + str(new_avg) + ' compared to your real average of ' + str(avg))
    ans = new_avg - avg
    ans = round(ans,2 )
    print('That is a change of ' + str(ans) + ' points!')
    # Recall
    print('\nToo bad your original grades are still the same!')
    print(grades)
    print('You should go ask for extra credit!')

# Conditionals Programs

def shipping_program():
    # Shipping accounts program
    usernames = ['abecharles','charlesabe', 'darylusow', 'elijayari']
    print('Welcome to the shipping accounts program')
    # Getting usernames
    user = input('\nHello, What is your username?: ')
    if user in usernames:
        print('Hello, ' + user.title() + '.' + ' Welcome back to your account.')
    # Shipping prices
        print('\nShipping orders 0 to 100: ' + '  \t$5.10 each')
        print('Shipping orders 100 to 500: ' + '\t$5.00 each')
        print('Shipping orders 500 to 1000: ' + '\t$4.95 each')
        print('Shipping orders over 1000: ' + '  \t$4.80 each')
    # Get user items to ship
        items = int(input('\nHow many items would you like to ship?: '))
        if items <= 100:
            cost = 5.10
        elif items <= 500:
            cost = 5.00
        elif items <= 1000:
            cost = 4.95
        else:
            cost = 4.80
        ship_formula = items * cost
        ship_formula = round(ship_formula, 2)

        print('To ship ' + str(items) + ' items it will cost you ' +'$' + str(ship_formula) + ' at ' + '$' + str(cost) + ' per item')
        order = input('\nWould you like to place this order? (y/n): ').upper()
        if order == 'Y':
            print('Okay, Shipping your ' + str(items) + ' items')
        else:
            print('Okay, no order is being placed at this time')
    else:
        print('Sorry, You are not registered!')


def coin_toss():
    # Coin toss app
    print('Welcome to the Coin Toss App')
    print('\nI will flip a coin a set number of times.')
    # Get user input
    flip = int(input('How many time would you like me to flip the coin?: '))
    see_result = input('Would you like to see the result each flip?(y/n): ').lower()
    print('\nFlipping!!!')
    # container for heads and tails
    head = 0
    tails = 0
    # Loop for the Flipping
    for flipping in range(flip):
        coin = random.randint(0,1)
        if coin == 0:
            head += 1
            if see_result.startswith('y'):
                print('HEADS')
        else:
            tails += 1
            if see_result.startswith('y'):
                print('TAILS')
        if head == tails:
            print('At ' + str(flip) + ' flips, the number of heads and tails were equal at ' + str(head+1) + ' each')
    # Percentage
    heads_percent = round(100*head / flip, 2)
    tails_percent = round(100 * tails / flip, 2)
    # Results
    print('Result of Flipping a coin ' + str(flip) + ' times')
    print('\nSide' + '\t\tCount' + '\t\tPercentage')
    print('Heads ' +'\t\t' +  str(head) + '/' + str(flip) + '\t\t\t' + str(heads_percent) + ' %')
    print('Tails ' + '\t\t' + str(tails) + '/' + str(flip) + '\t\t\t' + str(tails_percent) + ' %')


def voters_registration():
    # Voter Registration App
    print('Welcome to the Voter Registration App!')
    # Get user input
    name = input('Please Enter your name: ').title()
    age = int(input('Please enter your age: '))
    # Political parties
    parties = ['Republican', 'Democratic', 'Independent', 'Libertarian', 'Green']
    # Check if user is 18+ old
    if age >= 18:
        print('Congratulations ' + name + '! You are old enough to register to vote')
        # To display parties
        for party in parties:
            print('\n-' + party)
        # Ask user to join
        join_party = input('What party would you like to join?: ').title()
        # Results
        if join_party in parties:
            if join_party == 'Republican' or join_party == 'Democratic':
                print('\nCongratulations ' + name + '! You have joined the ' + join_party + ' party!')
                print('That is a major party!')
            elif join_party == 'Independent':
                print('\nCongratulations ' + name + '! You have joined the ' + join_party + ' party!')
                print('You are independent now!')
            else:
                print('\nCongratulations ' + name + '! You have joined the ' + join_party + ' party!')
                print('That is not a major party but congratulations!!')
        else:
            print("That is not given party.")

    else:
        print('\nYou are not old enough to register to vote.')


def guessing_app():
    # Guess My Number App
    print('Welcome to the Guess My Number App')
    # Get user input
    name = input('\nWhat is your name?: ').title()
    # The number that will guess
    print('Well ' + name + ', I am thinking of a number between 1 and 50.')
    number = random.randint(1, 50)
    guess = 5
    # Main loop
    for guesses in range(guess):
        guess_input = int(input('\nTake a guess:'))
        if guess_input < number:
            print('Your guess is too low.')
        elif guess_input > number:
            print('Your guess is too high.')
        else:
            break
    # Results
    if guess_input == number:
        print('Good job, ' + name + '!, You guessed my number in ' + str(guesses) + ' guesses.')
    else:
        print('\nGame Over. The number I was thinking of was ' + str(number))


def rps_app():
    # Rock,Paper,Scissors App
    print('Welcome to Rock, Paper,Scissors App')
    # Get user input
    rounds = int(input('\nHow many rounds would you like to play?: '))
    # Moves
    moves = ['rock', 'paper', 'scissors']
    # Holds the scores of player and computer
    player = 0
    computer = 0
    # Main loop
    for round in range (rounds):
        print('\nRound ' + str(round+1))
        print('\tPlayer: ' + str(player) + '\tComputer: ' + str(computer))
        # Computer moves
        comp_num = random.randint(0, 2)
        comp_moves = moves[comp_num]
        # Player moves
        p_move = input('Time to pick... rock,paper,scissors: ').lower().strip()
        # Check winner
        if p_move in moves:
            print('\tComputer: ' + comp_moves)
            print('\tPlayer: ' + p_move)
            # Rock
            if p_move == 'rock' and comp_moves == 'rock':
                winner = 'Tie'
                phrase = 'It is, a tie, how boring!'
            elif p_move == 'rock' and comp_moves == 'paper':
                winner = 'Computer'
                phrase = 'Paper covers rock'
            elif p_move == 'rock' and comp_moves == 'scissors':
                winner = 'Player'
                phrase = 'Rock breaks scissors'
            # Paper
            elif p_move == 'paper' and comp_moves == 'paper':
                winner = 'Tie'
                phrase = 'It is a tie, how boring'
            elif p_move == 'paper' and comp_moves == 'rock':
                winner = 'Player'
                phrase = 'Paper covers Rock'
            elif p_move == 'paper' and comp_moves == 'scissors':
                winner = 'Computer'
                phrase = 'Scissors cut paper!'
            # Scissors
            elif p_move == 'scissors' and comp_moves == 'scissors':
                winner = 'Tie'
                phrase = 'It is a tie, how boring'
            elif p_move == 'scissors' and comp_moves == 'rock':
                winner = 'Computer'
                phrase = 'Rock breaks Scissors'
            elif p_move == 'scissors' and comp_moves == 'paper':
                winner = 'Player'
                phrase = 'Scissors cut Paper'
            else:
                print('Round Not calculated')
                winner = 'Tie'
            print('\t' + phrase)
            # Display Winner
            if 'Player' == winner:
                print('\tYou win round ' + str(round+1))
                player += 1
            elif 'Computer' == winner:
                print('\tComputer win round ' + str(round+1))
                computer += 1
            else:
                print('\tThe Game is tie')
        else:
            print('Invalid move. Computer score')
            computer += 1
    # Results
    print('\nFinal Game Results')
    print('\tRound Played: ' + str(round + 1))
    print('\tPlayer Score: ' + str(player))
    print('\tComputer Score: ' + str(computer))
    if player > computer:
        print('\tWinner: Player!!')
    elif computer > player:
        print('\tWinner: Computer :((')
    else:
        print('\tWinner: Tie!!')


# Dictionary Programs

def thesa_app():
# Thesaurus App
    thesa = {
        'hot': ['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
        'cold': ['chilly', 'cool', 'freezing', 'frigid', 'polar'],
        'happy': ['content', 'cheery', 'jovial', 'merry', 'jocular'],
        'sad': ['unhappy', 'downcast', 'miserable', 'glum', 'melacholy']
        }
    print('Welcome to the Thesaurus App')
    # Displaying the key in thesa
    print('\nHere are the words in the thesaurus:')
    for keys in thesa.keys():
        print( "-" + keys)
    # Get user input
    user_word = input('What word would you like a synonym for?: ').lower()
    # Check if the word is in dict
    if user_word in thesa.keys():
        key = thesa[user_word]
        synonym = random.choice(key)
        print('The synonym of ' + user_word + ' is ' + synonym + '.')
    else:
        print("I'm sorry that word is not currently in Thesaurus.")
    # Ask user if they want to see the Thesaurus
    see_thesa = input('\nWould you like to see the whole Thesaurus?(Y/N)?: ').lower()

    if see_thesa == 'y':
        for key, values in thesa.items():
            print('\n' + key.title() + ' synonyms are:')
            for value in values:
                print('\t-' + value)
    else:
        print('\nI hope you enjoyed the program. Thank you!')


def database_admin_program():
    # Database Admin Program
    print('Welcome to the Database Admin Program')
    log_on_information = {'admin00': '1234567890',
                          'charlesabe': 'qwertyuiop',
                          'abeastig': 'charlesabe',
                          'darylusow': 'darylusow',
                          'elijahyari': 'elijahyari'}

    # Get user input
    username = input('Enter your username: ').lower().strip()
    # Check if username is in the database
    if username in log_on_information.keys():
        password = input('Enter you password: ')
        # Check if the password correct
        if password in log_on_information[username]:
            print('Hello ' + username + '! You are logged in')

            # Check if the user is the admin
            if username == 'admin00':
                print('\nHere is the current user ')
                for key, value in log_on_information.items():
                    print('Username: ' + key + '  \t\tPassword: ' + value)
            else: # If the user is not admin ask if they want to change pass
                change_pass = input('\nWould you like to change your password?(Y/N): ').lower()

                if change_pass == 'y':
                    new_pass = input('What would you like your new password to be? (8 characters long): ')
                    # Check in the new pass is 8 character long

                    if len(new_pass) < 8:
                        print(new_pass + ' not the mininum eight characters.')
                        print('\n' + username + ' your password is ' + password)
                    else:
                        print('\n' + username + ' your password is' + new_pass)

                else:
                    print('\nThank you, goodbye!')
        else:
            print('Your password is wrong.')
    else:
        print('The username is not in the database.')


def yes_no_poll():
    print('Welcome to the Yes or No Issue Polling App')
    # Getting the issue
    issue = input('\nWhat is the yes or no you will be voting on today?: ')
    num_voters = int(input('What is the number of voters you will allow on the issue?: '))
    password = input('Enter the password for polling results: ')
    # Define the number of yes and no
    vote_yes = 0
    vote_no = 0
    # Dictionary that holds the result
    results = {}
    # Main loop
    for voters in range(num_voters):
        name = input('\nEnter your full name: ').title()
        # Check if name is in Dictionary
        if name in results:
            print('You have voted, you cannot vote again')
        else:
            print('Here is out issue: ' + issue)
            voting = input('Is it yes or no?: ').lower().strip()
            if voting == 'yes' or voting == 'y':
                choice = 'yes'
                vote_yes += 1
            elif voting == 'no' or voting == 'n':
                choice = 'no'
                vote_no += 1
            else:
                print('That is not yes or no, but okay')


            # Adding the elements in Dictionary
            results[name] = choice
            print('Thank you ' + name + '!, Your vote of ' + voting + ' has been recorded but it will not affect the poll')

    # Display the result
    total_voters = len(results.keys())
    print('\nThe following ' +  str(total_voters) +  ' people voted')
    for keys in results.keys():
         print(keys)
    print('\nOn the following issue: ' + issue)
    if vote_yes > vote_no:
        print('Yes win! ' + str(vote_yes) + ' votes to ' + str(vote_no))
    elif vote_yes < vote_no:
         print('No wins!' + str(vote_no) + ' votes to ' + str(vote_yes))
    else:
         print('It was a tie!' + str(vote_yes) + ' votes to ' + str(vote_no))

    # To See the Full results
    input_pass = input('\nTo see the voting results enter the admin password: ')
    if input_pass == password:
        for key, value in results.items():
            print('Voter: ' + key + ' \t\t' + 'Vote: ' + value)


# While loops Programs

def factor_generator_app():
    # Factor Generator App
    print('Welcone to the Factor Generator App')
    factor_on = True
    while factor_on:
        # Get user input
        factor_num = int(input('\nEnter a number to determine all the factors of that number: '))

        # List for factors
        factors = []
        for num in range(1, factor_num+1):
            if factor_num % num == 0:
                factors.append(num)
        # Display the factors of given number
        print('\nThe factors of ' + str(factor_num) + ' are:')
        for factor in factors:
            print(factor)
        # Summary
        print('\nIn summary:')
        for factor in range(int(len(factors)/2)):
            print(str(factors[factor]) + ' * ' + str(factors[-factor - 1]) + ' = ' + str(factor_num))
        # If run again
        choice = input('Run again?(y/n): ').lower()
        if choice != 'y':
            factor_on = False
            print('Thank you for using the program!')


def even_odd():
    # Even Odd Number Sorter App
    print('Welcome to the Even Odd Number Sorter App')
    running = True
    # Main loop
    while running:
        # Get user input
        numbers = input('\nEnter in a string of numbers separated by a comma(,): ')
        numbers.replace(' ', '')
        # Make the string into list
        num_list = numbers.split(',')
        # Hold the even and odds value
        evens = []
        odd = []
        # Display Results
        print('\n---Result Summary---')
        for number in num_list:
            number = int(number)
            if number % 2 == 0:
                evens.append(number)
                print('\t' + str(number) + " is an even number")
            else:
                odd.append(number)
                print('\t' + str(number) + ' is an odd number')
        # Sort the list of evens and adds
        evens.sort()
        odd.sort()
        # Display the sorted even num and odd num
        print('\nThe following ' + str(len(evens)) + ' numbers are even:')
        for even in evens:
            print(even)
        print('\nThe following ' + str(len(odd)) + ' numbers are odd:')
        for odds in odd:
            print(odds)
        # Ask user if run the program
        choice = input('\nWould you like to run the program again?(y/n): ').lower()
        if choice != 'y':
            running = False
            print('Thank you for using the program. Goodbye')


def prime_number_app():
    # Prime Number App
    print('Welcome to the Prime Number App')
    running = True

    while running:
        print('\nEnter 1 to determine if a specific number is prime')
        print('Enter 2 to determine all prime numbers within a set range')
        # Get user input
        choice = int(input('Enter your choice 1 or 2?: '))

        if choice == 1:
            number = int(input('\nEnter a number to determine if it is prime or not: '))
            prime_status = True
            for numbers in range(2, number):
                # Check if prime
                if number % numbers == 0:
                    prime_status = False
                    break

            # Print summary
            if prime_status:
                print(str(number) + ' is prime!')
            else:
                print(str(number) + ' is not prime!')

        elif choice == 2:
            lower_bound = int(input('\nEnter the lower bound of your range: '))
            upper_bound = int(input('Enter the upper bound of your range: '))

            prime = []

            # Time of process
            start_time = time.time()

            for i in range(lower_bound, upper_bound + 1):
                # Check if current number is greater than 1
                if i > 1:
                    prime_status = True
                    for numbers in range(2, i):
                        # Check if prime
                        if i % numbers == 0:
                            prime_status = False
                            break
                else:
                    prime_status = False
                # Adding the current prime to the list
                if prime_status:
                    prime.append(i)

            # End time
            end_time = time.time()
            # Calculation it took
            delta_time = end_time - start_time
            delta_time = round(delta_time, 4)

            # Display Results
            print('\nCalculations took a total of ' + str(delta_time) + ' seconds')
            print('The following numbers between ' + str(lower_bound) + ' and ' + str(upper_bound) + ' are prime.')
            input('Press Enter to continue.')

            for primes in prime:
                print(primes)
        else:
            print('Your choice is invalid')

        # If user want to continue
        is_continue = input('\nWould you like to run the program again(y/n): ').lower()
        if is_continue != 'y':
            running = False
            print('Thank you for using the program!. Goodbye')


def guessing_word():

    # Guess My Word App
    print('Welcome to the Guess My Word App')

    game_dict = {
        'color': ['red', 'blue', 'orange', 'yellow', 'peach', 'brown'],
        'brand of cellphones': ['samsung', 'iphone', 'xiaomi', 'redmi', 'oppo', 'huawei'],
        'sports': ['basketball', 'soccer', 'baseball', 'volleybal', 'table tennis', 'badminton']
        }
    game_keys = []
    # To append the keys in the list
    for keys in game_dict.keys():
        game_keys.append(keys)

    # Main loop
    playing = True

    while playing:
        # Hold the values and keys in the dict
        game_category = game_keys[random.randint(0, len(game_keys) - 1)]
        game_word = game_dict[game_category][random.randint(0, 5)]

        # Blank word
        blank_word = []
        for letters in game_word:
            blank_word.append('-')

        print('\nGuess a ' + str(len(game_word)) + ' letter word from the following category: ' + game_category.title())

        # Number of Guesses
        guess = ''
        guess_count = 0
        while guess != game_word:
            print(''.join(blank_word))

            # Get user input
            guess = input('\nEnter your guess: ').lower().strip()
            guess_count += 1

            # Check if the word is correct
            if guess == game_word:
                print('\nYou guess my word in ' + str(guess_count) + ' guesses')
                break
            else:
                print('Your guess is wrong. Let us reveal a letter to help you')
                guess_wrong = True
                while guess_wrong:
                    letter_index = random.randint(0, len(game_word) - 1)
                    if blank_word[letter_index] == '-':
                        blank_word[letter_index] = game_word[letter_index]
                        guess_wrong = False

        # Ask user if they want to play again
        choice = input('\nDo you want to play again?(y/n): ').lower()
        if choice != 'y':
            playing = False
            print('Thank you for playing. Bye!')

# Function Programs
# Tic Tac Toe App

def tic_tac_toe():
    def draw_board(board):
        """Draw the board"""
        print(board[0] + '|' + board[1] + '|' + board[2])
        print(board[3] + '|' + board[4] + '|' + board[5])
        print(board[6] + '|' + board[7] + '|' + board[8])


    def get_player_input(player, board):
        """Get the position the user"""
        while True:
            move = int(input(f'{player}: Where would you like to place your piece(1-9): '))

            if move > 0 and move < 10:
                if board[move - 1] == '-':
                    return move
                else:
                    print('The spot has already been occupied.')
            else:
                print('Your move is not a spot on the board.')


    def place_marker(player, move, board):
        """Placing the move on to the board"""
        board[move - 1] = player


    def check_winner(board, player):
        """Checking the winner"""
        return ((board[0] == player and board[1] == player and board[2] == player) or
                (board[3] == player and board[4] == player and board[5] == player) or
                (board[6] == player and board[7] == player and board[8] == player) or
                (board[0] == player and board[3] == player and board[6] == player) or
                (board[1] == player and board[4] == player and board[7] == player) or
                (board[2] == player and board[5] == player and board[8] == player) or
                (board[0] == player and board[4] == player and board[8] == player) or
                (board[2] == player and board[4] == player and board[6] == player))

    def main():
        print('Welcome to the Tic Tac Toe App')
        print('' * 2)
        # player var
        player1 = 'X'
        player2 = 'O'
        # board
        c_list = ['-'] * 9
        n_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        # Displaying the Board
        draw_board(n_list)
        print('' * 5)
        draw_board(c_list)

        # Main loop
        playing = True
        while playing:
            move = get_player_input(player1, c_list)
            place_marker(player1, move, c_list)

            # display the current board
            draw_board(n_list)
            print('' * 5)
            draw_board(c_list)

            # Check if there is winner
            if check_winner(c_list, player1):
                print('\nPlayer 1 wins')
                break
            elif '-' not in c_list:
                print('The game is tie!')
                break

            # Players 2 turn
            else:
                move = get_player_input(player2, c_list)
                place_marker(player2, move, c_list)

                # display the current board
                draw_board(n_list)
                print('' * 5)
                draw_board(c_list)

                # Check if there is winner
                if check_winner(c_list, player1):
                    print('\nPlayer 2 wins')
                    break











































































