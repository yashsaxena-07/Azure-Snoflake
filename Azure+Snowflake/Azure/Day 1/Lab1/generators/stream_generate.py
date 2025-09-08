import time, random
from datetime import datetime

customers = ["Alice","Bob","Charlie","David","Emma","Frank","Grace","Hannah","Ivy","Jack","Zara"]
order_id = 101

with open("stream_orders.txt", "a") as f:
    while True:
        ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cust = random.choice(customers)
        amt = random.randint(50, 500)
        line = f"{order_id},{ts},{cust},{amt}\n"
        f.write(line)
        f.flush()
        print("New order:", line.strip())
        order_id += 1
        time.sleep(5)