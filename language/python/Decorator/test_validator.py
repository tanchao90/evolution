# -^- coding:utf-8 -^-

#===============================================================================
# 测试 validator.py
#===============================================================================

from validator import validParam, nullOk, multiType, ValidateException

def _unittest(func, *cases):
    for case in cases:
        _functest(func, *case)


def _functest(func, isCkPass, *args, **kws):
    print func, isCkPass, args, kws
    if isCkPass:
        func(*args, **kws)
    else:
        try:
            func(*args, **kws)
            assert False
        except ValidateException:
            pass

def _test1_simple():
    #检查第一个位置的参数是否为int类型：
    @validParam(int)
    def foo1(i): pass
    _unittest(foo1,
              (True, 1),
              (False, 's'),
              (False, None))

    #检查名为x的参数是否为int类型：
    @validParam(x=int)
    def foo2(s, x): pass
    _unittest(foo2,
              (True, 1, 2),
              (False, 's', 's'))

    #验证多个参数：
    @validParam(int, int)
    def foo3(s, x): pass
    _unittest(foo3,
              (True, 1, 2),
              (False, 's', 2))

    #指定参数名验证：
    @validParam(int, s=str)
    def foo4(i, s): pass
    _unittest(foo4,
              (True, 1, 'a'),
              (False, 's', 1))

    #针对*和**参数编写的验证器将验证这些参数包含的每个元素：
    @validParam(varargs=int)
    def foo5(*varargs): pass
    _unittest(foo5,
              (True, 1, 2, 3, 4, 5),
              (False, 'a', 1))

    @validParam(kws=int)
    def foo6(**kws): pass
    _functest(foo6, True, a=1, b=2)
    _functest(foo6, False, a='a', b=2)

    @validParam(kws=int)
    def foo7(s, **kws): pass
    _functest(foo7, True, s='a', a=1, b=2)


def _test2_condition():
    #验证一个10到20之间的整数：
    @validParam(i=(int, '10<x<20'))
    def foo1(x, i): pass
    _unittest(foo1,
              (True, 1, 11),
              (False, 1, 'a'),
              (False, 1, 1))

    #验证一个长度小于20的字符串：
    @validParam(s=(str, 'len(x)<20'))
    def foo2(a, s): pass
    _unittest(foo2,
              (True, 1, 'a'),
              (False, 1, 1),
              (False, 1, 'a'*20))

    #验证一个年龄小于20的学生：
    class Student(object):
        def __init__(self, age): self.age=age

    @validParam(stu=(Student, 'x.age<20'))
    def foo3(stu): pass
    _unittest(foo3,
              (True, Student(18)),
              (False, 1),
              (False, Student(20)))

    #验证一个由数字组成的字符串：
    @validParam(s=(str, r'/^\d*$/'))
    def foo4(s): pass
    _unittest(foo4,
              (True, '1234'),
              (False, 1),
              (False, 'a1234'))


def _test3_nullok():
    @validParam(i=nullOk(int))
    def foo1(i): pass
    _unittest(foo1,
              (True, 1),
              (False, 'a'),
              (True, None))

    @validParam(i=nullOk(int, '10<x<20'))
    def foo2(i): pass
    _unittest(foo2,
              (True, 11),
              (False, 'a'),
              (True, None),
              (False, 1))


def _test4_multitype():
    @validParam(s=multiType(int, str))
    def foo1(s): pass
    _unittest(foo1,
              (True, 1),
              (True, 'a'),
              (False, None),
              (False, 1.1))

    @validParam(s=multiType((int, 'x>20'), nullOk(str, '/^\d+$/')))
    def foo2(s): pass
    _unittest(foo2,
              (False, 1),
              (False, 'a'),
              (True, None),
              (False, 1.1),
              (True, 21),
              (True, '21'))

def _main():
    d = globals()
    from types import FunctionType
    print d
    for f in d:
        if f.startswith('_test'):
            f = d[f]
            if isinstance(f, FunctionType):
                f()

if __name__ == '__main__':
    _main()

    _test1_simple()