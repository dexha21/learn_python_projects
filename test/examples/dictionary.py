customer = {
  "name": "John Smith",
  "age": 30,
  "is_verified": True,
}

print(customer["name"])

print(customer.get("name"))
# print(customer.get("birthdate", "Jan 1 1980")) #with get method if a key doesn't exist you can add a default value in the second parameter

customer["birthdate"] = "Jan 1 1980"

print(customer["birthdate"])