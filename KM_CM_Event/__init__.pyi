from typing import Callable as _Callable, Any as _Any

EventHandlerType = _Callable[ ..., None ]
"""Functions that are used to handle events."""

class EventManager:
    """
Handles events. Normally, you should have one global instance of this class named ``G_Event``.
    """
    def __init__( self ) -> None:
        self.__EVENTS__: dict[ str, dict[ str, EventHandlerType ] ] = ...
        """All existing events."""

    def Event( self, Event: str ) -> None:
        """
Adds ``Event``.
        """
    def UnEvent( self, Event: str ) -> None:
        """
Deletes ``Event``.
        """

    def Handle( self, Event: str, Function: EventHandlerType, Name: str = ... ) -> None:
        """
Adds a Handle for ``Event``.
        """
    def UnHandle( self, Event: str, Name: str = ... ):
        """
Deletes a Handle for ``Event``.
        """

    def Call( self, Event: str, *Arguments: _Any, **KeyWordArguments: _Any ) -> None:
        """
Calls an ``Event``.
        """