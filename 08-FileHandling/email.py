import re

def email_sender(email_content):
    pattern = r'^(From: .*)<(.+)>'
    match = re.search(pattern,email_content, re.MULTILINE)
    return match.group(2) if match else None

def email_recipient(email_content):
    pattern = r'^(To: .*)<(.+)>'
    match = re.search(pattern,email_content, re.MULTILINE)
    return match.group(2) if match else None
