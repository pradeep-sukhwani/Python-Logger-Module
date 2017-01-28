import logging  # import logging
import test  # import test

def main_func():
    '''function that creates a file called results.log with a level
        info (i.e. to confirm that function works properly or not)
        and then print started and some lines and then calling
        addition function from test.py
    '''
    logging.basicConfig(filename='results.log', level=logging.INFO)
    logging.info('Started')
    logging.info('-'*10)
    test.add(2,5)
    logging.info('-'*10)
    logging.info('Finished')


test_func()