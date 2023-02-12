import asyncio
from typing import Optional
from poller.tg_api import TgClient

from models import UpdateObj
from run_poller import TokenPoller

class Poller:
    def __init__(self, config: TokenPoller):
        #self.rmq_worker = WorkerRmq(config = WorkerConfig)
        self.tg_client = TgClient(config.token)
        self.is_running = True
        self._task: Optional[asyncio.Task] = None

    async def poll(self):
        
        offset = 0
        while self.is_running:
            updates = await self.tg_client.get_updates_in_objects(offset=offset, timeout=60)
            for update in updates:
                offset = update.update_id + 1
                data = UpdateObj.Schema().dump(update)
                await self.rmq_worker.put(data)

    async def start(self):
        
        self.is_running = True
        self._task = asyncio.create_task(self.poll())

    async def stop(self):

        self.is_running = False
        self._task.cancel()
        try:
            await self._task
        except asyncio.CancelledError:
            pass

        await self.rmq_worker.stop()        

