import time
from win10toast import ToastNotifier

while True:
    notifier = ToastNotifier()
    notifier.show_toast("Drink Water!","It's been 2 hours. Time to drink a glass of water.",
                        duration = 5,
                        icon_path="python-problems\water_reminder\water_drop.ico")
    time.sleep(30) #adjust according to preference 
