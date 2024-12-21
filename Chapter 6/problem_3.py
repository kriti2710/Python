p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscibe this"
p4 = "click this"

message = input("Enter your comment")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("this message is spam")

else:
    print("valid message")