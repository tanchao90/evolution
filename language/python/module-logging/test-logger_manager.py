# -*- coding: utf-8 -*-

__author__ = 'Tan Chao'

'''
Test logger_manager module.
'''


from logger_manager import LoggerManager

logger = LoggerManager.get_logger('test')
logger.info('start...')
logger.debug('hello world')
logger.error('stop error')

try:
	print(2/0)
except Exception, e:
	logger.log_except()