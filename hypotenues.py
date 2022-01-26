# Created by: Zack Isingoma
# Created on: 19th, Jan 2022.
# Finds the hypotenues of a
# triangle using pythagoreus theorem
import math


def pythagoreus(base, height):
    hypotenues = math.sqrt(base**2 + height**2)
    print("{}cm and {}cm give the hypotenues of {:.2f}cm".
          format(base, height, hypotenues))

    return hypotenues


def main():
    user_base = input("Enter the base of the triangle(cm): ")
    user_height = input("Enter the height of the triangle(cm): ")

    try:
        user_base_int = int(user_base)
        user_height_int = int(user_height)
    except Exception:
        print("Invalid input")

    pythagoreus(user_base_int, user_height_int)


if __name__ == "__main__":
    main()
