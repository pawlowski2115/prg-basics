# tv_show.py file
# main program
from tv import TV

def main():
   # object creation
   tv = TV(5)

   # object usage
   tv.show_status()
   tv.turn_on()
   tv.show_status()
   tv.turn_off()
   tv.show_status()

if __name__ == "__main__":
   main() 