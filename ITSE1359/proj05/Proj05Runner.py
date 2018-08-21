def run(str, subStr):

    message = " I certify that this program is my own work \n and is not the work of others. I agree not \n to share my solution with others."
    print(message)

    str_range = 3

    if subStr in str:
        str_modified = str[str.index(subStr) - str_range : str.index(subStr) + len(subStr) +  str_range]
        return "Petra Unglaub-Maycock \n" + "\n" + str + "\n" + subStr + "\n" + str_modified
    else:
        return "ERROR: subStr not found in str!"