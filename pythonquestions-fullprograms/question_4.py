word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

word1 = word1.lower()
word2 = word2.lower()

if word1 > word2:
    print(f"The second word, {word2}, is alphabetically first")
else:
    print(f"The first word, {word1}, is alphabetically first")

# Upper case letters are actually smaller than lower case letters, meaning they have a higher priority than lower case letters.  
# The code will recognize ANY uppercase letter as smaller than ANY lowercase number. 
# So for example, uppercase letter 'X' is still smaller than lowercase letter "a" and is thus still alphabetically first according to python.
# By turning all letters into lowercase letters, all letters can now actually be evaluated by their order in the alphabet.
# The code will now be able to recognize which word is alphabetically first, without uppercase letters interfering
