from random import randint
from hamming_code import HammingCode


class BurstErrorCorrection(object):

    def generate_bits(self):
        # we can have 3 code words with size 4
        # we can correct burst error of size 3
        self.bits = [randint(0, 1) for x in range(12)]
        print "Data word: \n %r" % self.bits
        return self.bits

    def initialize_hamming_code(self):
        self.hamming = []
        length = len(self.bits)
        hamming_count = length / 4
        print "Code words using hamming code:"
        for i in range(0, hamming_count):
            hamming = HammingCode(bits=self.bits[i * 4: (i + 1) * 4])
            hamming.add_parity_bits()
            print hamming.bits
            self.hamming.append(hamming)

    def simulate_send(self):
        self.sent = []
        code_word_length = len(self.hamming[0].bits)
        for i in range(0, code_word_length):
            for h in self.hamming:
                self.sent.append(h.bits[i])
        print "Sent code words: \n %r" % self.sent
        return self.sent

    def induce_burst_error(self):
        start_index = randint(0, len(self.sent) - 3)
        print "Start index of burst error: %d" % start_index
        i = start_index
        self.received = []
        for j in self.sent:
            self.received.append(j)
        while(i < start_index + 3):
            self.received[i] = randint(0, 1)
            i += 1
        print "Received data with error: \n %r" % self.received
        return self.received

    def correct_error(self):
        code_word_length = len(self.hamming[0].bits)
        for i in range(0, code_word_length):
            for h in self.hamming:
                self.sent.append(h.bits[i])


b = BurstErrorCorrection()
b.generate_bits()
b.initialize_hamming_code()
b.simulate_send()
b.induce_burst_error()
