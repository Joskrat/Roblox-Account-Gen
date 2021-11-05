import random
import string


def passwordGen():
    extra = '!"$%&/()=?*#-.,'
    chars = string.ascii_letters
    nums = string.digits

    passwordChars = "".join(random.choice(chars) for ch in range(15))

    passwordNums = "".join(random.choice(nums) for ch in range(15))
    passwordExtra = "".join(random.choice(extra) for ch in range(15))

    password = "".join(random.choice(passwordChars) for i in range(random.randint(1, 5))) + "".join(random.choice(passwordExtra) for i in range(random.randint(1, 5))) + "".join(random.choice(
        passwordNums) for i in range(random.randint(1, 5))) + "".join(random.choice(passwordChars) for i in range(random.randint(1, 5))) + "".join(random.choice(passwordExtra) for i in range(random.randint(1, 5)))

    return password
