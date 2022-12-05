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
        case "4":
            percent = 87
        case "4-":
            percent = 80
        case "3+":
            percent = 78
        case "3":
            percent = 75
        case "3-":
            percent = 70
        case "2+":
            percent = 68
        case "2":
            percent = 65
        case "2-":
            percent = 61
        case "1+":
            percent = 58
        case "1":
            percent = 54
        case "1-":
            percent = 51
        case "R":
            percent = 30
        case "NE":
            percent = 0
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
