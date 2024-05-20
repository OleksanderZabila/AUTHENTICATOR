import pyotp
import qrcode

key = "ZABILA"

uri = pyotp.totp.TOTP(key).provisioning_uri(name="Zabila_Key", issuer_name="Server:")
print(uri)

qr = qrcode.make(uri)
qr.save("totp.png")
