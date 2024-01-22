import random

# Generate a random number between 1 and 100.
random_num = random.randint(1,100)  

# Initialize a variable to keep track of the number of game tries.
game_cnt = 1  

while True:
    try:
        # Prompt the user to enter a number. 
        my_number = int(input("Enter a number between 1 and 100: "))  

        # If the entered number is greater than the random number, print "Down".
        if my_number > random_num:
            print("Down")
        
        # If the entered number is less than the random number, print "Up".
        elif my_number < random_num:
            print("Up")  

        # If the entered number matches the random number, print a congratulations message with the number of tries taken.
        elif my_number == random_num:
            print(f"Congratulations.  You got it right in {game_cnt} tries.")  
            # Exit the loop.
            break  

        # Increment the game tries count.    
        game_cnt += 1  

    # Handle exceptions, such as non-integer input, and print an error message.
    except Exception as e:
        print("Error : ", e)  
