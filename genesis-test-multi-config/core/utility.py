import string
import random


def random_str(length, charset=None):
    if charset is None:
        charset = string.ascii_lowercase + string.digits
    return ''.join(random.choice(charset) for _ in range(length))


def random_mail():
    return 'silkcloudtest+' + random_str(20) + '@gmail.com'


def random_phone():
    return '+86186' + random_number(10) + '8497'


def random_number(length, charset=None):
    if charset is None:
        charset = string.digits
    return ''.join(random.choice(charset) for _ in range(length))


def random_pwd():
    return random_str(4, string.ascii_uppercase) + random_str(4, string.ascii_lowercase) + random_str(4, string.digits)


def create_phone(length, charset=None):
    if charset is None:
        pre_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                   "153", "155", "156", "157", "158", "159", "186", "187", "188"]
        random_pre = random.choice(pre_list)
        number = "".join(random.choice("0123456789") for i in range(length))
        phone_num = random_pre + number
    return phone_num
