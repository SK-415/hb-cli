import nonebot
from os import path
from nonebot.log import logger, default_format


nonebot.init()
app = nonebot.get_asgi()

nonebot.load_builtin_plugins()
nonebot.load_plugin("haruka_bot")

# Modify some config / config depends on loaded configs
# 
# config = nonebot.get_driver().config
# do something...


def run():
    logger.add(path.join('log', "error.log"),
           rotation="00:00",
           retention='1 week',
           diagnose=False,
           level="ERROR",
           format=default_format,
           encoding='utf-8'
           )
    
    nonebot.run(app="hb_cli.bot:app")