

class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    def __init__(self, status: bool = False, muted: bool = False, 
                 volume: int = MIN_VOLUME, channel: int = MIN_CHANNEL) -> None:
        """
        Function initializing class.
        :param status: Boolean state for whether or not the television is on.
        :param muted: Boolean state for whether or not volume is on regardless of value of volume.
        :param volume: Integer state for what magnitude sound is on.
        :param channel: Determines what channel the television is turned to.
        """
        self.__status: bool = status
        self.__muted: bool = muted
        self.__volume: int = volume
        self.__channel: int = channel
        self.before_mute_volume: int = Television.MIN_VOLUME
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



