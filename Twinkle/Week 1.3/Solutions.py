# Problem 1

r = True
s = False
t = True
x = False


# Problem 2

day = int(input("Please enter a number between 1-7: "))
if day == 1:
    s = 'Sunday'
elif day == 2:
    s = 'Monday'
elif day == 3:
   s = 'Tuesday'
elif day == 4:
    s = 'Wednesday'
elif day == 5:
    s = 'Thursday'
elif day == 6:
   s = 'Friday'
elif day == 7:
    s = 'Saturday'
else:
    s = 'Invalid number'
print(s)

# Problem 3 

# a) Michael Jackson was an American singer and dancer.
# P: Michael Jackson was an American singer.
# Q: Michael Jackson was an American dancer.
# R: P ∧ Q

# b) b) Michael Jackson was a song writer but didn’t direct The Avangers.
# P: Michael Jackson was a song writer.
# Q: Michael Jackson didn’t direct The Avangers.
# R: P ∧ ¬Q

# c) If I am not spiderman, then I am batman.
# P: I am spiderman.
# Q: I am batman.
# R: ¬P → Q

# d) You will get your swimming diploma if and only if you didn’t fail the swimming test and know how to dive.
# P: you will get your swimming diploma.
# Q: you fail the swimming test.
# M: you know how to dive.
# R: P ↔ (¬Q ∧ M)
