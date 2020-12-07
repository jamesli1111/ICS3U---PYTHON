mark = float(input("Enter your test mark: "))

#Version 1 of marks
print ("Version 1")
if mark > 84 and mark <=100:
    print ("Level 4")
else:
    if mark >=70 and mark <85:
        print ("Level 3")
    else:
        if mark >=60 and mark <70:
            print ("Level 2")
        else:
            if mark >=50 and mark <60:
                print ("Level 1")
            else:
                if mark >=0 and mark<50:
                    print ("Level R")
                else:
                    print ("Mark not in range")

print ("Version 2")
#Version 2 of marks
if mark > 84 and mark <=100:
    print ("Level 4")
elif mark >=70 and mark <85:
    print ("Level 3")
elif mark >=60 and mark <70:
    print ("Level 2")
elif mark >=50 and mark <60:
    print ("Level 1")
elif mark >=0 and mark<50:
    print ("Level R")
else:
    print ("Mark not in range")

print ("Version 3")
#Version 3 of marks
if mark > 100 or mark < 0:
    print ("Mark not in range")
elif mark >84:
    print ("Level 4")
elif mark >=70:
    print ("Level 3")
elif mark >=60:
    print ("Level 2")
elif mark >=50:
    print ("Level 1")
else:
    print ("Level R")

print ("Thank you and goodbye")

# a) No, the output of all different versions of code remains the same. Every code effectively does the same thing except with different lines of code.

# b) Version 3 of the code seems to be the most efficient and easiest to understand. 
# To begin, version 3 and 2 both use only one if statement. Comparatively, version 1 has five nested if statements.
# Now that we have determined why version 3 and 2 are more efficient than version 1, why is version 3 easier to understand and more efficient than version 2?
# Though both versions 2 and 3 use the same number of lines, version 3 is easier to understand
# Version 3 checks if the input value is valid or not first. Then checks which category the input value falls under by simply giving ONE if condition for each if or elif, whereas version 2 checks for TWO if conditions.
# For example, if the mark entered is 60... Version three will recognize that the mark >= to 60, whereas version 2 will check if the mark is >=60 AND if the mark is <70.