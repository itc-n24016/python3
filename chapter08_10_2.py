import logging 
def devide(x, y):
    return x / y

logging.basicConfig(filename='testlog.log', level=logging.WARNING,
        format='%(levelname)s:%(actime)s:%(message)s')

try:
    ret = devide(10, 0)
except:
    logging.exception('test exception message')
logging.shutdown()
