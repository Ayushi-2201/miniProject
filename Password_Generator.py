import random
import string

def generator(min_length, uppercase_letters, lowercase_letters, digits, specials):

    available_uppercase = string.ascii_uppercase
    available_lowercase = string.ascii_lowercase
    available_digits = string.digits
    available_specials = string.punctuation

    variablesAllowed = ""
    
    if uppercase_letters :
        variablesAllowed += available_uppercase

    if lowercase_letters :
        variablesAllowed += available_lowercase

    if digits :
        variablesAllowed += available_digits

    if specials :
        variablesAllowed += available_specials
    
    meets_criteria = False
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    password = ""

    while not meets_criteria or len(password) < min_length:
        char = random.choice(variablesAllowed)
        password += char
        
        if char in available_uppercase:
            has_uppercase = True

        elif char in available_lowercase:
            has_lowercase = True

        elif char in available_digits:
            has_digit = True

        elif char in available_specials:
            has_special = True


        meets_criteria = True

        if uppercase_letters:
            meets_criteria = has_uppercase
            
        if lowercase_letters:
            meets_criteria = meets_criteria and has_lowercase
            
        if digits:
            meets_criteria = meets_criteria and has_digit
           
        if specials:
            meets_criteria = meets_criteria and has_special
            


    return password


def main():
    while True :
        length_of_pwd = input("Enter the length for the password : ")
        if length_of_pwd.isdigit():
            length_of_pwd = int(length_of_pwd)
            uppercase_letters = input("Are uppercase letters allowed to occur in the generated password (y/n):").lower() == "y"
            lowercase_letters = input("Are lowercase letters allowed to occur in the generated password (y/n):").lower() == "y"
            digits = input("Are digits allowed to occur in the generated password (y/n):").lower() == "y"
            specials = input("Are special characters allowed to occur in the generated password (y/n):").lower() == "y"
            if not (uppercase_letters or lowercase_letters or digits or specials):
                print("Atleast one of the above variables (letters (uppercase or lowercase), digits, special characters) must be present to generate a password.")
                continue
            pwd = generator(length_of_pwd, uppercase_letters, lowercase_letters, digits, specials)
            print(f"The generated password is {pwd}")
            another = input("Want another password (y/n): ").lower() == "y"
            if not another:
                break
                
        else:
            print("Enter a number.")

main()



































def more_information(min_length, variablesAllowed, uppercase_letters = True, lowercase_letters = True, digits = True, specials = True, ):
    count = 0
    if not (uppercase_letters or lowercase_letters or digits or specials):
                print("Atleast one of the required variables (letters (uppercase or lowercase), digits, special characters) must be allowed to generate a password.")
    else :
        more_info = input("Do you want to specify the number of letters (uppercase or lowercase), digits, special characters in the password (y/n): ").lower() == "y"
        info_list = []
        if more_info:
            while True:
                no_of_uppercase_letters = input("How many uppercase letters are allowed to occur in the generated password :")
                count += no_of_uppercase_letters
                if no_of_uppercase_letters.isdigit():
                    no_of_uppercase_letters = int(no_of_uppercase_letters)
                    info_list.append(no_of_uppercase_letters)
                    if count > min_length:
                        print("The number of uppercase characters specified is more than the required length for the password.")
                    elif count == min_length:
                        print("Your specified character length is equal to the password. Do you want to continue? ")
                    
                else:
                    print("Enter a number.")
            while True:
                no_of_lowercase_letters = input("How many lowercase letters are allowed to occur in the generated password :")
                if no_of_lowercase_letters.isdigit():
                    no_of_lowercase_letters = int(no_of_lowercase_letters)
                    info_list.append(no_of_lowercase_letters)
                    break
                else:
                    print("Enter a number.")
            while True:
                no_of_digits = input("How many digits are  allowed to occur in the generated password :")
                if no_of_digits.isdigit():
                    no_of_digits = int(no_of_digits)
                    info_list.append(no_of_digits)
                    break
                else:
                    print("Enter a number.")
            while True:
                no_of_specials = input("How many special characters are  allowed to occur in the generated password : " )
                if no_of_specials.isdigit():
                    no_of_specials = int(no_of_specials)
                    info_list.append(no_of_specials)
                    break
                else:
                    print("Enter a number.")
    return info_list