def obtain_variables():
    while True:
        message = input("Please input your message: ")
        if message.strip() == "":
            print("Invalid input. Please enter a message that is not blank or contains only spaces.")
        else:
            break
    while True:
        try:
            shift = int(input("Please input your shift number: "))
            if shift >0:  # Check if the shift number is larger than 0 
                break
            else:
                print("Invalid input. Please enter a number between 1 and 25.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
obtain_variables()

def print_stuff():
    print("Input Text: " + message)
    print("Shift Number: " + str(shift))
    print("Output Text: " + encrypted_text)
print_stuff()