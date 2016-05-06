#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from distutils.core import setup

setup(
	name='TODO',
	version='0.0.1',
	author='Chenghao Qian',
	author_email='qch.jacob.jm@gmail.com',
	packages=['todo','todo.lib'],
	scripts=['todo/TODO'],
	package_data={'todo':['data/*.dat','data/usr/*/*.dat']},
	url='https://github.com/ChenghaoQ/Todo',
	license='COPYING.WTFPL',
	description='A simple todolist with cursor.'
)
