def generate_password():
    import random
    
    charaters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    charatersList = [character for character in charaters]
    
    characterCount = int(input("Enter the Number of Characters in Your Passwords: "))
    
    passwordList = []
    for i in range(characterCount):
        passwordList.append(random.choice(charatersList))
    
    password = "".join(passwordList)
    print(password)