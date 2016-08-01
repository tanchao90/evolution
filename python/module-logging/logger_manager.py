# -*- coding: utf-8 -*-

__author__ = 'Tan Chao'

'''
Python logging module wrapper.
'''

import logging
import logging.handlers as LH
import types
import os
import platform
import time
import traceback


# Logging Levels
# From high to low
LEVEL_CRITICAL	= logging.CRITICAL # 50
LEVEL_ERROR		= logging.ERROR # 40
LEVEL_WARNING	= logging.WARNING # 30, ==WARN
LEVEL_INFO		= logging.INFO # 20
LEVEL_DEBUG		= logging.DEBUG # 10
LEVEL_NOTSET	= logging.NOTSET # 0
LEVEL_CUSTOME	= 5 # define your own level


# handler type
HANDLER_STREAM		= 'stream'
HANDLER_SYSLOG		= 'syslog'
HANDLER_FILE		= 'file'
HANDLER_CUSTOME		= 'custom'


# Logger Config
DATE_FMT 		= '%Y-%m-%d_%H-%M-%S'
SYSLOG_ADDRESS	= '/dev/log'
SYSLOG_FACILITY	= LH.SysLogHandler.LOG_LOCAL1
LOG_PATH		= 'log' + os.sep
FORMATTER		= '-'.join(['%(asctime)s', '%(tag)s', '%(name)s', '%(filename)s', '%(levelname)s', '%(message)s'])


def log_traceback_hook(self):
	'''self is logger
	Catch except and output it by logger.
	'''
	self.error(traceback.format_exc())


def get_cur_time():
	return time.strftime(DATE_FMT)


class LoggerManager(object):
	created_loggers = set()
	log_level = LEVEL_DEBUG
	log_handler = HANDLER_STREAM
	log_tag = ''
	custom_handler = None

	@staticmethod
	def get_logger(logger_name):
		'''If the logger is exist, then return it directly.'''
		if logger_name not in LoggerManager.created_loggers:
			LoggerManager.create_logger(logger_name)

		logger = logging.getLogger(logger_name)
		if LoggerManager.log_handler == HANDLER_SYSLOG and platform.system() == 'Linux':
			logger = logging.LoggerAdapter(logger, {'logger_name': logger_name})

		return logger

	@staticmethod
	def create_logger(logger_name):
		# create logger
		logger = logging.getLogger(logger_name)
		logger.log_except = types.MethodType(log_traceback_hook, logger, logger.__class__) # add a method to logger
		logger.setLevel(LoggerManager.log_level)

		# create handler
		if LoggerManager.log_handler == HANDLER_SYSLOG:
			if platform.system() == 'Linux':
				handler = LH.SysLogHandler(SYSLOG_ADDRESS, facility=SYSLOG_FACILITY)
			else: # Windows, Mac
				handler = logging.FileHandler(LoggerManager.get_filename(), encoding='utf8')
		elif LoggerManager.log_handler == HANDLER_FILE:
			handler = logging.FileHandler(LoggerManager.get_filename(), encoding='utf8')
		elif LoggerManager.log_handler == HANDLER_CUSTOME:
			handler = LoggerManager.custom_handler()
		else:
			handler = logging.StreamHandler()

		# create formatter
		fmt = FORMATTER.replace('%(tag)s', LoggerManager.log_tag)
		formatter = logging.Formatter(fmt)

		handler.setFormatter(formatter)
		handler.setLevel(LoggerManager.log_level)
		logger.addHandler(handler)

		LoggerManager.created_loggers.add(logger_name)

	@staticmethod
	def get_filename():
		return LOG_PATH + LoggerManager.log_tag + "_" + get_cur_time() + '.log'

	@staticmethod
	def set_log_level(level):
		LoggerManager.log_level = level
		for name in LoggerManager.created_loggers:
			logger = logging.getLogger(name)
			logger.setLevel(level)
			for handler in logger.handlers:
				handler.setLevel(level)

	@staticmethod
	def set_log_handler(handler):
		LoggerManager.log_handler = handler

	@staticmethod
	def set_log_tag(log_tag):
		LoggerManager.log_tag = log_tag

	@staticmethod
	def set_custom_handler(handler):
		LoggerManager.log_handler = HANDLER_CUSTOME
		LoggerManager.custom_handler = handler


class Logger(object):
	def __init__(self, logger):
		self.logger = logger

	def log(self, log):
		self.logger.info('%s' % (log))


def main():
	LoggerManager.set_log_tag('app')
	LoggerManager.set_log_level(LEVEL_INFO)

	logger = LoggerManager.get_logger('client')
	logger.debug('debug message')
	logger.info('info message')
	logger.warn('warn message')
	logger.error('error message')
	logger.critical('critical message')
	logger.exception('exception message')

	LoggerManager.set_log_level(LEVEL_DEBUG)
	logger.debug('debug message new......')

	loggerWraper = Logger(logger)
	loggerWraper.log('test Logger')

	LoggerManager.set_log_handler(HANDLER_SYSLOG)
	loggerFile = LoggerManager.get_logger('server')
	loggerFile.info('start ok.')

	try:
		print(1/0)
	except:
		logger.log_except()


if __name__ == '__main__':
	main()
