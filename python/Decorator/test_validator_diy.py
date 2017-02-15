# -^- coding:utf-8 -^-

#===============================================================================
# 测试 validator_diy.py
#===============================================================================

from validator_diy import validParam, nullOk, multiType, ValidateException


def validName(name):
	if not isinstance(name, str) or name is None or name == '':
		return 'name must be a non-null string'
	return True


@validParam(name=validName)
def findUserByName(name):
	print 'findUserByName', name


# test
findUserByName('Peter')
try:
	findUserByName(1234) # 会抛出参数错误的异常，异常中包含错误原因
except Exception as e:
	print str(e)




