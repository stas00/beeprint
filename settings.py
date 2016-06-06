# -*- coding:utf-8 -*-
import sys
import types
from . import constants as C

outfile = sys.stdout
encoding = 'utf-8'
maxDeep = 5
leading = u'  '
newline = False
write_to_buffer_when_execute = False
bufferHandle = sys.stdout
tuple_in_line = True
list_in_line = True
# 过滤以 x 开头的属性
prop_leading_filters = ["__", "func_"]
# 根据类型过滤对象的属性
prop_filters = [types.MethodType]

# >> 优先策略
priority_strategy = C._PS_CONTENT_FIRST

