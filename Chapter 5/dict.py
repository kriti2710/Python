marks = {
    "Kriti" : 99,
    "Ritika": 96,
    "Shaurya":94
}
print(marks, type(marks))

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Kriti":97, "Reena":76})
print(marks)
print(marks.get("Kriti2")) # this will return none value
print(marks["Kriti2"]) #this will throw an error 