import re

def normalize_urdu_text(text):
    # Phone numbers ko digit-by-digit spell out karo
    urdu_digits = {
        '0': 'صفر', '1': 'ایک', '2': 'دو', '3': 'تین', '4': 'چار',
        '5': 'پانچ', '6': 'چھ', '7': 'سات', '8': 'آٹھ', '9': 'نو'
    }

    def spell_out_number(match):
        digits = match.group()
        return ' '.join(urdu_digits[d] for d in digits if d in urdu_digits)

    # Long digit sequences (jaise phone numbers, IDs — 5+ digits) ko digit-by-digit karo
    text = re.sub(r'\b\d{5,}\b', spell_out_number, text)

    return text

# Test
if __name__ == "__main__":
    test = "میرا فون نمبر 0300 1234567 ہے اور آج 2026 کا سال ہے۔"
    print(normalize_urdu_text(test))


# import re

# # Urdu digit mapping
# urdu_digits = {
#     '0': 'صفر', '1': 'ایک', '2': 'دو', '3': 'تین', '4': 'چار',
#     '5': 'پانچ', '6': 'چھ', '7': 'سات', '8': 'آٹھ', '9': 'نو'
# }

# def spell_out_digits(digit_string):
#     """Har digit ko alag alag Urdu lafz mein convert karta hai"""
#     return ' '.join(urdu_digits[d] for d in digit_string if d in urdu_digits)


# def normalize_urdu_text(text, digit_threshold=5):
#     """
#     Long digit sequences (phone numbers, CNIC, IDs) ko digit-by-digit
#     bolta hai. Chhote numbers (saal, quantity) ko poora number rehne
#     deta hai.

#     digit_threshold: kitne digits se zyada ho to digit-by-digit bola jaye
#                       (default 5 — is se 4-digit saal jaisay 2026 affect
#                       nahi hote, lekin phone/CNIC jaisay lambay number
#                       pakre jate hain)
#     """

#     # Step 1: CNIC format handle karo (13245-1234567-1 jaisa, dashes ke sath)
#     def handle_cnic(match):
#         cnic = match.group()
#         digits_only = re.sub(r'\D', '', cnic)  # sirf digits nikalo
#         return spell_out_digits(digits_only)

#     text = re.sub(r'\b\d{5}-\d{7}-\d\b', handle_cnic, text)

#     # Step 2: Phone numbers handle karo (spaces/dashes ke sath ya bina)
#     # jaise: 0300 1234567, 0300-1234567, 03001234567
#     def handle_phone(match):
#         phone = match.group()
#         digits_only = re.sub(r'\D', '', phone)
#         if len(digits_only) >= digit_threshold:
#             return spell_out_digits(digits_only)
#         return phone  # agar chhota hai to na chherna

#     # Pattern: digits with optional spaces/dashes in between, total 7+ digits
#     text = re.sub(r'\b[\d][\d\s\-]{5,}\d\b', handle_phone, text)

#     # Step 3: Baaki reh gaye standalone long digit sequences (bina space/dash)
#     def handle_plain_number(match):
#         digits = match.group()
#         if len(digits) >= digit_threshold:
#             return spell_out_digits(digits)
#         return digits  # chhota number (jaise saal) chhod do

#     text = re.sub(r'\b\d+\b', handle_plain_number, text)

#     return text


# # ---- Test cases ----
# if __name__ == "__main__":
#     test_cases = [
#         "میرا فون نمبر 0300 1234567 ہے۔",
#         "میرا فون نمبر 03001234567 ہے۔",
#         "میرا فون نمبر 0300-1234567 ہے۔",
#         "میرا CNIC نمبر 42101-1234567-1 ہے۔",
#         "آج 2026 کا سال ہے۔",
#         "میری عمر 25 سال ہے۔",
#         "کل 100 لوگ آئے تھے۔",
#     ]

#     for t in test_cases:
#         print(f"Original : {t}")
#         print(f"Normalized: {normalize_urdu_text(t)}")
#         print()