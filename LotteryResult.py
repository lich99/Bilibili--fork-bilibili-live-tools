from statistics import Statistics
import asyncio
import random

class LotteryResult():

    async def query(self):
        while 1:
            await Statistics().clean_TV()

            await asyncio.sleep(30 + random.uniform(0,4))
