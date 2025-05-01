import time
from plyer import notification

while True :
    print("Please drink water!")
    notification.notify(title="please drink some water",
                             message = "you need to drink water",)
    time.sleep(60*60) 