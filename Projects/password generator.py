import random
import string
def generate_pswd(min_length,number=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation
    characters=letters
    if number:
        characters+=digits
    if special_characters:
        characters+=special
    psd=""
    meets_criteria=False
    has_number=False
    has_special=False
    while not meets_criteria or len(psd)<min_length:
        new_char=random.choice(characters)
        psd+=new_char
        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
        meets_criteria=True
        if number:
            meets_criteria=has_number
        if special_characters:
            meets_criteria=meets_criteria and has_special
    return psd
min_length=int(input("enter minimum length:"))
has_number=input("In password you want number (yes/no)").lower()=="yes"
has_special=input("In password you want special character (yes/no)").lower()=="yes"
pswd=generate_pswd(min_length,has_number,has_special)
print("password is",pswd)
                      
