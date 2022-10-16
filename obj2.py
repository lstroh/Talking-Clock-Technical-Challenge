import HumanFriendlyTime
import sys
if __name__ == '__main__':
    obj = HumanFriendlyTime.HumanFriendlyTime()
    n = len(sys.argv)
    if n == 1:
        print(obj.get_human_friendly_time_now())
    elif n == 2:
        print(obj.get_human_friendly_time_string(sys.argv[1]))
    else:
        print("obj2 usage:")
        print("obj2 without any args : get current HumanFriendlyTime text")
        print("obj2 with Numeric Time : get the HumanFriendlyTime text. Example obj2 15:10")