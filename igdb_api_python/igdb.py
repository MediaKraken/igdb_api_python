# IGDB PYTHON WRAPPER

import json

import requests


class igdb:
    __api_key = ""
    __args = ""
    __api_url = "https://api-2445582011268.apicast.io/"

    def __init__(self, api_key):
        self.__api_key = api_key

    # CREATE URL FROM PARAMETERS
    def joinParameters(self, parameter="", types="", default="", prefix=""):
        if parameter in self.__args:
            default = str(prefix)
            if type(self.__args[parameter]) != types:
                default += ",".join(map(str, self.__args[parameter]))
            else:
                default += str(self.__args[parameter])
        return default

    def getRequest(self, url):
        headers = {
            'user-key': self.__api_key,
            'Accept': 'application/json'
        }
        r = requests.get(self.__api_url + url, headers=headers)
        r.body = json.loads(r.text)
        return r

    # CALL TO THE API
    def call_api(self, endpoint, args):
        ids = order = filters = expand = limit = offset = search = scroll = ""
        fields = "*"
        self.__args = args

        # If dict, convert it to komma seperated string
        if type(args) != int:
            ids = self.joinParameters(parameter='ids', types=int)
            fields = self.joinParameters(parameter='fields', types=str, default="*")
            expand = self.joinParameters(parameter='expand', types=str, prefix="&expand=")
            limit = self.joinParameters(parameter='limit', types=int, prefix="&limit=")
            offset = self.joinParameters(parameter='offset', types=int, prefix="&offset=")
            order = self.joinParameters(parameter='order', types=str, prefix="&order=")
            search = self.joinParameters(parameter='search', types=str, prefix="?search=")
            scroll = self.joinParameters(parameter='scroll', types=int, prefix="&scroll=")

            if 'filters' in args:
                for key, value in args['filters'].items():
                    filters += "&filter" + key + "=" + str(value)
        else:
            ids = args

        # Build URL
        url = endpoint + "/" + str(search) + str(ids)
        url += "&" if search != "" else "?"
        url += "fields=" + str(fields) + str(filters) + str(order) + str(limit) + str(offset) \
               + str(expand) + str(scroll)
        r = self.getRequest(url)
        return r

    # Get next scroll page
    def scroll(self, response):
        return self.getRequest(response.headers['x-next-page'])

    # GAMES
    def games(self, args=""):
        return self.call_api("games", args)

    # PULSE
    def pulses(self, args=""):
        return self.call_api("pulses", args)

    # CHARACTERS
    def characters(self, args=""):
        return self.call_api("characters", args=args)

    # COLLECTIONS
    def collections(self, args=""):
        return self.call_api("collections", args=args)

    # COMPANIES
    def companies(self, args=""):
        return self.call_api("companies", args=args)

    # FRANCHISES
    def franchises(self, args=""):
        return self.call_api("franchises", args=args)

    # FEEDS
    def feeds(self, args=""):
        return self.call_api("feeds", args=args)

    # PAGES
    def pages(self, args=""):
        return self.call_api("pages", args=args)

    # GAME_ENGINES
    def game_engines(self, args=""):
        return self.call_api("game_engines", args=args)

    # GAME_MODES
    def game_modes(self, args=""):
        return self.call_api("game_modes", args=args)

    # GENRES
    def genres(self, args=""):
        return self.call_api("genres", args=args)

    # KEYWORDS
    def keywords(self, args=""):
        return self.call_api("keywords", args=args)

    # PEOPLE
    def people(self, args=""):
        return self.call_api("people", args=args)

    # PLATFORMS
    def platforms(self, args=""):
        return self.call_api("platforms", args=args)

    # PLAYER_PERSPECTIVES
    def player_perspectives(self, args=""):
        return self.call_api("player_perspectives", args=args)

    # RELEASE_DATES
    def release_dates(self, args=""):
        return self.call_api("release_dates", args=args)

    # PULSE GROUPS
    def pulse_groups(self, args=""):
        return self.call_api("pulse_groups", args=args)

    # PULSE SOURCES
    def pulse_sources(self, args=""):
        return self.call_api("pulse_sources", args=args)

    # THEMES
    def themes(self, args=""):
        return self.call_api("themes", args=args)

    # REVIEWS
    def reviews(self, args=""):
        return self.call_api("reviews", args=args)

    # TITLES
    def titles(self, args=""):
        return self.call_api("titles", args=args)

    # TITLES
    def credits(self, args=""):
        return self.call_api("credits", args=args)
