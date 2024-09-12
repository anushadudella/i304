"""
Informatics 304: Programming for Informatics (Fall 2021)
HW1 - 8 Problems, 100 points total

Each problem is contained in a function that is invoked at the bottom of this file.
If you do not want to run the code for a given problem, simply comment out that 
problem number's function at the bottom of this file.

Each problem contains an initial print statement that shows the problem number.  
DO NOT CHANGE THIS. Add your code below the instructions for the problem.


Notes on Using Visual Studio Code (VSCode)
------------------------------------------
IF COMMENTS ABOVE ARE NOT WRAPPING IN VSCode, GO TO SETTINGS (GEAR ICON IN THE LOWER 
LEFT), TYPE "wrap" IN THE SEARCH BOX, AND SET "Editor: Word Wrap" TO "on"


Notes on Grading
----------------
The point value of each problem is noted in a comment above the problem 

Producing the correct answer alone is not enough by itself to receive full-credit. Just as it's important to show your work in completing math problems, your solution should be easy for another person to read and understand both your approach (i.e., *how* you tried to solve the problem) as well as *why* you pursued that approach. 

Writing meaningful comments is an important part of this: explaining what you are *intending* to do at each step, even if the actual translation of this intent into actual Python ultimately proves erroneous. More specifically, you should write your human-readable "pseudocode" as comments first, convince yourself that your "algorithm" in pseudocode is correct, and then translate your pseudocode into real Python code (that the computer can execute). 

Using meaningful variables names also helps make your Python program clearer to others and more "self-documenting". 

In grading each problem, the AA will ask questions such as:

* Does your program run without errors?

* How correct is the solution: all, mostly, some, none? 

* For partial credit, how much of the problem was attempted?

* Did you "show your work" in a way the AA can understand. For example, in real-world programming job, would another developer that was trying to make sense of your code be able to do so, in order to extend your code with new functionality, or to find and fix any "bugs" in your code)?

  - Did you include comments, and more specifically the pseudocode for your algorithm to solve the problem?

  - Did you use meaningful variable names?

* Did you follow class "coding conventions":

  - Did you use snake_case for naming variables, and UPPERCASE names for constants? 

  - Did you use whitespace (blank lines and spaces) to make your code readable? 

"""
import turtle

# 0 points (already solved demonstration)
def problem_0():
    print('\n Problem 0 \n')
    """
    This is a demonstration example only; it is already solved for you.
    
    Note that you must indent each line. This is because in Python, indentation effects program interpretation, so if you do not indent your Python code consistently, it will fail to run with an error, or run but produce erroneous output.

    Example problem: output the sum of 2 and 3
    """
    # YOUR SOLUTION GOES HERE -- THIS ONE IS SOLVED FOR YOU!
    sum = 2 + 3
    print(f'Sum = {sum}')


# 10 points
def problem_1():
    print('\n Problem 1 \n')
    """
    In mathematics long division, standard terminology is that the 

        Dividend / Divisor = Quotient and Remainder.  
        
    For example, 7 / 2 = 3 remainder 1

    Prompt the user for two integer inputs. Store these in variables named dividend and divisor. 

    Print the integer quotient (ie, the results of integer division) and the remainder.

    To verify your program is working correctly, test it by running it on different inputs and verifying that it produces the correct, expected output in case. To be clear, this testing is not code for you to submit, but manual testing for you to perform to verify the accuracy of your program.  For example consider the test cases below.

    Test Case(s):
        * 1/3 = 0 remainder 1 
        * 11/3 = 3 remainder 2
        * 5/2 = 2 remainder 1
    """
    # YOUR SOLUTION GOES HERE

    # Declaring variables and asking the user for input (for the dividend and divisor)
    dividend = int(input('Enter your dividend: '))
    divisor = int(input('Enter your divisor: '))

    # Calculating the integer divison and storing it in a variable "quotient"
    quotient = dividend // divisor

    # Calculating the remainder of divison ad storing it in a variable "remainder"
    remainder = dividend % divisor 

    # Printing both the quotient and remainder 
    print('Your quotient is: ', quotient)
    print('Your remainder is: ', remainder)

# 10 points
def problem_2():
    print('\n Problem 2 \n')
    """
    A car’s miles-per-gallon (MPG) can be calculated with the following formula:

        MPG = miles driven / gallons of gas used
    
    Write a program that asks the user for the number of miles driven and the gallons of gas used. It should calculate the car's MPG and display the result.

    Assume floating-point value inputs and output.
    """
    # YOUR SOLUTION GOES HERE

    # Declaring variables and asking the user for input (for the miles driven and gallons of gas used)
    miles_driven = float(input('Enter the number of miles you have driven: '))
    gallons_gas = float(input('Enter the gallons of gas used: '))

    # Calculating the MPG (miles driven by the gallons of gas) and storing it in a variable "MPG"
    MPG = miles_driven / gallons_gas

    # Printing the MPG
    print('Your miles-per-gallon or MPG is: ', MPG)


