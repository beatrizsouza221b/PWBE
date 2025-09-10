import typing
import types
import asyncio

types.CoroutineType = typing.Coroutine
from robocode_tank_royale.bot_api import Bot, BotInfo, events, Color

class Bia(Bot):
    def __init__(self):
        super().__init__(BotInfo(name = "Bia", version = "1.0", authors = ["Dorival"]))

        self.body_color = Color(255, 0, 0)
        self.scan_color = Color(147, 112, 219)
        self.radar_color = Color(139, 0, 0)
        self.turret_color = Color(139, 0, 0)

    async def run(self):
        while self.is_running():
            await self.forward(100)
            await self.fire(2)
            await self.back(100)
            await self.turn_gun_left(360)
            await self.turn_left(-360)

    async def on_scanned_bot(self, event: events.ScannedBotEvent):
        await self.fire(3)

    async def on_hit_wall(self, event: events.HitWallEvent):
        await self.back(200)

if __name__ == "__main__":
    asyncio.run(Bia().start())