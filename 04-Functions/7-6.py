def hide(card_number):
    start = card_number[:2]
    end = card_number[-4:]
    middle = "*" * 10
    return start + middle + end

print(hide("1234567890123456"))