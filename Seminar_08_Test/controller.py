import view
import imp
import exp
import logger
# import search

def start():
    if view.mod() == '1':
        info = view.exp()
        exp.expp(info)
        logger.log_info(info)

    else:
        info = view.inpp()
        imp.impo(info)
        logger.log_info(info)