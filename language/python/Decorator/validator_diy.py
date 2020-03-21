# -^- coding:utf-8 -^-

# --------------------------------------------------------------
# Author: TanChao
# Date  : 2015.09.23
# Intro : 用装饰器实现参数类型判断
# --------------------------------------------------------------

import inspect
import re


class ValidateException(Exception):
	pass


def validParam(*varargs, **keywords):
	'''验证参数的装饰器。'''

	varargs = map(_toStardardCondition, varargs)
	keywords = dict((k, _toStardardCondition(keywords[k])) for k in keywords)

	def generator(func):
		# 获取func中的参数名称、非关键字可变长参数名称、关键字参数名称
		args, varargname, kwname = inspect.getargspec(func)[:3]
		# dctValidator: 参数名-值验证函数的字典
		dctValidator = _getCallArgs(args, varargname, kwname, varargs, keywords)

		def wrapper(*callvarargs, **callkeywords):
			# dctCallArgs: 参数名-值的字典
			dctCallArgs = _getCallArgs(args, varargname, kwname, callvarargs, callkeywords)
			# print 'dctValidator:', dctValidator
			# print 'dctCallArgs:', dctCallArgs

			k, item, result = None, None, None
			try:
				# 依此检查每个条件
				for k in dctValidator:
					if k == varargname:    # 检查非关键字可变长参数
						for item in dctCallArgs[k]:
							result = dctValidator[k](item)
							assert True == result
					elif k == kwname:    # 检查关键字参数
						for item in dctCallArgs[k].values():
							result = dctValidator[k](item)
							assert True == result
					else:    # 检查普通参数
						item = dctCallArgs[k]
						result = dctValidator[k](item)
						assert True == result
			except Exception, e:
				print e
				print inspect.getsource(dctValidator[k])
				error_info = ('%s() parameter validation fails, param: %s, value: %s(%s), validator: %s'
					% (func.func_name, k, item, item.__class__.__name__, result))
				raise ValidateException, error_info

			return func(*callvarargs, **callkeywords)

		wrapper = _wrapps(wrapper, func)
		return wrapper

	return generator


def nullOk(cls, condition=None):
	'''这个函数指定的检查条件可以接受None值'''

	return lambda x: x is None or _toStardardCondition((cls, condition))(x)


def multiType(*conditions):
	'''这个函数指定的检查条件只需要有一个通过'''

	# 将所有条件转换为检查对应的函数
	lstValidator = map(_toStardardCondition, conditions)
	def validate(x):
		for v in lstValidator:
			if v(x):
				return True
	return validate


def _toStardardCondition(condition):
	'''将各种格式的检查条件转换为检查函数'''

	# class condition
	if inspect.isclass(condition):
		info = "must be %s type" % condition.__name__
		return lambda x: isinstance(x, condition) or info

	if isinstance(condition, (tuple, list)):
		cls, condition = condition[:2]
		if condition is None:
			return _toStardardCondition(cls)

		# regular condition
		if cls in (str, unicode) and condition[0] == condition[-1] == '/':
			info = 'must match regular expression: %s' % condition
			return lambda x: (isinstance(x, cls) and re.match(condition[1:-1], x) is not None) or info

		# pure str condition
		info = 'must satisfy rule: %s' % condition
		return lambda x: (isinstance(x, cls) and eval(condition)) or info

	# fcuntion condition
	return condition


def _getCallArgs(args, varargname, kwname, varargs, keywords):
	'''获取调用时的各参数名-值验证函数的字典 or 各参数名-值的字典
	args: 参数名称
	varargname: 非关键字可变长参数名称
	kwname: 关键字参数名称
	varargs: 非关键字可变长参数(tuple) (参数类型 or 参数值)
	keywords: 关键字参数(dict) (参数类型 or 参数值)
	'''

	dictArgs = {}
	varargs = tuple(varargs)
	keywords = dict(keywords)

	argcount = len(args)
	varcount = len(varargs)
	callvarargs = None

	if argcount <= varcount:
		# 参数少，因此先遍历参数，依此位每个参数赋值
		for n, argname in enumerate(args):
			dictArgs[argname] = varargs[n]

		callvarargs = varargs[-(varcount-argcount):]
	else:
		#值少，因此先遍历值，依此位每个参数赋值
		for n, var in enumerate(varargs):
			dictArgs[args[n]] = var

		# 处理剩余的参数
		for argname in args[-(argcount-varcount):]:
			if argname in keywords:
				dictArgs[argname] = keywords.pop(argname)
		callvarargs = ()

	if varargname is not None:
		dictArgs[varargname] = callvarargs

	if kwname is not None:
		dictArgs[kwname] = keywords

	dictArgs.update(keywords)
	return dictArgs


def _wrapps(wrapper, wrapped):
	'''复制元数据'''

	for attr in ('__module__', '__name__', '__doc__'):
		setattr(wrapper, attr, getattr(wrapped, attr))
	for attr in ('__dict__',):
		getattr(wrapper, attr).update(getattr(wrapped, attr, {}))

	return wrapper
