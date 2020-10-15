def test_something_that_involves_user_input(monkeypatch):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr('builtins.input', lambda _: "Mark")

    # go about using input() like you normally would:
    i = input("What is your name?")
    assert i == "Mark"
    
def add(a, b):
    if a > 0 and b > 0:
        x=input()
        print(x)
        return a + b
    else:
        return None

def add_with_exception(a, b):
    if a > 0 and b > 0:
        return a + b
    else:
        raise ValueError
