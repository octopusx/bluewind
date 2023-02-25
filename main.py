#!/usr/bin/env python3
# import sys
import asyncio
import time
import spec

# from bleak import BleakClient
import headwind

on = [0x4, 0x4, 0x2]
off = [0x2, 0x0]
sleep = [0x4, 0x1]
hr = [0x4, 0x2]
spd = [0x4, 0x3]
speed = [0x2, 0x32]

# async def main(address):
#     async with BleakClient(address) as client:
#         print(f"Connected: {client.is_connected}")

#         print("Turning Device on...")
#         # await client.write_gatt_char("a026e038-0a7d-4ab3-97fa-f1500f9feb8b", on)
#         await client.write_gatt_char("a026e038-0a7d-4ab3-97fa-f1500f9feb8b", sleep)
#         # await asyncio.sleep(1.0)

async def main(address):
    fan = headwind.Headwind(address)
    print("turning fan on")
    await fan.on()
    print("wait 10 seconds")
    time.sleep(10)
    print("put fan to sleep")
    await fan.sleep()

if __name__ == "__main__":
    asyncio.run(main(spec.address))