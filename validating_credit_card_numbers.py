import re

def validate_credit_card(card):
    pattern = r'^[456]\d{3}(-?\d{4}){3}$'
    if re.match(pattern, card):
        card_no_hyphen = card.replace('-', '')
        if not re.search(r'(\d)\1{3,}', card_no_hyphen):
            return "Valid"
    return "Invalid"

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        card = input()
        print(validate_credit_card(card))
