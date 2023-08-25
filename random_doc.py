'''
__or__ -> or method
__and__ -> and method
left_shift ->
right_shift ->
arithmatic_right_shift ->
'''

class BinaryNumber(list):
    ''''''

    def __or__ (self, other: 'BinaryNumber'):
        assert len(self) == len(other), "Length of two binary numbers must be equal"
        new_bn =[]
        for index in range(len(self)):
            if self[index] or other[index] == 1:
                new_bn.append(1)
            else:
                new_bn.append(0)
        return BinaryNumber(new_bn)

    def __and__ (self, other: 'BinaryNumber'):
        assert len(self) == len(other), "Length of two binary numbers must be equal"
        new_bn = []
        for index in range(len(self)):
            if self[index] and other[index] == 1:
                new_bn.append(1)
            else:
                new_bn.append(0)
        return BinaryNumber(new_bn)

    def __add__(self, other: 'BinaryNumber'):
        carry = None
        new_bn = []
        index = -1
        assert len(self) == len(other), "Length of two binary numbers must be equal"
        while abs(index) < len(self):
            if self[index] and other[index]: # both 1
                carry = 1
                new_bn.insert(0,0)
            elif self[index] or other[index]: # if one is 1
                if carry > 0:
                    new_bn.insert(0,0)
                else:
                    new_bn.insert(0,1)
            elif not self[index] and not other[index]: # both 0
                if carry > 0:
                    new_bn.insert(0,1)
                    carry = 0
                else:
                    new_bn.insert(0,0)
            index -= 1
        return BinaryNumber(new_bn)



