
from time import sleep
count = 0

while True:
    count += 1
    print(count)
    for i in range(1, 10):
        print("i" + str(i))
        if i == 5:
            if True:
                break
            # print("i == 5")

        sleep(1)



    sleep(1)