# 15 points
def problem_3():
    print('\n Problem 3 \n')
    """
    A customer in a store purchases three items. Write a program that asks for the price of each item, then displays the subtotal, the amount of sales tax, and the total (subtotal + tax). Assume the sales tax is 7%.

    Your output should be a proper monetary amount in US dollars, i.e., don't forget to include a $ and to round the output to two decimals places (cents).
    """
    # YOUR SOLUTION GOES HERE

    # Asking the user for inputs regarding the first three purchase prices and storing in variables item 1, 2, and 3 correspondingly
    item_one = float(input('Enter the price of the first item you have purchased: '))
    item_two = float(input('Enter the price of the second item you have purchased: '))
    item_three = float(input('Enter the price of the third item you have purchased: '))

    # Calculating the subtotal, sales tax of 7%, and the final total of the items
    subtotal = item_one + item_two + item_three
    sales_tax = subtotal * 0.07
    total = sales_tax + subtotal

    # Printing the subotal of the items, amount of sales tax, and the total (including sales tax) rounded to two decimal places
    print('Your subtotal for the items is: $', round(subtotal,2))
    print('Your amount of sales tax is: $', round(sales_tax,2))
    print('Your total is: $', round(total,2))


# 15 points
def problem_4():
    print('\n Problem 4 \n')
    """
    A cookie recipe calls for the following ingredients:
        1.5 cups of sugar
        1 cup of butter
        2.75 cups of flour

    The recipe produces 48 cookies using these ingredients. Write a program that asks the user how many cookies he or she wants to make, then displays the number of cups of each ingredient needed to produce the specified number of cookies. 

    Assume the input number of cookies is an integer value. 

    Output floating-point values to 2-degrees of precision.    
    """
    # YOUR SOLUTION GOES HERE

    # Asking the user how many cookies they want to make and storing it in corresponding variable
    cookie_number = float(input('How many cookies do you want to make?: '))

    # Calculating the unit amount for sugar, butter, and flour and storing it in corresponding variables
    singular_sugar = 1.5/48 
    singular_butter = 1/48
    singular_flour = 2.75/48

    # Calculating the total sugar, butter, and flour needed based on user input * unit amounts 
    total_sugar = round((singular_sugar * cookie_number),2)
    total_butter = round((singular_butter * cookie_number),2)
    total_flour = round((singular_flour * cookie_number),2)

    # Printing the total sugar, butter, and flour amounts for the inputted cookie number
    print('For', cookie_number, 'cookies, you need', total_sugar, 'cups of sugar')
    print('For', cookie_number, 'cookies, you need', total_butter, 'cups of butter')
    print('For', cookie_number, 'cookies, you need', total_flour, 'cups of flour')


# 20 points
def problem_5():
    print('\n Problem 5 \n')
    """
    Chapter 2. Programming Exercise #14. "Compound Interest"

    Assume that the input for "n", the number of times per year that the interest is compounded" is an integer value, and that the input for "r", the annual interest rate, is a floating-point value such as 5.3 (indicating a 5.3% interest rate). The remaining inputs should also be floating-point values. 
    
    Your output should be a proper monetary amount in US dollars.
    """
    # YOUR SOLUTION GOES HERE

    # Asking the user how many times interest compounded, annual interest rate, principal amount, and a time period
    interest_compounded = int(input('How many times per year is your interest compounded?: '))
    annual_interest = float(input('What is the annual interest rate?: ')) / 100
    principal_amount = float(input('What is your principal amount?: ' ))
    time = float(input('How long is the time period? (in years): '))

    # Calculating the rate (annual interests by interest compounded) and time period (interest compounded multiplied by time) 
    rate = annual_interest / interest_compounded
    time_period = interest_compounded * time

    # Applying compound interest formula and calculating with user inputted amounts
    amount = principal_amount * (pow((1+rate), time_period))

    # Printing commpound interest amount 
    print('Your compound interest amount is: $', amount)


# # 15 points
def problem_6():
    print('\n Problem 6 \n')
    """
    Implement the following English turtle commands in Python:
   
    * use a turtle shape for the pen
    * prompt the user with a turtle dialog box for numeric input and save it in a variable named "distance"
    * move forward that amount
    * change the turtle's color to red
    * rotate 90 degrees left and move ahead by 50
    * change the size of turtle to 3
    * set the turtle to faster speed 5
    * pull up the turtle pen 
    * retrace the turtle's path back to its starting position
    * prompt the user with turtle dialog box for textual input and save in a variable "message"
    * write the message to the screen in blue text

    Keep the turtle window open until the user clicks on it.
    """
