price = float(input("The price of your purchase is: "))

if price < 0.0:

    print ("Invalid dollar amount")
    
elif price >= 100.0:

    print ("You can save 40%")
    print (f"Your final price is: {price*0.6}")

elif price >= 75.0:

    print ("You can save 30%")
    print (f"Your final price is: {price*0.7}")

elif price >=50.0:
    
    print ("You can save 20%")
    print (f"Your final price is: {price*0.8}")

elif price >=25.0:

    print ("You can save 10%")
    print (f"Your final price is: {price*0.9}")

else:
    
    print ("No savings are available")
  
# Just as I said in question 5, this code is efficient because there are no nested if statements.
# Furthermore, the code determines the category of the user input, using only one condition for each if or elif