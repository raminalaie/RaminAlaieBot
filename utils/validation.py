# utils/validation.py

def validate_national_code(national_code: str) -> bool:
    if len(national_code) != 10 or not national_code.isdigit():
        return False

    check = int(national_code[9])
    s = sum(int(national_code[x]) * (10 - x) for x in range(9)) % 11

    return (s < 2 and check == s) or (s >= 2 and check + s == 11)
