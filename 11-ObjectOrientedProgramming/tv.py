class TV:
    def __init__(self, new_channel_no):
      self.is_on = False
      self.new_channel_no = new_channel_no
    def turn_off(self):
      self.is_on = False
    def turn_on(self):
      self.is_on = True
      
    def show_status(self):
        if self.is_on:
            print(f'TV is on, channel {self.new_channel_no}')
        else:
            print("TV is off")



    
       