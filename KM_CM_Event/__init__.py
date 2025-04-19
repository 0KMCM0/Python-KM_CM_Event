EventHandlerType = ...

class EventManager:
    def __init__( self ): self.__EVENTS__ = {}

    def Event( self, Event ):
        self.__EVENTS__.setdefault( Event, {} )
    def UnEvent( self, Event ):
        try: del self.__EVENTS__[ Event ]
        except: pass

    def Handle( self, Event, Function, Name = '__DEFAULT__' ):
        try: self.__EVENTS__[ Name ][ Event ] = Function
        except: pass
    def UnHandle( self, Event, Name = '__DEFAULT__' ):
        try: del self.__EVENTS__[ Event ][ Name ]
        except: pass

    def Call( self, Event, *Arguments, **KeyWordArguments ):
        for F in self.__EVENTS__[ Event ].values():
            F( *Arguments, **KeyWordArguments )