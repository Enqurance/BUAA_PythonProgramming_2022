dic_checksum = {1: 7, 2: 9, 3: 10, 4: 5, 5: 8, 6: 4, 7: 2,
                8: 1, 9: 6, 10: 3, 11: 7, 12: 9, 13: 10,
                14: 5, 15: 8, 16: 4, 17: 2}
dic_reminder = {0: 1, 1: 0, 2: "X", 3: 9, 4: 8, 5: 7, 6: 6,
                7: 5, 8: 4, 9: 3, 10: 2}


def is_adult(target_date, cur_day):
    tar_year = int(target_date[0])
    tar_month = int(target_date[1])
    tar_day = int(target_date[2])
    cur_year = int(cur_day[0:4])
    cur_month = int(cur_day[4:6])
    cur_day = int(cur_day[6:8])
    if tar_year - cur_year > 18:
        return True
    elif tar_year - cur_year == 18:
        if tar_month > cur_month:
            return True
        elif tar_month == cur_month:
            if tar_day >= cur_day:
                return True
    return False


if __name__ == "__main__":
    adult = 0
    invalid = 0
    n = int(input())
    time = input().split()
    for i in range(n):
        identity_id = input()
        checksum = 0
        cnt = 1
        for num in identity_id[:17]:
            checksum += dic_checksum.get(cnt) * int(num)
            cnt += 1
        reminder = dic_reminder.get(checksum % 11)
        if str(reminder) != identity_id[17]:
            invalid += 1
        if is_adult(time, identity_id[6:14]):
            adult += 1
    print(str(adult) + " " + str(invalid))
