import copy

fruit = {"grape": 1, "cherry": 2, "orange": 3, "lemon": 4, "kiwifruit": 5, "tomato": 6,
         "peach": 7, "pineapple": 8, "coconut": 9, "watermelon": 10, "WATERMELON": 11}
fruit_r = {1: "grape ", 2: "cherry ", 3: "orange ", 4: "lemon ", 5: "kiwifruit ", 6: "tomato ",
           7: "peach ", 8: "pineapple ", 9: "coconut ", 10: "watermelon ", 11: "WATERMELON "}
if __name__ == "__main__":
    container = []
    result = []
    pointer = 0
    full = 0
    sure = 0
    size, line = map(int, input().split())
    for i in range(line):
        container.append(fruit.get(input()))
        pointer += 1
        while True:
            if (pointer >= 2) & (container[pointer - 1] == container[pointer - 2]):
                container.pop()
                container[pointer - 2] += 1
                pointer -= 1
            else:
                break
        if (len(container) > size) & (sure == 0):
            full = 1
            sure = 1
            result = copy.deepcopy(container)
        if (container.__contains__(11)) & (sure == 0):
            sure = 1
            result = copy.deepcopy(container)
    if full == 1:
        print("You lose!")
        result.pop()
        for item in result:
            print(fruit_r.get(item), end="")
    else:
        if container.__contains__(11):
            print("You win!")
            for item in result:
                print(fruit_r.get(item), end="")
        else:
            print("You lose!")
            for item in container:
                print(fruit_r.get(item), end="")
