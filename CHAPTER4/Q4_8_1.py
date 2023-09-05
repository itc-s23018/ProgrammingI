def show_begin_end(func):
    def deco_func(*args, **kwargs):
        print("== start")
        result = func(*args, **kwargs)
        print("== end")
        return result

    return deco_func
import time


@show_begin_end
def sleep_for_a_while():
    print("Sleeping..")
    time.sleep(2)
    print("Done Sleeping")

print(sleep_for_a_while())
