import time
from plyer import notification

def send_notification(title, message):
       notification.notify(
              title = title,
              message = message,
              timeout = 10 # notification stays for ten seconds
              )
if __name__ == '__main__':
       
       send_notification("Drink Water!", "It's time to drink water.")
       time.sleep(90*60) # after one and half hour the notificaion will popup again.

       send_notification("Take a berak from screen!",
              """look away from the screen and view an item at least 20 feet away for 20 seconds.
              This will help prevent eye soreness from excessive screen time.""")
       time.sleep(20*60) # after every twenty minutes the noification will popup again.

       while True:

              send_notification("Take a berak from screen!",
              """look away from the screen and view an item at least 20 feet away for 20 seconds.
              This will help prevent eye soreness from excessive screen time.""")
              time.sleep(70*60) # after every twenty minutes the noification will popup again.

              send_notification("Drink Water!",
              "It's time to drink water.")
              time.sleep(20*60) # after one and half hour the notificaion will popup again.

