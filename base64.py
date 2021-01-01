import base64

a = input("Your message: ")

a1 = a.encode("UTF-8")
a2 = base64.b64encode(a1)
a3 = a2.decode("UTF-8")

print(a3)
