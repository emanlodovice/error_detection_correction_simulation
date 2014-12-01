class CRC(object):

    def xor(self, binary1, binary2):
        if len(binary1) == 1:
            if binary1 == binary2:
                return '0'
            else:
                return '1'
        else:
            result = ''
            for i in range(len(binary1)):
                result += self.xor(binary1[i], binary2[i])
            return self.remove_leading(result)

    def remove_leading(self, binary):
        while len(binary) > 0:
            if binary[0] == '0':
                binary = binary[1:]
            else:
                break;
        return binary

    def add_leading(self, binary, length):
        return '0'*(length-len(binary)) + binary

    def get_remainder(self, data, divisor):
        while len(data) >= len(divisor):
            b1 = data[0:len(divisor)]
            result = self.xor(b1, divisor)
            data = result + data[len(divisor):]
        return self.add_leading(data, len(divisor)-1)

    def to_send(self, data, divisor):
        print 'Data to send:', data + self.get_remainder(
            data + ('0'*(len(divisor)-1)), divisor)

    def validate_receive(self, data, divisor):
        if self.get_remainder(data, divisor) == '0' * (len(divisor)-1):
            print 'Data is valid.'
        else:
            print 'There is an error in the data'

crc = CRC()
crc.to_send('1001', '1011')
crc.validate_receive('1001110', '1011')