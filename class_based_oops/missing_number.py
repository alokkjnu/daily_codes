"""
Python program to find missing number in list.
input = [1,2,4,5,6]
output = 3
"""

class MissingNumber:

    def __init__(self,inp1,inp2):

        self.inp1 = inp1
        self.inp2 = inp2

    def find_missing(self):

        expected_sum = self.inp2 * (
            self.inp2 + 1
        ) // 2
        actual_sum = sum(self.inp1)

        return abs(expected_sum - actual_sum)


if __name__ == "__main__":
    inp1 = [1,2,4,5,6]
    inp2 = 5

    cls_ob = MissingNumber(inp1,inp2)
    res = cls_ob.find_missing()
    print(res)