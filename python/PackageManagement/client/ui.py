# -*- coding: utf-8 -*-


__all__ = ['Point']


class Point(object):
	def __init__(self, x, y):
		super(Point, self).__init__()
		self.x = x
		self.y = y

	def draw(self):
		print 'point x:%s, y:%s' % (self.x, self.y)
