import json
from .blocks import BaseBlock
from .variables import BaseVariable

class ImportedBlock(BaseBlock):
    pass

class ImportedBracket(BaseBlock):
    def __init__(self, side):
        self.side = side
    def export(self):
        return [{
            "id": "bracket",
            "type": "norm",
            "direct": self.side
        }]

class ImportedVariable(BaseVariable):
    def __init__(self, type, data):
        self.id = type
        self.data = data
        self.defaultData = data

class Template:
    def __init__(self, name="Unnamed Template", author=None, version=None):
        self.name = name
        self.author = author
        self.version = None
        self.blocks = []
    def add_block(self, block:BaseBlock):
        self.blocks.append(block)
    def remove_block(self, id:int):
        self.blocks.pop(id)
    def export(self):
        eblocks = []
        for block in self.blocks:
            eblock = block.export()
            for eb in eblock:
                eblocks.append(eb)
        template = json.dumps({"blocks": eblocks})
        return template, self.name, self.author, self.version
    @classmethod
    def from_raw(cls, data):
        template = cls()
        #print(data)
        blocks = data["blocks"]
        for block in blocks:
            if block["id"] == "block":
                variables = []
                for variable in block["args"]["items"]:
                    ivariable = ImportedVariable(variable["item"]["id"],
                                                 variable["item"]["data"])
                    variables.append(ivariable)
                iblock = ImportedBlock(*variables)
                iblock.blockAction = block["action"]
                iblock.blockType = block["block"]
            elif block["id"] == "bracket":
                iblock = ImportedBracket(block["direct"])
            template.add_block(iblock)
        return template