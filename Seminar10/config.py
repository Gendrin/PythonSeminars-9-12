def Token():
    with open("token.txt", "r") as file:
        return  file.readline()