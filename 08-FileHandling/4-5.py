
import re

def read_email(name):
    try:
        with open(name, 'r', encoding='utf-8') as file:
            email_content = file.read()
        return email_content
    except FileNotFoundError:
        print(f"Hey! The file {name} does not exist.")
        return None


def email_sender(name):
    content = read_email(name)
    pattern = r'^From:\s+<(.*?)>'
    match = re.search(pattern, content)
    return match

print(email_sender('email.txt'))