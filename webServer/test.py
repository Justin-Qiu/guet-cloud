#!/usr/bin/env python
# -*- coding: utf-8 -*-

from server import user_log

print ''

try1 = user_log('1101120705', '123456')
print '1101120705',
if try1 == -1:
    print '密码错误！'
elif try1 == -2:
    print '用户名错误！'
else:
    print '登录成功！'
    for item in try1[:-1]:
        print item + ' ',
    print ''
if try1 != -1 and try1 != -2:
    for i in range(len(try1[-1])):
        for j in range(2):
            print try1[-1][i][j],
        print ''

print ''

try1 = user_log('1101120706', '654321')
print '1101120706',
if try1 == -1:
    print '密码错误！'
elif try1 == -2:
    print '用户名错误！'
else:
    print '登录成功！'
    for item in try1[:-1]:
        print item + ' ',
    print ''
if try1 != -1 and try1 != -2:
    for i in range(len(try1[-1])):
        for j in range(2):
            print try1[-1][i][j],
        print ''

print ''

try1 = user_log('1101120707', '123456')
print '1101120707',
if try1 == -1:
    print '密码错误！'
elif try1 == -2:
    print '用户名错误！'
else:
    print '登录成功！'
    for item in try1[:-1]:
        print item + ' ',
    print ''
if try1 != -1 and try1 != -2:
    for i in range(len(try1[-1])):
        for j in range(2):
            print try1[-1][i][j],
        print ''

print ''

try1 = user_log('1101120710', '123456')
print '1101120710',
if try1 == -1:
    print '密码错误！'
elif try1 == -2:
    print '用户名错误！'
else:
    print '登录成功！'
    for item in try1[:-1]:
        print item + ' ',
    print ''
if try1 != -1 and try1 != -2:
    for i in range(len(try1[-1])):
        for j in range(2):
            print try1[-1][i][j],
        print ''

print ''

try1 = user_log('1101120711', '123456')
print '1101120711',
if try1 == -1:
    print '密码错误！'
elif try1 == -2:
    print '用户名错误！'
else:
    print '登录成功！'
    for item in try1[:-1]:
        print item + ' ',
    print ''
if try1 != -1 and try1 != -2:
    for i in range(len(try1[-1])):
        for j in range(2):
            print try1[-1][i][j],
        print ''

print ''

try1 = user_log('1101120712', '123456')
print '1101120712',
if try1 == -1:
    print '密码错误！'
elif try1 == -2:
    print '用户名错误！'
else:
    print '登录成功！'
    for item in try1[:-1]:
        print item + ' ',
    print ''
if try1 != -1 and try1 != -2:
    for i in range(len(try1[-1])):
        for j in range(2):
            print try1[-1][i][j],
        print ''

print ''

try1 = user_log('1101120713', '654321')
print '1101120713',
if try1 == -1:
    print '密码错误！'
elif try1 == -2:
    print '用户名错误！'
else:
    print '登录成功！'
    for item in try1[:-1]:
        print item + ' ',
        print ''
    print ''
if try1 != -1 and try1 != -2:
    for i in range(len(try1[-1])):
        for j in range(2):
            print try1[-1][i][j],
        print ''

print ''

try1 = user_log('1101120714', '123456')
print '1101120714',
if try1 == -1:
    print '密码错误！'
elif try1 == -2:
    print '用户名错误！'
else:
    print '登录成功！'
    for item in try1[:-1]:
        print item + ' ',
        print ''
    print ''
if try1 != -1 and try1 != -2:
    for i in range(len(try1[-1])):
        for j in range(2):
            print try1[-1][i][j],
        print ''
