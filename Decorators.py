def make_pretty(func):
    def inner():
        print("I am decorated")
        func()
    return inner

@make_pretty
def vanillacake():
    print("I am vanillacake")

@make_pretty
def blackcake():
    print("I am blackcake")

vanillacake()
blackcake()