from typing import Any, Dict, Union

from aiocqhttp.api import Api

from pathlib import Path
import os
import configparser


class Custom:
    def __init__(self, bot_api: Api):
        self.api = bot_api
        self.inipath = Path(os.path.dirname(__file__)).parent / 'yobot_data' / 'groups.ini'

    async def execute_async(self, ctx: Dict[str, Any]) -> Union[None, bool, str]:
        # 多CQ适配：触发写入ini，群号=bot号
        cmd = ctx['raw_message']
        if cmd == '手动添加群记录' or cmd == '修复网页催刀':
            config = configparser.RawConfigParser()
            config.read(str(self.inipath))
            config.set('GROUPS', str(ctx['group_id']), str(ctx['self_id']))
            with open(str(self.inipath), 'w') as f:
                config.write(f)
            return '群记录添加成功！'
