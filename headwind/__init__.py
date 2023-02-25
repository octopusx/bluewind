#!/usr/bin/env python3

from bleak import BleakClient

ON = [0x4, 0x4, 0x2]
OFF = [0x2, 0x0]
SLEEP = [0x4, 0x1]
HR = [0x4, 0x2]
SPD = [0x4, 0x3]
MIN_SPEED = [0x2, 0x1]
HALF_SPEED = [0x2, 0x32]
FULL_SPEED = [0x2, 0x64]
CHARACTERISTIC = "a026e038-0a7d-4ab3-97fa-f1500f9feb8b"

class Headwind:
    fanClient = None
    def __init__(self, address):
        self.fanClient = BleakClient(address)

    async def sleep(self):
        async with self.fanClient as client:
            await client.write_gatt_char(CHARACTERISTIC, SLEEP)
    
    async def on(self):
        async with self.fanClient as client:
            await client.write_gatt_char(CHARACTERISTIC, ON)

    async def speedMode(self):
        async with self.fanClient as client:
            await client.write_gatt_char(CHARACTERISTIC, SPD)

    async def hrMode(self):
        async with self.fanClient as client:
            await client.write_gatt_char(CHARACTERISTIC, HR)

    async def manualSpeed(self, speed):
        if speed > 0:
            value = [0x2, hex(speed)]
            async with self.fanClient as client:
                await client.write_gatt_char(CHARACTERISTIC, value)

# async def main(address):
#     async with BleakClient(address) as client:
#         print(f"Connected: {client.is_connected}")

#         print("Turning Device on...")
#         # await client.write_gatt_char("a026e038-0a7d-4ab3-97fa-f1500f9feb8b", on)
#         await client.write_gatt_char("a026e038-0a7d-4ab3-97fa-f1500f9feb8b", SLEEP)
#         # await asyncio.sleep(1.0)

# if __name__ == "__main__":
#     asyncio.run(main(spec.address))