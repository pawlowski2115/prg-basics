# tv_show.py file
# main program
from tv import TV

def main():
   # object creation
   tv = TV()
   channels = ["TVP1", "TVP2", "Polsat", "TVN", "Filmbox", "Discovery"]
   tv.set_channels(channels)
   # object usage
   tv.show_status()
   tv.turn_on()
   tv.show_status()
   tv.show_channels()
   tv.set_channels(5)
   tv.show_status()
   tv.turn_off()
   tv.show_status()

if __name__ == "__main__":
   main() 