class TestFather:
    def __init__(self):
        self.attr = 100

    def do(self):
        print("choose AC!")


class TestChild(TestFather):
    def do(self):
        print("choose BD!")


test = TestChild()
test.do()
print(test.attr)
