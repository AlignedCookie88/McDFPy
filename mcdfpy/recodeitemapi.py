import socket
import json
import base64
import gzip
from .template import Template

class RecodeItemAPIError(Exception):
    pass

class RecodeItemAPI:
    def __init__(self, address="localhost", port=31372):
        self.address = address
        self.port = port
    def init_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.address, self.port))
    def send(self, data) -> bytes:
        self.init_socket()
        self.sock.send(data)
        data = self.sock.recv(2048)
        self.sock.close()
        return data
    def send_item(self, type: str, data: str, name:str = "Recode Item API Python Interface Item"):
        tosend = {"type": type, "data": data, "source": name}
        tosendjson = json.dumps(tosend)+"\n"
        tosendbytes = bytes(tosendjson, "utf-8")
        rawout = self.send(tosendbytes)
        jsonout = rawout.decode("utf-8")
        out = json.loads(jsonout)
        if out["status"] == "error":
            raise RecodeItemAPIError(out["error"])
    def send_nbt(self, data:str, name:str = "NBT Item"):
        self.send_item("nbt", data, name)
    def send_template(self, data:Template):
        jsondata, name, author, version = data.export()
        name = name.replace("&", "§")
        templatedata = {"data": jsondata, "name": name}
        if author:
            templatedata["author"] = author
        if version:
            templatedata["version"] = version
        templatejson = json.dumps(templatedata)
        self.send_item("raw_template", templatejson, "§6Template §7- §r"+name)
    def receive_template(self) -> Template:
        self.init_socket()
        rawtemplate = self.sock.recv(20480)
        self.sock.send(b"{\"success\":\"\"}")
        self.sock.close()
        templatetext = rawtemplate.decode("utf-8", "ignore")
        templatedict = json.loads(templatetext)
        if templatedict["type"]=="template":
            templatedata = json.loads(templatedict["received"])
            templatecoderaw = templatedata["code"]
            templatecodecompressed = base64.b64decode(templatecoderaw)
            templatecodestr = gzip.decompress(templatecodecompressed)
            templatecode = json.loads(templatecodestr)
            template = Template.from_raw(templatecode)
            return template
        else:
            raise RecodeItemAPIError("Received \""+templatedict["type"]+"\", expected a \"template\".")