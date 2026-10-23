"""
Name: Jadin Wilson
Peers: (add any collaborators)
References: stack overflow
"""

def get_letter():
    """ This function gets input checks if it is correct and returns """
    # remove the default return and add your code
    # Plan in commits

    
    #Loop while true
    while True:
        # (1) Ask user for input
        user_input = input("Give an single uppercase letter: ")
        # (2) If the inputed string is longer then a single character prompt again
        length = len(user_input)
        if length>1:
            print ("Error: it needs to be a single character.")
            continue
        #(3) If the inputed string is not A,B, or C print error message
        elif user_input not in ["A","B","C"]:
            print("Error: You provided the wrong character.")
            continue
        else:
        #(4) return correctly inputed value
            return user_input
            break

def get_digit():
    """ This function asks the user for input checks if the input is a digit and is 1,2, or 3 """
    # Plan
    #(1) Loop
    while True:
        #(2) get input from user
        number = input("Give an single number character: ")
        #(3) if the number is not a digit print error and continue otherwise go to next check
        if number.isdigit():
            digit = int(number)
            #(4) if 1,2, or 3 is in range then return else print error
            if digit in range (1,4):
                return digit
                break
            else:
                print("Error: a single digit needs to be in [1,3].")
                continue
        else:
            print("Error: your input should be only digits.")
            continue

def check_pattern(letter, digit, st_list):
    """ This function checks if letters and digits are in word and prints """
    matching_words = []
    #Plan
    #(1) turn int's into strings
    letters = str(letter)
    digits = str(digit)
    # (2)Loop through word in list
    for word in st_list:
    # (3) if pattern in word print word
        letter_index = word.find(letters)
    #(4) If letter in word does not equal -1:
        if letter_index != -1:
    #(5) If digits in word is letter in word + 1 append matching words
            if digits in word[letter_index + 1:]:
                matching_words.append(word)
                
    #(6)Always print "Strings with the pattern: "
    print("Strings with the pattern: ")
    #(5) Print the results separated by spaces if any match found
    if matching_words:
        
        print(" ".join(matching_words))

#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    while True:
    # Call get letter
        letter = get_letter()
    # assign get_digit to digit and call
        digit = get_digit()
    # Call check_pattern and pass letter, digit, and st_list 
        check_pattern(letter, digit, st_list)
    # Prompt to try again 
        again = input("Try Again? (y/n): ")
    # If again == y continue else break
        if again == "y":
            continue
        else:
            break
    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()



 






