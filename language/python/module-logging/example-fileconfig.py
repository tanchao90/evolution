#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Tan Chao'

'''
logger wrapper.
use fileConfig.
'''


import logging
import logging.config
import datetime
import os


if not os.path.isdir('log/'):
	os.mkdir('log/')
logging.config.fileConfig('fileconfig.conf')

cur_path = os.path.abspath(os.path.curdir)
log_path = cur_path + os.sep + 'log' + os.sep


def _get_logger(logger_name, file_name):
	"""
	get logger by logger_name
	reset the handler to output log in new file (file_name)
	"""
	logger = logging.getLogger(logger_name)

	old_handlers = []
	new_handlers = []

	for hand in logger.handlers:
		if isinstance(hand, logging.FileHandler):
			new_hand = logging.FileHandler(file_name, hand.mode)   #name, w/a
			new_hand.setLevel(hand.level)
			new_hand.setFormatter(hand.formatter)

			old_handlers.append(hand)
			new_handlers.append(new_hand)

	for hand in old_handlers:
		logger.removeHandler(hand)

	for hand in new_handlers:
		logger.addHandler(hand)

	return logger


def get_current_time():
	cur_time = datetime.datetime.now()
	return cur_time.strftime('%Y-%m-%d_%H-%M-%S')


loggers = {}


def get_logger(logger_name):
	file_name = log_path + '{}_{}.log'.format(logger_name, get_current_time())

	if logger_name not in loggers:
		loggers[logger_name] = _get_logger(logger_name, file_name)

	return loggers[logger_name]


if __name__ == '__main__':
	logger1 = get_logger('root')
	logger1.info("test1111111111")

	logger11 = get_logger('root.root')
	logger11.info("test1111122222")

	logger2 = get_logger('root.general')
	logger2.info("test2222222222")
	print(logger2.name)

	logger3 = get_logger('root.general')
	logger3.info("test33333333333")

	logger4 = logger1.getChild('general')
	logger4.info('test444444444444444')
	print(logger4.name)

	logger5 = get_logger('test')
	logger5.info('gggggg')

	print(id(logger1), id(logger11), id(logger2), id(logger3), id(logger4), id(logger5))