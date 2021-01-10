from pyfiglet import Figlet

iden = ["!", "&", "@", "%", "{", "]", "?", "*", "#", "£", "^", "|"]
alp = {10: "a", 20: "b", 30: "c", 40: "d", 50: "e", 60: "f", 70: "g", 80: "h", 90: "i", 11: "j", 12: "k", 13: "l", 14: "m", 15: "n", 16: "o", 17: "p", 18: "q", 19: "r", 21: "s", 22: "t", 23: "u", 24: "v", 25: "w", 26: "x", 27: "y", 28: "z"}

def main():
    f = Figlet()
    print(f.renderText("Decryptinator"))
    user_Input = input("Input string> ")
    filtered = find_identifier(user_Input)
    translated = translator(filtered)
    final = reverser(translated)
    print("Output> " + final)


def find_identifier(input):
    temp = []
    x = 0
    while x < len(input):
        if input[x] in iden:
            temp.append(input[x+1:x+3])
        x += 1
    return temp


def translator(input):
    temp = []
    x = 0
    while x < len(input):
        z = input[x]
        if int(z) in alp:
            temp.append(alp[int(z)])
        x += 1
    return "".join(temp)


def reverser(input):
    return input[::-1]


if __name__ == "__main__":
    main()