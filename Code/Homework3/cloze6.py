class A:
    def P(self):
        print("Bonjour")


class B:
    def P(self):
        print("Bonjour")


class C(A, B):
    def P(self):
        print("Bonjour")
