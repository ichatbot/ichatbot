import typing
import threading
from abc import ABCMeta, abstractmethod


class IChatbot(metaclass=ABCMeta):

    def __init__(self, options: typing.Dict):
        self._logging = False
        self._running = False
        self._options = options

    def on(self, event: str, callback: typing.Callable):
        return self

    def _login(self):
        if self._logging or self._running:
            return

        self._logging = True

        uuid = None
        while self._logging:
            if uuid is None:
                uuid = self._get_qrcode_uuid()
            # TODO print uuid
            status = self._check_login(uuid)

            if status:
                break

        self._logging = False

    @abstractmethod
    def _check_login(self, uuid: str) -> bool:
        pass

    @abstractmethod
    def _get_qrcode_uuid(self):
        pass

    @abstractmethod
    def _receive_message(self):
        pass

    def start(self, block=True):
        self.login()

        def main_loop():
            # TODO -> heart
            self._running = True
            while self._running:
                try:
                    pass
                except KeyboardInterrupt:
                    break

            self._running = False

        if block:
            main_loop()
        else:
            thread = threading.Thread(target=main_loop)
            thread.setDaemon(True)
            thread.start()
