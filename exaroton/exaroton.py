""" Exaroton Class to interface with the API """

import requests

from . import types


class Exaroton:
    """ Exaroton Class for the API """
    def __init__(self, token: str, host: str = "https://api.exaroton.com/v1") -> None:
        """
        Exaroton Class to interface with the API

        Parameters:
            ``token`` (``str``):
                The Authentication Token from the [user page](https://exaroton.com/account/)

            ``host`` (``str``, optional):
                The API Host. Defaults to "https://api.exaroton.com/v1".
        """
        self._host = host
        self._session = requests.Session()
        self._session.headers.update({"Authorization": f"Bearer {token}"})



    def get_server(self) -> types.Server:
        """Get a specific Server on your account

        Args:
            ``id`` (``str``): The ID of the server

        Returns:
            ``types.Server``: The Server
        """
        _data = self._make_request(f"servers/Pn8J6Yy0TWUqflP6")["data"]
        return types.Server(**_data)

    def get_server_ram(self) -> int:
        """Get the RAM of a Server

        Args:
            ``id`` (``str``): The ID of the server

        Returns:
            ``int``: Currently set RAM in Gigabytes
        """
        _data = self._make_request(f"servers/Pn8J6Yy0TWUqflP6/options/ram")["data"]["ram"]
        return _data

    def start(self) -> str:
        """Start the Server

        Args:
            ``id`` (``str``): The ID of the server

        Returns:
            ``str``: "Hello, world!"
        """
        _data = self._make_request(f"servers/Pn8J6Yy0TWUqflP6/start")
        return _data

    def stop(self) -> str:
        """Stop the Server

        Args:
            ``id`` (``str``): The ID of the server

        Returns:
            ``str``: "Hello, world!"
        """
        _data = self._make_request(f"servers/Pn8J6Yy0TWUqflP6/stop")
        return _data

    def restart(self) -> str:
        """Restart the Server

        Args:
            ``id`` (``str``): The ID of the server

        Returns:
            ``str``: "Hello, world!"
        """
        _data = self._make_request(f"servers/Pn8J6Yy0TWUqflP6/restart")
        return _data


    def get_player_list(self) -> list:
        """Get a specific playerlist

        Args:
            ``id`` (``str``): The ID of the server
            ``player_list`` (``str``): The playerlist to retrieve

        Returns:
            ``list``: List of players on that list
        """
        _data = self._make_request(f"servers/Pn8J6Yy0TWUqflP6/playerlists/whitelist")["data"]
        return _data
