

class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self, status = False, muted = False, volume = MIN_VOLUME, channel = MIN_CHANNEL) -> None:
        self.__status = status
        self.__muted = muted
        self.__volume = volume
        self.__channel = channel
    def power(self):
        if not self.__status:
            self.__status = True
        else:
            self.__status = False
    def mute(self):
        if self.__status:
            if not self.__muted:
                self.__muted = True
                self.before_mute_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.before_mute_volume
    def channel_up(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            elif self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            elif self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
    def volume_up(self):
        if self.__status:
            if self.__volume < Television.MAX_VOLUME and not self.__muted:
                self.__volume += 1
            elif self.__muted:
                self.mute()
                self.__volume += 1

    def volume_down(self):
        if self.__status:
            if self.__volume > Television.MIN_VOLUME and not self.__muted:
                self.__volume -= 1
            elif self.__muted:
                self.mute()
                self.__volume -= 1
    def __str__(self):
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}."



