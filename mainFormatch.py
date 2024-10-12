import os

while True:
    strInput = input()
    match(strInput):
        case "11":
            print("this is 11")
        case "22":
            print("this is 22")
        case _:
            print("this is others")