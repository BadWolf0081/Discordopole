from pogodata import PogoData

#from .boards import 
from .config import Config
from .maps import MapUrl, StaticMap
from .queries import Queries
from .templates import Templates
from .emotes import Emotes

from dp.utils.util import get_json_file
from discord.ext import commands

class DPfiles:
    def __init__(self, config):
        self.load_boards()
        self.geofences = get_json_file("config/geofence.json")
        #self.custom_emotes = get_json_file("config/emotes.json")

        if config.language not in ["de", "en", "es", "fr", "pl"]:
            config.language = "en"
        self.locale = get_json_file(f"dp/data/locale/{config.language}.json")
        if config.language not in ["de", "en", "es", "fr"]:
            config.language = "en"
        self.form_locale = get_json_file(f"dp/data/forms/{config.language}.json")

    def load_boards(self):
        self.boards = get_json_file("config/boards.json")

class DPvars:
    def __init__(self):
        self.config = Config("config/config.ini")
        self.bot = commands.Bot(command_prefix=self.config.prefix, case_insensitive=1)
        self.emotes = Emotes(self.bot, self.config)
        self.queries = Queries(self.config)
        self.map_url = MapUrl(self.config.map, self.config.map_url)
        self.static_map = StaticMap(self.config.tileserver_url, self.config.map_style)
        self.load_gamedata()

        self.files = DPfiles(self.config)

        self.templates = Templates(self, get_json_file("config/templates.json"))
    
    def load_gamedata(self):
        pogodata_locale = {
            "en": "english",
            "de": "german",
            "fr": "french",
            "es": "spanish"
        }
        self.pogodata = PogoData(pogodata_locale.get(self.config.language, "english"))

dp = DPvars()