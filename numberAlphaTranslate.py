numberIN = input("Phone number in XXX-XXX-XXXX: ")
numberOut = [0]*12
i = 0

for ch in numberIN:
    if ch == "-":
        numberOut[i] = ch
    elif ch.isdigit():
        numberOut[i] = ch
    elif ch.lower() == "a" or ch.lower() == "b" or ch.lower() == "c":
        numberOut[i] = 2
    elif ch.lower() == "d" or ch.lower() == "e" or ch.lower() == "f":
        numberOut[i] = 3
    elif ch.lower() == "g" or ch.lower() == "h" or ch.lower() == "i":
        numberOut[i] = 4
    elif ch.lower() == "j" or ch.lower() == "k" or ch.lower() == "l":
        numberOut[i] = 5
    elif ch.lower() == "m" or ch.lower() == "n" or ch.lower() == "o":
        numberOut[i] = 6
    elif ch.lower() == "p" or ch.lower() == "q" or ch.lower() == "r" or ch.lower() == "s":
        numberOut[i] = 7
    elif ch.lower() == "t" or ch.lower() == "u" or ch.lower() == "v":
        numberOut[i] = 8
    elif ch.lower() == "w" or ch.lower() == "x" or ch.lower() == "y" or ch.lower() == "z":
        numberOut[i] = 9
    i = i + 1

print("The phone number is:", end=" ")
for num in numberOut:
    print(num, end="")
