#!/usr/bin/python

print "-------------------------------"
Title = "Life of My Remaing Dollars"
print Title
print "-------------------------------"
print ""
print "By answering the questions accurately, we can estimate how long you can live without a job!"

print "Total cash in your name"
print "<---------------------->"
total = input("How liquid are you? Checking + Savings + Cash >>> ")
print total

print "Now we need to know how much you spend each month"
print "Bills!"
print "<------->"
rent = input("how much is your rent? >>> ")
car = input("how sweet is your car? and insurance >>> ")
power = input("how much is your electricty >>> ")
cable = input("how much is your cable/internet >>> ")
food = input("how much do you spend on food >>> ")
gas = input("how much do you spend on gas >>> ")
entertainment = input("you should be looking for a job not partying. how much are you spending on entertainment >>> ")
recreation = input("don't lie to yourself, how much ar spending on drugs and/or alcohol >>> ")

Bills = rent+car+power+cable+food+gas+entertainment+recreation

print ("Your monthly bills total to an astonishing "+ str(Bills) + "!!!")

def daystobroke(Bills, total):
	dailycost = Bills/30
	life = total/dailycost

	
	return life;

dayz = raw_input("Type 'DAYZ' to execute the complex algorithm to find out how many days you can live without a job >>> ")

if (dayz == "DAYZ"):
	print "You have days to live!" , daystobroke(Bills=Bills, total=total)

else:
	print "do something else with your life"
