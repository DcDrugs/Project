#!/usr/bin/env python3
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def factorial(factor):
    result = 1
    for item in range(1, factor + 1):
        result *= item
    return result


def main():
    num = int(input())
    result = factorial(num)
    logging.info("result = %s", result)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrut:
        logging.error("Good error")
