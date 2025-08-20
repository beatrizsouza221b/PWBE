import time

while True:
    hora =  time.strftime("%H:%M:%S:")
    print(f"Agora são: {hora}")
    time.sleep(10)

    time.strftime