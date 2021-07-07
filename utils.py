import logging
format = '%(asctime)s:%(levelname)s:%(message)s'
logging.basicConfig(filename="app.log",filemode='a',level=logging.DEBUG,format = format, datefmt='%d/%m/%Y%I:%M:%S %p')
logger = logging.getLogger()

