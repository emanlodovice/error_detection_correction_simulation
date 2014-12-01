# simulates even parity bit
from random import randint


class Parity(object):

    def generate_bits(self, number):
        self.bits = [randint(0, 1) for x in range(number)]
        return self.bits

    def append_even_parity(self):
        self.is_even_parity = True
        # is_even = True
        # for i in self.bits:
        #     if i == 1:
        #         is_even = not is_even
        ones = self._count_ones(self.bits)
        if ones % 2 == 0:
            self.bits.append(0)
        else:
            self.bits.append(1)
        return self.bits

    def append_odd_parity(self):
        self.is_even_parity = False
        self.append_even_parity()
        if self.bits[-1] == 0:
            self.bits[-1] = 1
        else:
            self.bits[-1] = 0
        return self.bits

    def induce_error(self):
        i = 0
        self.received = []
        while i < len(self.bits):
            if randint(0, 4) == 1:
                self.received.append(randint(0, 1))
            else:
                self.received.append(self.bits[i])
            i += 1
        return self.received

    def detect_error(self):
        ones = self._count_ones(self.received)
        if self.is_even_parity:
            return ones % 2 == 0
        else:
            return ones % 2 == 1

    def _count_ones(self, num):
        count = 0
        for i in num:
            if i == 1:
                count += 1
        return count




p = Parity()
print p.generate_bits(10)
print p.append_odd_parity()
print p.induce_error()
print p.detect_error()

