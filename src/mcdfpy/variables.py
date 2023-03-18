
GAME = "unsaved"
SAVE = "save"
LOCAL = "local"

class VariableError(Exception):
    pass

class BaseVariable:
    id = ""
    defaultData = {}
    def __init__(self, **data):
        self.data = self.defaultData
        self.set(**data)
    def set(self, **data):
        acceptablekeys = self.defaultData.keys()
        for k in data:
            v = data[k]
            if k in acceptablekeys:
                if type(v) == str:
                    v = v.replace("&", "§")
                self.data[k] = v
            else:
                raise VariableError(f"Incompatible variable data. This variable type accepts any of the following arguments: {acceptablekeys}")
    def reset_data(self):
        self.data = self.defaultData
    def export(self, slot=0):
        return {
            "slot": slot,
            "item": {
                "id": self.id,
                "data": self.data
            }
        }

class Variable(BaseVariable):
    id = "var"
    defaultData = {
        "name": "variable",
        "scope": GAME
    }

class TextVariable(BaseVariable):
    id = "txt"
    defaultData = {
        "name": "text"
    }

class NumberVariable(BaseVariable):
    id = "num",
    defaultData = {
        "name": "0"
    }

class LocationVariable(BaseVariable):
    id = "loc",
    defaultData = {
        "x": 0,
        "y": 0,
        "z": 0,
        "pitch": 0.0,
        "yaw": 0.0
    }
    def export(self, slot=0):
        output = super().export(slot)
        data = output["item"]["data"]
        output["item"]["data"] = {
            "isBlock": False,
            "loc": data
        }

class VectorVariable(BaseVariable):
    id = "vec"
    defaultData = {
        "x": 0,
        "y": 0,
        "z": 0
    }

class SoundVariable(BaseVariable):
    id = "snd"
    defaultData = {
        "sound": "Creative Music",
        "pitch": 1.0,
        "vol": 2.0,
        "variant": "nuance1"
    }

class ParticleVariable(BaseVariable):
    id = "part"
    defaultData = {
        "particle": "Dust",
        "cluster": {
            "amount": 1,
            "horizontal": 0.0,
            "vertical": 0.0
        },
        "data": {
            "rgb": 16711680,
            "colorVariation": 0,
            "size": 1.0,
            "sizeVariation": 0
        }
    }

class PotionVariable(BaseVariable):
    id = "pot",
    defaultData = {
        "pot": "Instant Health",
        "dur": 1000000,
        "amp": 0
    }

class GameValueVariable(BaseVariable):
    id = "g_val"
    defaultData = {
        "type": "Location",
        "target": "Default"
    }