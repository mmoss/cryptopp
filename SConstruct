import os

AddOption('--prefix',
					dest='prefix',
					type='string',
					nargs=1,
					action='store',
					metavar='DIR',
					help='installation prefix',
					default=Dir('#target'))

AddOption('--enable-debug',
					dest='enable-debug',
					action='store_true',
					metavar='DEBUG',
					help='include debug flags when compiling')

AddOption('--shared',
					dest='shared',
					action='store_true',
					metavar='SHARED',
					help='build a shared library')

env = Environment(PREFIX = GetOption('prefix'),
									DEBUG = True if GetOption('enable-debug') else False,
									SHARED = True if GetOption('shared') else False,
									MODE = 'debug' if GetOption('enable-debug') else 'release')

if env['DEBUG']:
	env.AppendUnique(CCFLAGS = '-g')

env.SConscript('src/SConscript', variant_dir='#target/build/$MODE', duplicate=0, exports='env')
