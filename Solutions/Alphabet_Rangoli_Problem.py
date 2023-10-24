# Will print out the Alphabet Rangoli, a diamond-shaped pattern with letters, "a" being in the middle
def PrintAlphabetRangoli(n):
    finalString = "" # The final string we'll print out
    maxNum = (2*n) - 1 # the number of rows and columns we need to print out (we'll reuse this number a lot!)
    for i in range(0, maxNum):
        for j in range(0, maxNum):
            newNum = (2*n - 2) # The initial value of the number (we'll subtract from this one)
            if (i < n): newNum -= i # If you're not past the middle
            else: newNum -= (maxNum - 1 - i) # If you've past the middle
            if (j < n): newNum -= j # If you're not past the middle
            else: newNum -= (maxNum - 1 - j)  # If you've past the middle
            newChar = "" # The new character to add to the final string
            if newNum > n-1: newChar = "-" # If the number is too big (somewhere in the corner) => "-"
            else: newChar = chr(newNum + 97) # If it's somewhere in the middle => corresponding letter
            if j != 0: finalString += f"-{newChar}" # Add "-" and new character to the final string, if you're not at the first row
            else: finalString += newChar # If you're at the first row, don't add a "-"
        finalString += "\n" # After each row, jump lines
    print(finalString) # Print the fomatted string

# Test cases:
PrintAlphabetRangoli(1)
PrintAlphabetRangoli(2)
PrintAlphabetRangoli(3)
PrintAlphabetRangoli(4)
PrintAlphabetRangoli(5)
PrintAlphabetRangoli(15)
PrintAlphabetRangoli(19)
PrintAlphabetRangoli(26)