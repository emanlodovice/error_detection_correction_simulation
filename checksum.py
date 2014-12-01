class Checksum(object):

    def to_binary(self, x):
        b = ''
        while x:
            b = str(x%2) + b
            x /= 2
        return b

    def to_int_array(self, arr):
        y = []
        for x in arr:
            y.append(int(x,2))
        return y

    def checksum(self, data, n_bit):
        x = sum(data)
        b = self.to_binary(x)
        while len(b) > n_bit:
            l = len(b)
            b = self.to_binary(int(b[0:l-4],2) + int(b[l-4:],2))
        return pow(2, n_bit) - 1 - int(b, 2)

    def to_send(self, n_bit, data):
        int_arr = self.to_int_array(data)
        print 'Data to send:', data + [self.to_binary(
            self.checksum(int_arr, n_bit))]

    def validate_receive(self, n_bit, data):
        data = self.to_int_array(data)
        if self.checksum(data, n_bit) == 0:
            print 'Data is valid.'
        else:
            print 'There is an error in the data'

c = Checksum()
c.to_send(4, ['0111', '1011', '1100', '0000', '0110'])
c.validate_receive(4, ['0111', '1011', '1100', '0000', '0110', '1001'])