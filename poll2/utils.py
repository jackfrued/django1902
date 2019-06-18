import random


def generate_mobile_code(length=6):
    """生成手机验证码字符串"""
    select_nums = random.choices('0123456789', k=length)
    return ''.join(select_nums)


def generate_captcha_code(length=4):
    """生成图片验证码字符串"""
    selected_chars = random.choices(
        '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
        k=length
    )
    return ''.join(selected_chars)