#     # YOUR SOLUTION GOES HERE

    # Setting up the turtle screen, background, and color 
    turtle.setup(1.0,1.0)   
    turtle.speed(1)         
    turtle.shape('turtle')
    turtle.color('purple')
    turtle.bgcolor('Black')

    # Asking the user for distance to move and storing it in corresponding variable
    distance = turtle.numinput("Let's move forward!", 'Enter a distance to move: ')
    # Moving the turtle forward for that specific distance
    turtle.forward(distance)

    # Changing fill color, pen color, direction, and size for turtle
    turtle.fillcolor('red')
    turtle.pencolor('red')
    turtle.left(90)
    turtle.forward(50)
    turtle.shapesize(3)
    turtle.speed(5)
    turtle.penup()
    turtle.pendown()
    turtle.goto(0,0)

    # Printing the user's message to the screen with requirements (blue text)
    message = turtle.textinput('Enter some text here!', 'Your message: ')
    message = message + "     "
    turtle.color('blue')
    turtle.write(message,False, "right", font=("Times", 30, "normal"))

    # Keeping window open until user clicks off of it
    turtle.exitonclick()

#15 points
def problem_7():
    print('\n Problem 7 \n')
    """
    Chapter 2. Programming Exercise #15. "Turtle Graphics Drawings"

    While the textbook shows six shapes to draw (2 columns, 3 rows), you only need to draw the upper-left shape: the rotated, connected squares (left column, 1st row)

    The left square should have a red border and be blue inside.  The right square should have a blue border and be red inside. The outline of each square should be 5 pixels wide.

    Keep the turtle window open until the user clicks on it.
    """
    # YOUR SOLUTION GOES HERE
    
    # Sets up window size to fill the screen, sets the width of the pen for frawing, sets the drawing speed to slowest (1)
    # Changes the turtle's shape to an arrow and the background of the turtle window to black
    turtle.setup(1.0,1.0)  
    turtle.width(5) 
    turtle.speed(1)  
    turtle.shape('arrow')
    turtle.bgcolor('black')

    # Sets the outline color for drawing, fill color for drawing
    turtle.color('blue')
    turtle.fillcolor('red')

    # Begins the process of filling the shape with the set fill color
    turtle.begin_fill()
    
    # Function takes the side length, fill color, line color, and number of turns
    def draw_filled_shape(side_length, fill_color, line_color, turns):
        turtle.color(line_color) # Sets the pen color (outline for shape)
        turtle.fillcolor(fill_color) # Sets the fill color for the shape
        turtle.begin_fill() # Begins filling the shape with the fill color
        for i in range(turns): # Loops for the number of sides (or turns)
            turtle.forward(side_length) # Moving the turtle forward by the given side length
            turtle.right(90) # Turning the turtle 90 degrees to form the edges of the shape
        turtle.end_fill() # Lastly, filling the shape with color

    turtle.goto(0,0) # Moves the turtle back to the starting position
    turtle.pendown() 
    turtle.left(50) 
    draw_filled_shape(200, 'red', 'blue', 4) # Function call for the right square 

    turtle.right(180) # Rotates the pen 180 degres to change direction for the other square 
    draw_filled_shape(200, 'blue', 'red', 4) # Function call for the left square

    turtle.exitonclick() # Keeps the window open until the user clicks on it


# OPTIONAL - up to 10 points EXTRA CREDIT
# Fix and document better
def problem_8():
    print('\n Problem 8 \n')
    """
    Creative Tutle (EXTRA CREDIT)

    Make something creative with Turtle: a drawing or an interactive program.  The only limit is your imagination!  See the Python turtle documentation online for additional commands you can use.  

    Grading: more creative, difficult, and/or effortful work will be rewarded with more extra credit points. 
    """
    # YOUR SOLUTION GOES HERE

    # Sets initial background color to white, sets speed to fast, and pen color to white (sets everything to default settings)
    turtle.bgcolor('white')
    turtle.speed(0)
    turtle.pencolor('white')

    # Prompts the user to design their own mandala with user inputs of radius, color, outline, and number of edges for the shape
    radius = turtle.numinput("Design your own mandala!", 'What should the radius be? Enter a valid number, please!')
    bg_color = turtle.textinput("Nice! Now let's add some color!", "What color should the background be? Enter a valid color, please!")
    turtle.bgcolor(bg_color)
    pen_color = turtle.textinput("Sweet! Pick the outline for the mandala!", "What should the pen color be? Enter a valid color, please!")
    turtle.pencolor(pen_color)
    sides_shape = turtle.numinput("What should the shape be?", "Enter a number starting from 3, please!")

    # Function takes a radius as a parameter
    # Draws the radius 15 times with a decreasing radius for the next iteration
    def draw_shape(radius):
        for i in range(15):
            turtle.circle(radius, steps=int(sides_shape)) # Draws a shape with the user specified number of sides from the input
            radius=radius-4

    def mandala_maker(): 
        for i in range(15): # Loops 15 times to create the mandala pattern
            draw_shape(radius) # Calls the draw_shape function with the user specified radius from the input
            turtle.left(26) # Rotates the turtle by 26 degrees to shift the next shape form slightly 

    mandala_maker() # Calls the function

    turtle.exitonclick() # Keeps the window open until the user clicks on it       

#===============================
# UNCOMMENT WHICHEVER PROBLEMS YOU WANT TO RUN! 

# Demonstration problem (already solved)
#problem_0()
# Main problems to complete
# problem_1()
# problem_2()
# problem_3()
# problem_4()
# problem_5()
# problem_6()
# problem_7()

# Extra credit
problem_8()