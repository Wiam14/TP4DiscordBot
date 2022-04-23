import logging

class TheLog():
    def __init__(self):
        logging.basicConfig(filename='logs.log', format='%(filename)s: %(message)s', level=logging.DEBUG)

    def ErrorMsg(self):
        logging.warning("warning message")
    
    def infolog(self,msg):
        logging.info(str(msg))
        print(str(msg))

    def SaveMsg(self,author,msg):
        logging.debug(str(author)+": "+str(msg))
