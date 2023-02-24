#!/usr/bin/env python3
import sys
import asyncio
import platform
import spec

from bleak import BleakClient

# async def main(address: str):
#     async with BleakClient(address) as client:
#         print("Services:")
#         for service in client.services:
#             print(service)

on = [0x4, 0x4, 0x2]
off = [0x2, 0x0]
sleep = [0x4, 0x1]
hr = [0x4, 0x2]
spd = [0x4, 0x3]
speed = [0x2, 0x32]

async def main(address):
    async with BleakClient(address) as client:
        print(f"Connected: {client.is_connected}")

        print("Turning Device on...")
        # await client.write_gatt_char("a026e038-0a7d-4ab3-97fa-f1500f9feb8b", on)
        await client.write_gatt_char("a026e038-0a7d-4ab3-97fa-f1500f9feb8b", sleep)
        # await asyncio.sleep(1.0)

if __name__ == "__main__":
    asyncio.run(main(spec.address))