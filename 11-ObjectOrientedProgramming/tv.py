class TV:
    def __init__(self):
      self.is_on = False
      self.new_channel_no = 1
      self.channels = []

    def turn_off(self):
      self.is_on = False

    def turn_on(self):
      self.is_on = True

    def set_channels(self, channels_list):
       self.channels = channels_list
    
    def show_channels(self):
       print("Channel list:")
       for index, channel in enumerate(self.channels, start=1):
          print(f'{index}. {channel}')
      
    def show_status(self):
        if self.is_on:
            channel_name = self.channels[self.new_channel_no - 1]
            print(f'TV is on, channel {self.new_channel_no} ({channel_name})')
        else:
            print("TV is off")



    
       