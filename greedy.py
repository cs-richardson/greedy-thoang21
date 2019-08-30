"""
Tung Hoang - 08/30/19

This program ask user how much change is owned and calculate the least numbers
of coin needed to give the user. The coins value at 25, 10, 5, and 1 cents
"""
import math

# Coins value
quarter = 25
dime = 10
nickel = 5
penny = 1
numQuarter = numDime = numNickel = numPenny = 0

# Ask user for input
dollarMoney = float(input("How much change is owned? "))

# Convert the dollars into cents and round up if needed
centMoney = math.ceil(dollarMoney * 100)

# Finding out the number of quarters needed
if centMoney >= quarter:
    numQuarter = centMoney // quarter
    
    centMoney = centMoney  % quarter # Calculate the leftovers money)

# Finding out the number of dimes needed
if centMoney >= dime:
    numDime = centMoney // dime
    
    centMoney = centMoney % dime  # Calculate the leftovers money

# Finding out the number of nickels needed
if centMoney >= nickel:
    numNickel = centMoney // nickel
    
    centMoney = centMoney % nickel  # Calculate the leftovers money

# Finding out the number of pennies needed
numPenny = centMoney // penny

# Add the numbers of coins together
numCoin = str(numQuarter + numDime + numNickel + numPenny)

# Out put the least number of coins needed
print ("You need " + numCoin + " coins")
