#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Dec 2022
# This program converts grades


def calculate_grade(grade: str) -> int:
    # calculate area

    # process
    match grade:
        case "4+":
            percent = 97
            return percent
        case "4":
            percent = 87
            return percent
        case "4-":
            percent = 80
            return percent
        case "3+":
            percent = 78
            return percent
        case "3":
            percent = 75
            return percent
        case "3-":
            percent = 70
            return percent
        case "2+":
            percent = 68
            return percent
        case "2":
            percent = 65
            return percent
        case "2-":
            percent = 61
            return percent
        case "1+":
            percent = 58
            return percent
        case "1":
            percent = 54
            return percent
        case "1-":
            percent = 51
            return percent
        case "R":
            percent = 30
            return percent
        case "NE":
            percent = 0
            return percent
        case _:
            percent = -1
            return percent


def main():
    # input
    print("This program converts grade level to percentage.")
    grade = input("Enter grade as a level: ")

    # call functions
    grades_as_percent = calculate_grade(grade)
    if grades_as_percent == -1:
        print("Invalid Input")
    else:
        print("Level {0} equals {1}%.".format(grade, grades_as_percent))

    print("\nDone.")


if __name__ == "__main__":
    main()
