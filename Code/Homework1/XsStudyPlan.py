if __name__ == "__main__":
    hour, minute = map(int, input().split())
    time_len = int(input())
    hour += (time_len + minute) // 60
    minute = (time_len + minute) % 60
    if (hour >= 23) & (minute >= 30):
        print("23:30")
    else:
        print("%02d:%02d" % (hour, minute))
