def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1/num2

def length_of_string(str):
    return len(str)

def join_string(str1, str2):
    return f"{str1}{str2}"

def add_string_as_number(str1, str2):
    return int(str1) + int(str2)

def number_to_full_month_name(num):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September"
    }
    return months[num]

def number_to_short_month_name(num):
    months = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "Jun",
        7: "Jul",
        8: "Aug",
        9: "Sep",
        10: "Oct"
    }
    return months[num]


def volume_of_cube(len, h, w):
    return len*w*h

def reverse_str(str):
    empty_list = []
    empty_str = ""
    for char in str:
        empty_list.append(char)
    empty_list.reverse()
    empty_str.join(empty_list)
    return empty_str
