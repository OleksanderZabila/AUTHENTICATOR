import pyotp

key = "ZABILA"

totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input("Enter key: ")))