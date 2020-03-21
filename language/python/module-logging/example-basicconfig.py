#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Tan Chao'

'''
logger wrapper.
'''


import logging
import logging.config
import sys


def test_logging():
	"""
	learn how to use logging
	"""
	logging.basicConfig(
		level=logging.DEBUG,
		format='[%(asctime)s] %(filename)s[line:%(lineno)d][fun:%(funcName)s] %(levelname)s %(message)s',
		datefmt='%Y-%m-%d %H:%M:%S',
		filename='log/myapp.log',
		filemode='w',
		stream=sys.stderr
		)

	logging.debug('This is a message')
	logging.info('This is a message')
	logging.warning('This is a message')


test_logging()