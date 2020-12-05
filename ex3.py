# Print the text
print ("I will now count my chickens:")

#Count Hens, 30 / 6 = 5, + 25 = 30; count rooster, 25 * 3 = 75, then
# remainder of 75 / 4 is 3 (18 3/4), so 100 - 3 = 97
print("Hens", 25.0 + 30.0 / 6.0)
print("Rooster", 100.0 - 25.0 * 3.0 % 4.0)

#Print the text
print("Now I will count the eggs:")

#Order of operations. First do the division, 1/4 = .25. The % is the
#remainder of 4/2, which is 0. So 3 + 2 (5) + 1 (6) -5 (1) + 0 (1) -.25 (.75)
# +6 = 6.75
print(3. + 2. + 1. - 5. + 4. % 2. - 1. / 4. + 6.)

#Print the text
print("Is it true that 3 + 2 < 5 -7?")

#Figure out if 5 < -2, it's not so print False
print(3. + 2. < 5. - 7.)

#Do the math to figure out the numbers
print("What is 3 + 2?", 3. + 2.)
print("What is 5 - 7", 5. - 7.)

#Print the text
print("Oh, that's why it's False.")

#Print the text
print("How about some more.")

#Now do it with greater than or equal or less than or equal
print("Is it greater?", 5. > -2.)
print("Is it greater or equal?", 5. >= -2.)
print("Is it less or equal", 5. <= -2.)
