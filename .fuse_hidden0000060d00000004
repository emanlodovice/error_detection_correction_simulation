# simulates error detection and correction using hamming code
from random import randint


class HammingCode(object):

    def __init__(self, bits=[]):
        self.bits = bits
        self.received = []

    def generate_bits(self):
        self.bits = [randint(0, 1) for x in range(4)]
        return self.bits

    def add_parity_bits(self):
        r0 = (self.bits[3] + self.bits[2] + self.bits[1]) % 2
        r1 = (self.bits[2] + self.bits[1] + self.bits[0]) % 2
        r2 = (self.bits[3] + self.bits[2] + self.bits[0]) % 2
        self.bits += [r2, r1, r0]
        return self.bits

    def induce_error(self):
        self.received = []
        index = randint(0, len(self.bits)-1)
        for i, v in enumerate(self.bits):
            if index == i:
                if v == 0:
                    self.received.append(1)
                else:
                    self.received.append(0)
            else:
                self.received.append(v)
        return self.received

    def correct_error(self):
        s0 = (self.received[1] + self.received[2] + self.received[3] +
              self.received[6]) % 2
        s1 = (self.received[0] + self.received[1] + self.received[2] +
              self.received[5]) % 2
        s2 = (self.received[0] + self.received[2] + self.received[3] +
              self.received[4]) % 2
        coding = {
            '000': -1,
            '001': 6,
            '010': 5,
            '011': 1,
            '100': 4,
            '101': 3,
            '110': 0,
            '111': 2
        }
        syndrome = '{0}{1}{2}'.format(s2, s1, s0)
        print 'syndrome = ' + syndrome
        index = coding[syndrome]
        if index == -1:
            print "No error"
        else:
            if self.received[index] == 0:
                self.received[index] = 1
            else:
                self.received[index] = 0
            print 'Data code after correction: %r' % self.received[0:4]


# h = HammingCode()
# print "original: %r" % h.generate_bits()
# print "with parity: %r" % h.add_parity_bits()
# print "received with errors: %r" % h.induce_error()
# h.correct_error()
