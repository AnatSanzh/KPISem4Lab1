import logic
from enum import Enum


class _CUIStates(Enum):
    """Class that is used to track ConsoleInterface internal state"""
    ISLE: int = 1
    SHOW_RECORDS: int = 2


class ConsoleInterface:
    """Class that provides CUI that allows to interact with phone record list"""

    state = _CUIStates.ISLE
    state_data = {}

    def _update(self):
        """Main update function"""
        # todo: change comments
        pass

    def run(self):
        """Starts CUI"""
        pass
