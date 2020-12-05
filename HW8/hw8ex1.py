class Data:
    def __init__(self, data=''):
        self.data = data

    @classmethod
    def m_1(cls, data):
        print(data.replace('-', '.'))

    @staticmethod
    def m_2(data):
        if (1 <= int(data.split('-')[0]) <= 31) and (1 <= int(data.split('-')[1]) <= 12) and \
                (1 <= int(data.split('-')[2]) <= 3000):
            print('Everything is fine!')
        else:
            print('Enter valid numbers!')


# a = Data('23-03-2828')
Data.m_2('23-03-2828')
Data.m_1('23-03-2828')
