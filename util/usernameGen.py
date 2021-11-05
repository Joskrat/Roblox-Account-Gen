import random
import string


def nameGen():
    chars = string.ascii_letters
    nums = string.digits

    names = open("./names.txt")
    names = names.read()

    name = random.choice(names)

    username = name + "".join(random.choice(chars) for i in range(2)) + \
        "".join(random.choice(nums)
                for i in range(4))
    return username
