import logging
from loguru import *
from zipfile import ZipFile
import pyAesCrypt as krakinzr
from termcolor import *
import shutil
from datetime import *
from os import getenv
import os
from dotenv import load_dotenv
load_dotenv('./Sasuke_core.env')
Ssuke= getenv('HEROKU', None)
Sasuk = getenv('HEROKU', None)
Sasuke = getenv('CODE', None)
BFS = 64 * 1024
# ⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
#                 ███╗   ███╗██╗███████╗██╗   ██╗██╗  ██╗██╗
#                 ████╗ ████║██║╚══███╔╝██║   ██║██║ ██╔╝██║
#                 ██╔████╔██║██║  ███╔╝ ██║   ██║█████╔╝ ██║
#                 ██║╚██╔╝██║██║ ███╔╝  ██║   ██║██╔═██╗ ██║
#                 ██║ ╚═╝ ██║██║███████╗╚██████╔╝██║  ██╗██║
#                 ╚═╝     ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
# ⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
class InterceptHandler(logging.Handler):
    LEVELS_MAP = {
        logging.CRITICAL:
        'CRITICAL',
        logging.ERROR:
        'ERROR',
        logging.WARNING:
        'WARNING',
        logging.INFO:
        'INFO',
        logging.DEBUG:
        'DEBUG'}

    def _get_level(
            self,
            record):
        return self.LEVELS_MAP.get(
            record.levelno,
            record.levelno)

    def emit(self, record):
        logger_opt = logger.opt(
            depth=6,
            exception=record.exc_info,
            ansi=True,
            lazy=True)
        logger_opt.log(self._get_level(record),
                       record.getMessage())


logging.basicConfig(handlers=[InterceptHandler()],
                    level=logging.INFO)
# ⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
#                 ███╗   ███╗██╗███████╗██╗   ██╗██╗  ██╗██╗
#                 ████╗ ████║██║╚══███╔╝██║   ██║██║ ██╔╝██║
#                 ██╔████╔██║██║  ███╔╝ ██║   ██║█████╔╝ ██║
#                 ██║╚██╔╝██║██║ ███╔╝  ██║   ██║██╔═██╗ ██║
#                 ██║ ╚═╝ ██║██║███████╗╚██████╔╝██║  ██╗██║
#                 ╚═╝     ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
# ⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
LOGS = logging.getLogger(__name__)
if Sasuke is not None:
    if os.path.exists('Zz4xp01pklo'):
        pass
    else:
        try:
            os.system('https://github.com/GasComIT/Zz4xp01pklo.git')
        except Exception as e:
            if Ssuke == 'HEROKU':
                LOGS.info(str(e))
            else:
                print(e)
            pass
    if os.path.exists('xp0e.zip'):
        pass
    else:
        files = [
            'Zz4xp01pklo/xp0e.zip',
            'Zz4xp01pklo/2xp0e.zip',
            'Zz4xp01pklo/3xp0e.zip',
            'Zz4xp01pklo/4xp0e.zip',
            'Zz4xp01pklo/5xp0e.zip',
            'Zz4xp01pklo/6xp0e.zip',
            'Zz4xp01pklo/7xp0e.zip',
            'Zz4xp01pklo/8xp0e.zip'
        ]
        for f in files:
            shutil.move(f, '.')
        shutil.rmtree('Zz4xp01pklo')
# ⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
#                 ███╗   ███╗██╗███████╗██╗   ██╗██╗  ██╗██╗
#                 ████╗ ████║██║╚══███╔╝██║   ██║██║ ██╔╝██║
#                 ██╔████╔██║██║  ███╔╝ ██║   ██║█████╔╝ ██║
#                 ██║╚██╔╝██║██║ ███╔╝  ██║   ██║██╔═██╗ ██║
#                 ██║ ╚═╝ ██║██║███████╗╚██████╔╝██║  ██╗██║
#                 ╚═╝     ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
# ⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
    try:
        with ZipFile('xp0e.zip') as zf:
            zf.extractall()
        with ZipFile('2xp0e.zip') as zf:
            zf.extractall()
        with ZipFile('3xp0e.zip') as zf:
            zf.extractall()
        with ZipFile('4xp0e.zip') as zf:
            zf.extractall()
        with ZipFile('5xp0e.zip') as zf:
            zf.extractall()
        with ZipFile('6xp0e.zip') as zf:
            zf.extractall()
        with ZipFile('7xp0e.zip') as zf:
            zf.extractall()
        with ZipFile('8xp0e.zip') as zf:
            zf.extractall()
        try:
            files = [
                '2xp0e.zip',
                '3xp0e.zip',
                '4xp0e.zip',
                '5xp0e.zip',
                '6xp0e.zip',
                '7xp0e.zip',
                '8xp0e.zip'
            ]
            for f in files:
                os.remove(f)
        except Exception as e:
            if Ssuke == 'HEROKU':
                LOGS.info(str(e))
            else:
                print(e)
            pass
    except Exception as e:
        if Ssuke == 'HEROKU':
            LOGS.info(str(e))
        else:
            print(e)
        pass
# ⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
#                 ███╗   ███╗██╗███████╗██╗   ██╗██╗  ██╗██╗
#                 ████╗ ████║██║╚══███╔╝██║   ██║██║ ██╔╝██║
#                 ██╔████╔██║██║  ███╔╝ ██║   ██║█████╔╝ ██║
#                 ██║╚██╔╝██║██║ ███╔╝  ██║   ██║██╔═██╗ ██║
#                 ██║ ╚═╝ ██║██║███████╗╚██████╔╝██║  ██╗██║
#                 ╚═╝     ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
# ⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
    if os.path.isfile('xp0e.py'):
        try:
            Krakinzr.encryptFile('xp0e.py', 'xp0e.aes', Sasuk, BFS)
            os.remove('xp0e.py')
        except Exception as e:
            if Ssuke == 'HEROKU':
                LOGS.info(str(e))
            else:
                print(e)
        pass
    else:
        pass

    try:
        Krakinzr.decryptFile('xp0e.aes', 'xp0edoc.py', Sasuk, BFS)
    except Exception as e:
        if Sasuke == 'HEROKU':
            LOGS.info(str(e))
        else:
            print(e)
        pass

    try:
        files = [
            '2xp0e.aes',
            '3xp0e.aes',
            '4xp0e.aes',
            '5xp0e.aes',
            '6xp0e.aes',
            '7xp0e.aes',
            '8xp0e.aes'
        ]
        for f in files:
            os.remove(f)
    except Exception as e:
        if Ssuke == 'HEROKU':
            LOGS.info(str(e))
        else:
            print(e)
        pass
# ⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
#                 ███╗   ███╗██╗███████╗██╗   ██╗██╗  ██╗██╗
#                 ████╗ ████║██║╚══███╔╝██║   ██║██║ ██╔╝██║
#                 ██╔████╔██║██║  ███╔╝ ██║   ██║█████╔╝ ██║
#                 ██║╚██╔╝██║██║ ███╔╝  ██║   ██║██╔═██╗ ██║
#                 ██║ ╚═╝ ██║██║███████╗╚██████╔╝██║  ██╗██║
#                 ╚═╝     ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
# ⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
    try:
        from xp0edoc import *
        if Sasuke in YYUCCitinZfgQdrclRPOP:
            print('ꪶ࿋྄ིᤢꫂ  Correct Krakinz code ꪶ࿋྄ིᤢꫂ')
            os.remove('xp0e.zip')
            os.remove('xp0e.aes')
            os.remove('xp0edoc.py')
            shutil.rmtree('__pycache__')
            if os.path.exists('Sasuke_server/Lab.py'):
                os.system('python3 Sasuke_server/Lab.py')
            else:
                pass
        else:
            os.system('clear')
            print('❌❌  Wrong Krakinz code ❌❌')
            os.remove('xp0e.zip')
            os.remove('xp0e.aes')
            os.remove('xp0edoc.py')
            shutil.rmtree('__pycache__')
            pass
    except Exception as e:
        if Ssuke == 'HEROKU':
            LOGS.info(str(e))
        else:
            print(e)
        pass
# ⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
#                 ███╗   ███╗██╗███████╗██╗   ██╗██╗  ██╗██╗
#                 ████╗ ████║██║╚══███╔╝██║   ██║██║ ██╔╝██║
#                 ██╔████╔██║██║  ███╔╝ ██║   ██║█████╔╝ ██║
#                 ██║╚██╔╝██║██║ ███╔╝  ██║   ██║██╔═██╗ ██║
#                 ██║ ╚═╝ ██║██║███████╗╚██████╔╝██║  ██╗██║
#                 ╚═╝     ╚═╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝
# ⬡==========================⬡    ꪶ࿋྄ིᤢꫂ Sasuke ꪶ࿋྄ིᤢꫂ    ⬡==========================⬡
