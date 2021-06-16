# Task 2

# Create a simple prototype of a TV controller in Python. It’ll use the following commands

# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes"
# if the channel N or 'name' exists in the list, or "No" - in the other case.


CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    current_ch = 0

    def __init__(self, input_channels):
        self.channels = input_channels

    def first_channel(self):
        return self.channels[0]

    def last_channel(self):
        return self.channels[-1]

    def turn_channel(self, n):
        try:
            self.current_ch = n - 1
            return self.current_channel()
        except IndexError:
            return "Channel doesn't exist"

    def next_channel(self):
        self.current_ch += 1
        if self.current_ch >= len(self.channels):
            self.current_ch = 0
        return self.current_channel()

    def previous_channel(self):
        self.current_ch -= 1
        if self.current_ch < 0:
            self.current_ch = len(self.channels) - 1
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_ch]

    def is_exist(self, n):
        if isinstance(n, int):
            if 0 <= n < len(self.channels):
                return "YES"
            else:
                return "NO"
        else:
            if n in self.channels:
                return "YES"
            else:
                return "NO"


controller = TVController(CHANNELS)


print(controller.first_channel())

print(controller.last_channel())

print(controller.turn_channel(1))

print(controller.next_channel())

print(controller.previous_channel())

print(controller.current_channel())

print(controller.is_exist("BBC"))
print(controller.is_exist(4))


