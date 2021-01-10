from pyfiglet import Figlet
import random
import string

chars = string.ascii_letters
iden = ["!", "&", "@", "%", "{", "]", "?", "*"]
alp = {"a": 10, "b": 20, "c": 30, "d": 40, "e": 50, "f": 60, "g": 70, "h": 80, "i": 90, "j": 11, "k": 12, "l": 13, "m": 14, "n": 15, "o": 16, "p": 17, "q": 18, "r": 19, "s": 21, "t": 22, "u": 23, "v": 24, "w": 25, "x": 26, "y": 27, "z": 28}
values = []
hashes = []
enc = []

def main():
    f = Figlet()
    print(f.renderText("Encryptinator"))

    user_Input = input("Input string> ")
    string = reverser(user_Input)
    checker(string)
    hasher(values)
    print("Output> " + combiner(values, hashes))


def reverser(input):
    return input[::-1]


def checker(input):
    for x in input:
        y = random.choice(iden)
        if x in alp:
            values.append(y + str(alp[x]))
    

def hasher(input):
    for x in input:
        randomness = ""
        random_int = random.randint(5, 10)
        for c in range(random_int):
            randomness += random.choice(chars)

        hashes.append(randomness)


def combiner(x, y):
    list = []
    i = 0
    while i < len(x):
        list.append(x[i])
        list.append(y[i]) 
        i += 1
    return "".join(list)

if __name__ == "__main__":
    main()