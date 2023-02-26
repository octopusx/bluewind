#!/usr/bin/env python3
from flask import Flask
from headwind import Headwind as Headwind

app = Flask(__name__)
app.config.from_prefixed_env()

@app.route("/on")
async def on():
    fan = Headwind(app.config["ADDRESS"])
    await fan.on()
    return "<p>Turning headwind on</p>"

@app.route("/sleep")
async def sleep():
    fan = Headwind(app.config["ADDRESS"])
    await fan.sleep()
    return "<p>Putting headwind to sleep</p>"

@app.route("/speed/<int:speed>")
async def speed(speed):
    fan = Headwind(app.config["ADDRESS"])
    await fan.manualSpeed(speed)
    return f"<p>Setting headwind speed to {speed}</p>"
