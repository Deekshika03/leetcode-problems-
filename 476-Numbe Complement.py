"""Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation."""

#solution 

class Solution:
    def findComplement(self, num: int) -> int:
        
        # Num ko binary string mein convert kr rhe h
        # [2:] se starting ka '0b' hata rhe h
        binary = bin(num)[2:]

        # Complemented binary ko store krne ke liye empty string
        complement = ""

        # Binary ke har bit ko check karenge
        for bit in binary:

            # Agar bit 0 hai, toh uska complement 1 hoga
            if bit == '0':
                complement += '1'

            # Agar bit 1 hai, toh uska complement 0 hoga
            else:
                complement += '0'

        # Complement binary string ko decimal int m convert kr rhe h
        return int(complement, 2)
