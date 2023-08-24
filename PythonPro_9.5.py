
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler("file_log.log", mode="w")
formatter = logging.Formatter("%(name)s - %(asctime)s - %(levelname)s %(message)s")

handler.setFormatter(formatter)
logger.addHandler(handler)


def dec(func):
    def wrapper(a):
        if not isinstance(a, int | float):
            logger.error(f"Wrong type of a variable: {a}")
            raise TypeError("Wrong Type of a variable")
        if a <= 0:
            logger.error(f"Wrong Value of a variable: {a}")
            raise ValueError("Wrong Value of a variable")
        logger.info(f"Variable is {a}")

        logger.info(f"Result is {func(a)}")
        return print(func(a))

    return wrapper


@dec
def fact(num):

    res = 1
    while num > 0:
        res *= num
        num -= 1
    return res


fact(2)
