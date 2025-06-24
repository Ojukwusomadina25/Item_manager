import string

def check_password_strength(password):
    has_upper = any(char.isupper() for  char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    long_enough = len(password) >= 8
    
    strength = sum([has_upper, has_lower, has_digit, has_symbol, long_enough])
    
    if strength == 5:
        print("✅ Strong password!")
    elif 3 <= strength <5:
        print("⚠️ Medium password, could be stronger")
    else:
        print("❌ Weak password")
    if strength <5:
        if not has_upper:
            print("Tip: Add an upper case letters")
        if not has_digit:
            print("Tip: Add some numbers")
        if not has_lower:
            print("Tip: Add lower case letters")
        if not has_symbol:
            print("Tip: use symbols like !@*/.")
        if not long_enough:
            print("Tip: make it at least 8 characters or longer")

while True:
    user_input = input("Enter a password to check (or type exit to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    if not user_input.strip():
        print("⚠ Please type something — password cannot be empty")
        continue
    check_password_strength(user_input)