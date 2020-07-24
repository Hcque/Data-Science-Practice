import time, sys
from HTMLTestRunner import HTMLTestRunner
import unittest
test_dir = './interface'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')

if __name__ == '__main__':
    # test_data
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    # print(now)
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='Guest Manage System Interface Test Report',
                            )
    runner.run(discover, None, None)
    fp.close()


