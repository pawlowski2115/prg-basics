import email

try:
    with open('email.txt', 'r', encoding='utf-8') as file:
        content = file.read()

    sender = email.email_sender(content)
    print(sender)

    receiper = email.email_recipient(content)
    print(receiper)
    
except FileNotFoundError:
        print(f"Hey! The file does not exist.")
