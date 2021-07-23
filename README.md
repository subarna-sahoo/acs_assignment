# ACS assignment

You are given an integer K.

Task

Write code to determine a valid integer having K digits such that the product of digits of the integer is greater than or equal to the sum of digits of the integer and the product of the digits of the integer is minimized. If more than 1 such integer exists, determine the smallest possible integer.

Notes

A valid integer does not contain leading zeros. For example, valid integers having 3 digits are "234", "123". But "012" is not a valid integer.
Suppose a valid integer having K digits is a1a2..ak, then the sum of digits is a1 + a2 +..+ ak and the product of digits is a1 * a2 *..* ak.
Example

Assumption

K = 2
Approach

Consider integer N = 22, you can see that product of digits = 4 is greater than or equal to the sum of digits = 4 and the product of the digits is minimized. It can be proved that this is the smallest integer of 2 digits.
Therefore, the output is 22.


K = 2
Approach

Consider integer N = 123, you can see that product of digits = 6 is greater than or equal to the sum of digits = 6 and the product of the digits is minimized. It can be proved that this is the smallest integer of 3 digits.
Therefore, the output is 123.

Constraints


1 =< K <= 100000


# $ python3 task_solution.py 
