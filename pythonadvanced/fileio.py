with open(r"log01.log", "r") as fp:
    for line in fp:
        print(line)
    for x in dir(fp):
        print(x)