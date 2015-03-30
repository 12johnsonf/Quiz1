import time
def congrats(score):
    print("Score: ", score)
    if score > 6:
        for i in range(5):
            print("Well done")
            time.sleep(0.5)
