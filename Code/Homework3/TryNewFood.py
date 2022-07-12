if __name__ == "__main__":
    food = str(input())
    food_list = food.split()
    food_set = set(food_list)
    food_list = list(food_set)
    food_list.sort()
    for item in food_list:
        print(item, end=" ")
