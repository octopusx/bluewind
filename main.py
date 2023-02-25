#!/usr/bin/env python3
import asyncio
import click
import time
import headwind.spec as spec
from headwind import Headwind as Headwind


@click.command()
@click.option('--address', default=None, help='headwind mac address')
@click.option('--cmd', default=None, help='command to send')
@click.option('--speed', default=1, help='manual speed value, 1 to 100')
async def main(address, cmd, speed):
    fan = Headwind(address)
    match cmd:
        case 'on':
            print("turning fan on")
            await fan.on()
        case 'sleep':
            print("putting fan to sleep")
            await fan.sleep()
        case 'manual':
            print("seetting fan speed")
            await fan.speed(speed)

#TODO: fix the async error with Click, or replace with another cli lib
if __name__ == "__main__":
    asyncio.run(main())