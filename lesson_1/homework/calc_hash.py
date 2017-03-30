import hashlib
import unittest
from collections import namedtuple

'''
I love Python;sha1;9233eac58259dd3a13d6c9c59f8001823b6b1fee
'''


Calc = namedtuple('Calc', ('text', 'hash_alg'))


def get_calc_hash(line):
    '''
    Вычисление хэш суммы
    :param list: 
    :return: 
    '''
    line = line.split(';')
    if line:
        data = Calc(*line)
        text = data.text.encode('utf-8')
        hash_alg = data.hash_alg
        if hash_alg == 'md5':
            h = hashlib.md5()
        elif hash_alg == 'sha512':
            h = hashlib.sha512()
        elif hash_alg == 'sha1':
            h = hashlib.sha1()
        h.update(text)
        res = h.hexdigest
    else:
        res = ()
    return res

class TestCalc(unittest.TestCase):

    def test_get_calc_hash(self):
        self.assertEqual(get_calc_hash('I love Python;sha1'),
                         ('9233eac58259dd3a13d6c9c59f8001823b6b1fee'))

if __name__ == "__main__":
    unittest.main()

