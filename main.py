def to_upper(name):
    return name.upper()

def greet(name):
    print(f"Hello {name}")

if __name__ == "__main__":
    name = "GAurav"
    res = to_upper(name)
    greet(name)
    greet(res)