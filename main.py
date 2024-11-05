import random
import string

def generator(min_lenght, numbers = True, special_char = True):
    
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation
    
    characters = letters
    
    if numbers:
        characters += digits
    if special_char:
        characters += specials
        
    main_criteria = False
    has_nums = False
    has_special = False
    
    pwd = ""
    while not main_criteria or len(pwd) < min_lenght:
        
        char = random.choice(characters)
        
        pwd += char
        
        if char in digits:
            has_nums = True
        elif char in specials:
            has_special = True
            
        main_criteria = True
        
        if numbers:
            main_criteria = has_nums
        if special_char:
            main_criteria = main_criteria and has_special
            
    return pwd


min_lenght = int(input("\nEnter Minimum lenght of Password: "))
numbers = input("Need Numbers? (y/n) ").lower() == "y"
specials = input("Need Special Characters? (y/n) ").lower() == "y"


pwd = generator(min_lenght, numbers, specials)
      
print(f"\n The generated password is {pwd}\n")  
        