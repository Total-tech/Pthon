import time
from plyer import notification as n

if __name__ == "__main__":
    while True:
        n.notify(
            title="Please drink water",
            message="you need to drink water",
            # facades ="C:\\Users\\NITJ\\Desktop\\desktop\\python projects/water.png"
        )
        time.sleep(1600*3)