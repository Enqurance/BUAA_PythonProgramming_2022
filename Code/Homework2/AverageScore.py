if __name__ == "__main__":
    n = int(input())
    total_Chinese = 0
    total_Math = 0
    total_English = 0
    for i in range(n * 3):
        score, subject = input().split()
        if subject == "Chinese":
            total_Chinese += float(score)
        elif subject == "English":
            total_English += float(score)
        elif subject == "Math":
            total_Math += float(score)
    print("%.2f\n%.2f\n%.2f\n" %
          (total_Chinese / n, total_Math / n, total_English / n))
