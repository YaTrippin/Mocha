from fastapi import FastAPI
import yaml
import aiofiles
import pathlib
import uvicorn
from light import Light, Group
from model import Lights
import json
import logging

import model


# PATH CONSTANTS
CWD = pathlib.Path(__file__).resolve().parent
YAML_CONFIG_FILE = CWD.parent / "config.yml"


# DEVICES
groups = []
lights = []

app = FastAPI()
logger = logging.getLogger("app")


@app.on_event("startup")
async def startup():
    # Parse yml config file
    config = {}
    async with aiofiles.open(YAML_CONFIG_FILE, "r") as conf_file:
        data = await conf_file.read()
        config = yaml.load(data)

    # Create empty groups
    for group_data in config['groups']:        
        groups.append(Group(group_data))

    # Add each LED configuration to the light array
    for light_data in config['lights']:
        light = Light(light_data)
        light_groups = light.get_groups()
        lights.append(light) 

        # Add the LED to their respective groups (by reference)
        force_synced = False    # If the LED is in a group that is forced synchronized
        for group in light_groups:
            if force_synced and group.is_force_synced: # Prevent light from being force-synced with multiple groups
                group.add_member(light)
    
    
    # Check if nRF24l01 API is online
    pass


@app.get("/get_lights")
async def get_led_data():
    lights_model_list = []
    

    for light in lights:
        lights_model_list.append(light.light_model().dict())
        
    return model.Lights(lights=lights_model_list)


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, log_level=logging.DEBUG)

