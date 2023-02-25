#!/usr/bin/env python3
import asyncio
import click
from config import Configurinator as Config
from headwind import Headwind as Headwind

@click.command()
@click.option('--address', default=None, help='headwind mac address')
@click.option('--cmd', default=None, help='command to send')
@click.option('--speed', default=1, help='manual speed value, 1 to 100')
def main(address, cmd, speed):
    conf = Config()
    conf.load_config(address, cmd, speed)
    asyncio.run(bluewind(conf))

async def bluewind(conf):
    fan = Headwind(conf.address)
    match conf.cmd:
        case 'on':
            print("turning fan on")
            await fan.on()
        case 'sleep':
            print("putting fan to sleep")
            await fan.sleep()
        case 'manual':
            print("seetting fan speed")
            await fan.speed(conf.speed)
    print('stuff')


if __name__ == "__main__":
    main()