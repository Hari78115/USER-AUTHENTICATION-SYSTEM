#password strength checker

#length>8 chr,digit,uppercase,lower case,special char

import re
user_name=input("enter your name :")
number=input('enter your phone number :')
def number_check(number):
    if number.isdigit() and len(number)==10:
        return "phone number is valid"
    else :
        raise ValueError("your phone number is invalid , Please enter valid number")
print(number_check(number))


# Checking OTP 

otp=input('enter one time password :')

def otp_check(otp):
    if otp.isdigit() and len(otp)==6:
        return " your otp is valid"
    else :
        raise ValueError("your otp is invalid,Please enter valid otp")
print(otp_check(otp))


# Checking Captcha


enter_captcha=input("enter your captcha : ")
def check_captcha(enter_captcha):
    if len(enter_captcha)<=6:
        raise ValueError("your enterd captcha is invalid captcah ,please enter valid captcha")
    if not any (char.isdigit() for char in enter_captcha):
        raise ValueError("you enterd captcha is invalid captcha,Captcha must contain atlaeast one digit")
    if not any(char.isupper() for char in enter_captcha):
        raise ValueError("your entered captcha is  invalid captcha,captcha must contain atleast one upper case letter ")
    if not any(char.islower() for char in enter_captcha):
        raise ValueError("your entered captcha is invalid,captcha must contain atleast one lower letter")
    return "your captcha is valid"


# Entering Email and Checking Email Vaild or invalid


email=input("Enter your email to login :")
def email_check(email):
    if '@' in email and '.' in email :
        return "entered email is valid "
    else:
        raise ValueError("your email is invalid")
print(email_check(email))


# Checking Password Strength

password=input('enter your password :')

def password_strength_check(password):
    
    if len(password) < 8:
        return "weak : password must contain atleat 8 charecters"
    if not any(char.isdigit() for char in password):
        return "weak: password must contain atleat one number"
    
    if not any(char.isupper() for char in password):
        return "weak: password must contain atleast one uppercase alphabet"
    
        
    if not any(char.islower() for char in password):
        return "weak: password must contain atleast one lowercase alphabet"
    
    if not re.search(r'[!@#$%^&*()]',password):
        return "weak: password must contain atleast one special charecter"


    return "strong : your password is secured."

print(password_strength_check(password))
