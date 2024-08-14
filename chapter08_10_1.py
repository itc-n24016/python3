import logging

logging.basicConfig(filename='practice1.log', level=logging.WARNING)
logging.warning('1')
logging.error('2')
logging.debug('3')
logging.info('4')
logging.shutdown()

with open('practice1.log', 'r') as f:
    a = f.read()
    print(a)

print('answer:2')
