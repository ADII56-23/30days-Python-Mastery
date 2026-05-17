#String pattern validation
user_input ="12345"
valid = True
for ch in user_input:
    if not ch.isdigit():
        valid =False
        break
if valid:
    print("Valid")
else:
    print("Invalid (Contains non-digit characters)")