import unittest,datetime
import HtmlTestRunner

from utils.init_folder import init_html_folder

suite = unittest.defaultTestLoader.discover('./../exec_manage', pattern = '*.py')

if __name__ == '__main__':
    #runner = unittest.TestRunner()
    date_time = datetime.datetime.now()
    date = date_time.strftime('%Y-%m-%d')
    report_time = date_time.strftime('%Y-%m-%d')
    init_html_folder(date)
    runner = HtmlTestRunner.HTMLTestRunner(output='./../report/html/')
    runner.run(suite)

