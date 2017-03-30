import hashlib
import unittest
from collections import namedtuple
import os

'''
I love Python;sha1;9233eac58259dd3a13d6c9c59f8001823b6b1fee
Я люблю Питон;md5;50b461d17299cc037a432307a2d93a55
'''


Calc = namedtuple('Calc', ('text', 'hash_alg', 'code'))


def get_calc_hash(line):
    '''
    Вычисление хэш суммы. Делится строка, определяем алгоритм шифрования,
    шифруем строку, ранее переведенную в бинарный код.
    :param list: 
    :return: res
    '''
    line = line.split(';')
    if line:
        data = Calc(*line)
        text = data.text.encode('utf-8')
        # text = data.text
        hash_alg = data.hash_alg
        if hash_alg == 'md5':
            h = hashlib.md5()
        elif hash_alg == 'sha512':
            h = hashlib.sha512()
        elif hash_alg == 'sha1':
            h = hashlib.sha1()
        h.update(text)
        res = h.hexdigest()
    else:
        res = ()
    return res

class TestCalc(unittest.TestCase):

    def test_get_calc_hash(self):
        self.assertEqual(get_calc_hash('I love Python;sha1;'),
                         ('9233eac58259dd3a13d6c9c59f8001823b6b1fee'))

res = []
with open('need_hashes.csv', 'r') as f:
    for ss in f:
        code = get_calc_hash(ss)
        print(code)
        res.append(code)

with open('need_hashes.csv', 'w') as f:
    for ss in res:
        f.write(ss + '\n')


if __name__ == "__main__":
    unittest.main()