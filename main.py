import time
from plyer import notification

if __name__ == "__main__":
    notification.notify(
        title = "Please Drink Water",
        message = "Drinking water is very important and crucial for a human's health!",
        timeout = 3
    )