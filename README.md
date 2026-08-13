# User Authentication System

A Python-based user authentication and validation system that validates user information before login.

## Features

* Phone number validation
* 6-digit OTP validation
* CAPTCHA validation
* Email validation
* Password strength checking
* Password requirements:

  * Minimum 8 characters
  * At least one digit
  * At least one uppercase letter
  * At least one lowercase letter
  * At least one special character

## Technologies Used

* Python
* Regular Expressions (`re`)

## How to Run

1. Clone the repository.
2. Open the project folder.
3. Run the Python file:

```bash
python authentication.py
```

4. Enter the requested information when prompted.

## Example

```text
enter your name: Hari
enter your phone number: 9876543210
phone number is valid

enter one time password: 123456
your OTP is valid

Enter your email to login: example@gmail.com
entered email is valid

enter your password: Hari@12345
strong : your password is secured.
```

## Project Purpose

This project was created to practice Python functions, conditional statements, string validation, exception handling, and regular expressions.
