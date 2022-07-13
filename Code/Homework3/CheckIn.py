if __name__ == "__main__":
    n = int(input())
    check_list = {}
    for i in range(n):
        instr = str(input()).split()
        if instr[0] == "1":
            temp = {instr[1]: instr[2]}
            check_list.update(temp)
        elif instr[0] == "2":
            if check_list.get(instr[1]):
                print(check_list.get(instr[1]))
            else:
                print(9999)
        elif instr[0] == "3":
            cnt = 0
            for key in check_list.keys():
                if int(check_list.get(key)) <= int(instr[2]):
                    cnt += 1
            print(cnt)
