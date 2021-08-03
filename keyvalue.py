phone = {"kim":"1111","lee":"2222","park":"3333"}
print(phone.keys())
print(phone.values())

for k in phone.keys():
    print(k)

print("park" in phone)
print("moon" in phone)
print("moon" not in phone)