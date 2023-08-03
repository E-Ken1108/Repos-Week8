# Code written by Kendrick Evans of CIS245 #

# Starting here is the definition of a primary function, which will contain the whole program #
def primary():

  # Here, we have the introduction of the beginning function, which will display an intro for the program #
  beginning()

  # After the intro is ran, we run a try function that will get the user input for how many miles they traveled, and will immediately put that number in a class to be used later #
  try:
    miles = int(input('How many miles did you travel? '))

    miles_conv(miles)

  # The except function will only occur an a user inputs a number that is not an integer, and will rerun the code with the displayed message #
  except:
    print('An error occured. Try entering the number of miles as a whole number.\n')
    primary()

#The definition of the beginning function, as seen in the beginning. This is what will be displayed first and foremost everytime the code is ran #

def beginning():
  print('This conversion will be helpful if you want to learn miles to kilometers')
  print('or are traveling outside of the United States where kilometers are most common.\n')
  print('Every mile is about 1.61 kilometers. \n')

# The meat of the code, this is where the computations are done. Since the miles should already be an integer, I added a round function for kilometers, rounding it to the nearest hundreth when it is displayedd to the user. 

def miles_conv(miles):
  kilometers = miles * 1.61
  print('You would have traveled', round(kilometers, 2), 'km by traveling', miles, 'miles.')

primary()