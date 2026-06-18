def get_starting_number():
    while True:
        try:
            n = int(input("How many bottles of beer on the wall? "))
            if n >= 1:
                return n
        except:
            pass

def sing(start):
    def bottle(n):
        return "bottle" if n == 1 else "bottles"
    i = start
    keep_singing = True
    while keep_singing:
        if i > 1:
            print(f"{i} {bottle(i)} of beer on the wall, {i} {bottle(i)} of beer. ")
            print(f"Take one down, pass it around, {i - 1} {bottle(i - 1)} of beer on the wall. ")
            print()
            i -= 1
        else:
            print(f"1 bottle of beer on the wall, 1 bottle of beer. ")
            print(f"Take it down, pass it around, no more bottles of beer on the wall! ")
            keep_singing = False

if __name__ == "__main__":
    sing(get_starting_number())
