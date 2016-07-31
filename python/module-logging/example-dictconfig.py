#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Tan Chao'

'''
logger wrapper.
use dictConfig.
'''


import logging
import logging.config
import yaml


def testLogging():
	with open('dictconfig.yaml') as f:
		dict_config = yaml.load(f)

	logging.config.dictConfig(dict_config)

	logger1 = logging.getLogger('foo.bar.baz')
	logger2 = logging.getLogger('foo')
	logger3 = logging.getLogger('bar')

	print(logger1, logger2, logger3)
	logger1.error('aaa')
	logger2.error('bbb')
	logger3.error('ccc')


if __name__ == '__main__':
	# main()
	# test()
	testLogging()