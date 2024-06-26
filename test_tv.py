#Ralph Cyrel B. Ronda
#BSCPE 1-2
#Television (class)

class TV:
#constructor
    def __init__(self):
        self.channel = 1
        self.volume_level = 1
        self.on = False
#creating a method for turn on and off
    def turn_on(self):
        self.on = True
    def turn_off(self):
        self.on = False
#creating a method for volume
    def get_volume(self):
        return self.volume_level
#creating a method for volume (1-7 limit)
    def set_volume(self, volume_level):
        if 1 <= volume_level <= 7:
            self.volume_level = volume_level
#creating a method for increasing the volume
    def volume_up(self):
        if self.on and self.volume_level < 7:
            self.volume_level += 1
#creating a method for decreasing the volume
    def volume_down(self):
        if self.on and self.volume_level > 1:
            self.volume_level -= 1
#creating a method for channel
    def get_channel(self):
        return self.channel
#creating a method for channel (1-120 limit)
    def set_channel(self, channel_level):
        if 1 <= channel_level <= 120:
            self.channel = channel_level
#creating a method for increasing the channel
    def channel_up(self):
        if self.on and self.channel < 120:
            self.channel += 1
#creating a method for decreasing the channel
    def channel_down(self):
        if self.on and self.channel > 1:
            self.channel -= 1