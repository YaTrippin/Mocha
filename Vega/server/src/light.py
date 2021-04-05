from enum import Enum
import traceback
import model


class LightType(Enum):
    RGB = []
    RGBW = ["white_temperature"]
    S = ["colour"]
    RGBA = []
    RGBWA = []
    SA = []


# Individual LED Light
class Light():
    def __init__ (self, light_type: LightType, name: str, groups: list = []):
        pass
    
    def __init__ (self, config: dict):
        try:
            self.name = config['name']            
            self.light_type = config['type']
            self.net_id = config['network_id']
            self.hw_id = config['hw_id']
            
            self.groups = config['groups']
            self.opt_args = LightType[config['type']].value
            args = {list(arg.keys())[0]:arg[list(arg.keys())[0]] for arg in config['args']}
            
            for arg in self.opt_args:
                setattr(self, arg, args[arg] if arg in args else None)
        except ValueError:
            raise ValueError(f"Value Error: Can't create Light Object. YAML Key Error?")

    def get_groups(self):
        return self.groups

    def set_groups(self, groups):
        self.groups = groups
    
    def light_model(self):
        return model.Light(name=self.name, light_type=self.light_type, groups=self.groups, network_id=self.net_id)
        

# Group of LED Lights
class Group():
    def __init__(self, name, force_sync = False):
        self.name = name
        self.force_sync = force_sync 
        self.members = []

    def __init__(self, config: dict):
        try:
            self.name = config['name']
            self.force_sync = config['force_sync']
            self.members = []
        except ValueError:
            raise ValueError(f"Value Error: Can't create Group Object. YAML Key Error?")

    def add_member(self, light: Light):
        self.members.append(light)   # Light object is passed by reference, can be modified

    def get_members(self):
        return self.members

    def remove_member(self, light: Light):
        self.members.remove(light)

    def is_force_synced(self):
        return self.force_sync
