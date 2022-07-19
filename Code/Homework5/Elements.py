ele1 = list("He Li Be Ne Mg Al Si Cl Ar Na".lower().split())
ele2 = list("H B C N O F P S".lower().split())

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        s = input().lower()
        for ele in ele1:
            s = s.replace(ele, "~")
        for ele in ele2:
            s = s.replace(ele, "~")
        s = s.replace("~", "")
        if len(s) == 0:
            print("Yes")
        else:
            print("No")
