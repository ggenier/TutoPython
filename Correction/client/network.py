
def getMessage(str):
    # if type(str) is not str:
        # return (-1, 0)
    if len(str) == 0:
        return (-1, 0)

    if str[0] != "!":
        return (0, str)

    if str[1] == ">":
        return (1, int(str[2]))

    if str[1] == "<":
        return (2, int(str[2]))

    if str[1] == ".":
        return (3, str[2:])

    if str[1] == "!":
        return (4, 0)

    return -1
