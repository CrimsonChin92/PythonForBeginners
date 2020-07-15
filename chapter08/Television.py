# Chapter 8 challenge 2
# Write a program that simulates a television by creating it as an object. The
# user should be able to enter a channel number and raise or lower the volume.
# Make sure the channel number and volume stay within valid ranges.

class Television(object):
    """A television object"""

    def __init__(self, channel = 0, volume = 0):
        self.channel = channel
        self.volume = channel

    def talk(self):
        print("You are currently watching channel",self.channel,
              "at volume level", self.volume)

    def changeChannel(self, channel_req, num_channels = 5):
        if 0 <= channel_req <= num_channels:
            self.channel = channel_req
            print("Changing channel to", end=" ")
        else:
            print("\aChannel not found. Staying on", end=" ")
        # call private method to get channel name
        print(self.channelName)

    def changeVolume(self, vol_dir, max_volume = 10):
        if vol_dir == "UP":
            if self.volume == max_volume:
                print("\aMax. volume level reached")
            else:
                self.volume += 1
                print("Volume", self.volume)
        elif vol_dir == "DOWN":
            if self.volume == 0:
                print("\aMin. volume level reached")
            else:
                self.volume -= 1
                print("Volume", self.volume)

    @property
    def channelName(self):
        """Define a list of channels with a string representing each channel number"""
        channel_list = ("Neutral",
                        "BBC1",
                        "BBC2",
                        "ITV",
                        "Channel 4",
                        "Channel 5")
        channel_name = channel_list[self.channel]
        return channel_name
    
def instructions():
    """Provide instructions on how to use the controller to interact with the television"""
    print(
        """
            TURNING ON TELEVISION

            Use your keypad to interact with the television:
            1. Enter a number to change change
            2. Enter "up" or "down" to adjust volume
            3. Enter "off" to turn on television

        """)
    
def main():
    """Main body handles the user input request and determines what action to take next"""
    # create object
    tv = Television()

    # handle user input
    user_req = None
    while user_req != "OFF":
        # prompt user to change channel/volume or turn off television
        user_req = input("\nCommand: ").upper()
        print("") # add blank line

        if user_req == "OFF":
            print("Turning off Television")
            
        elif user_req == "UP" or user_req == "DOWN":
            tv.changeVolume(vol_dir = user_req)
            
        elif user_req == "":
            tv.talk()

        else:
            try:
                channel_req = int(user_req)
                tv.changeChannel(channel_req = channel_req)
            except ValueError:
                print("\aInvalid request",
                      "\nPlease enter 'up' or 'down' to change volume",
                      "\nEnter a numerical figure to change channel",
                      "\nOr 'off' to turn off television")

    # create list of channels
##    channel_list = ('Neutral',
##                    'BBC1',
##                    'BBC2',
##                    'ITV',
##                    'Channel 4',
##                    'Channel 5')

# run program
instructions()
main()
