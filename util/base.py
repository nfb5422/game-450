from dndnetwork import DungeonMasterServer, PlayerClient


class DungeonMaster:
    def __init__(self):
        self.game_log = '' 
        self.server = DungeonMasterServer(self.game_log, self.dm_turn_hook)

    def start_server(self):
        self.server.start_server()

    def dm_turn_hook(self):
        dm_message = ''
        # Do DM things here. You can use self.game_log to access the game log

        # Return a message to send to the players for this turn
        return dm_message 


class Player:
    def __init__(self, name):
        self.name = name
        self.client = PlayerClient(self.name)

    def connect(self):
        self.client.connect()

    def unjoin(self):
        self.client.unjoin()

    def take_turn(self, message):
        self.client.send_message(message)
