# -^- coding:utf-8 -^-

import inspect
import re

class ValidateException(Exception): pass


def validParam(*varargs, **keywords):
    '''验证参数的装饰器。'''

    varargs = map(_toStardardCondition, varargs)
    keywords = dict((k, _toStardardCondition(keywords[k]))
                    for k in keywords)

    def generator(func):
        args, varargname, kwname = inspect.getargspec(func)[:3]
        dctValidator = _getcallargs(args, varargname, kwname,
                                    varargs, keywords)
        # print 'dctValidator', dctValidator
        def wrapper(*callvarargs, **callkeywords):
            dctCallArgs = _getcallargs(args, varargname, kwname,
                                       callvarargs, callkeywords)
            # print 'dctCallArgs', dctCallArgs
            k, item = None, None
            try:
                for k in dctValidator:
                    if k == varargname:
                        for item in dctCallArgs[k]:
                            assert dctValidator[k](item)
                    elif k == kwname:
                        for item in dctCallArgs[k].values():
                            assert dctValidator[k](item)
                    else:
                        item = dctCallArgs[k]
                        assert dctValidator[k](item)
            except:
                raise ValidateException,\
                       ('%s() parameter validation fails, param: %s, value: %s(%s)'
                       % (func.func_name, k, item, item.__class__.__name__))

            return func(*callvarargs, **callkeywords)

        wrapper = _wrapps(wrapper, func)
        return wrapper

    return generator


def _toStardardCondition(condition):
    '''将各种格式的检查条件转换为检查函数'''

    if inspect.isclass(condition):
        return lambda x: isinstance(x, condition)

    if isinstance(condition, (tuple, list)):
        cls, condition = condition[:2]
        if condition is None:
            return _toStardardCondition(cls)

        if cls in (str, unicode) and condition[0] == condition[-1] == '/':
            return lambda x: (isinstance(x, cls)
                              and re.match(condition[1:-1], x) is not None)

        return lambda x: isinstance(x, cls) and eval(condition)

    return condition


def nullOk(cls, condition=None):
    '''这个函数指定的检查条件可以接受None值'''

    return lambda x: x is None or _toStardardCondition((cls, condition))(x)


def multiType(*conditions):
    '''这个函数指定的检查条件只需要有一个通过'''

    lstValidator = map(_toStardardCondition, conditions)
    def validate(x):
        for v in lstValidator:
            if v(x):
                return True
    return validate


def _getcallargs(args, varargname, kwname, varargs, keywords):
    '''获取调用时的各参数名-值的字典'''
    # print args, varargname, kwname, varargs, keywords

    dctArgs = {}
    varargs = tuple(varargs)
    keywords = dict(keywords)

    argcount = len(args)
    varcount = len(varargs)
    callvarargs = None

    if argcount <= varcount:
        for n, argname in enumerate(args):
            dctArgs[argname] = varargs[n]

        callvarargs = varargs[-(varcount-argcount):]

    else:
        for n, var in enumerate(varargs):
            dctArgs[args[n]] = var

        for argname in args[-(argcount-varcount):]:
            if argname in keywords:
                dctArgs[argname] = keywords.pop(argname)

        callvarargs = ()

    if varargname is not None:
        dctArgs[varargname] = callvarargs

    if kwname is not None:
        dctArgs[kwname] = keywords

    dctArgs.update(keywords)
    # print dctArgs

    return dctArgs


def _wrapps(wrapper, wrapped):
    '''复制元数据'''

    for attr in ('__module__', '__name__', '__doc__'):
        setattr(wrapper, attr, getattr(wrapped, attr))
    for attr in ('__dict__',):
        getattr(wrapper, attr).update(getattr(wrapped, attr, {}))

    return wrapper