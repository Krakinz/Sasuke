import platform
import psutil
import os
my_system = platform.uname()
print('⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡')
print(f'ꪶ࿋྄ིᤢꫂ𝐒𝐲𝐬𝐭𝐞𝐦: {my_system.system}')
print(f'ꪶ࿋྄ིᤢꫂ𝐍𝐨𝐝𝐞 𝐍𝐚𝐦𝐞: {my_system.node}')
print(f'ꪶ࿋྄ིᤢꫂ𝐑𝐞𝐥𝐞𝐚𝐬𝐞: {my_system.release}')
print(f'ꪶ࿋྄ིᤢꫂ𝐕𝐞𝐫𝐬𝐢𝐨𝐧: {my_system.version}')
print(f'ꪶ࿋྄ིᤢꫂ𝐌𝐚𝐜𝐡𝐢𝐧𝐞: {my_system.machine}')
print(f'ꪶ࿋྄ིᤢꫂ𝐌𝐞𝐦𝐨𝐫𝐲: {psutil.virtual_memory()}')
print(f'ꪶ࿋྄ིᤢꫂ𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐨𝐫: {my_system.processor}')
print('''
⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
                ███╗   ███╗██╗███████╗██╗   ██╗██╗  ██╗██╗
                ████╗ ████║██║╚══███╔╝██║   ██║██║ ██╔╝██║
                ██╔████╔██║██║  ███╔╝ ██║   ██║█████╔╝ ██║
                ██║╚██╔╝██║██║ ███╔╝  ██║   ██║██╔═██╗ ██║
                ██║ ╚═╝ ██║██║███████╗╚██████╔╝██║  ██╗██║
                ╚═╝     ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
''')
os.system('node Sasuke_server/Sasuke.js')