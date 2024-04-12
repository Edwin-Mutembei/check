"""
Question 1 - Reverse Integer
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123 Output: 321 Example 2:

Input: x = -123 Output: -321 Example 3:

Input: x = 120 Output: 21

Constraints:

-2^31 <= x <= 2^31 - 1

Solution phase
There are several types of integers: signed, unsigned, 32 bit, 64 bit
[-2147483647, +2147483647] range
Reverse the integer - the last digit becomes the first check if it is within range

Step 1: Convert the number into a string

Step 2: Sort by index - reverse


"""

def reverse_number(number):
    number = str(number)

    max = len(number) - 1
    new_number = ''
    for i in range(len(number)):
        new_number += number[max - i]

    if new_number[-1] == '-':
        new_number = new_number[:len(new_number) - 1]
        new_number = '-' + new_number

    new_number = int(new_number)

    if -2147483647 < new_number < 2147483647:
        return new_number
    else:
        return 0
    
    def main():
        number = input('Enter a number:  ')
        print(reverse_number(number))

    if __name__ == '__main__':
        main()

