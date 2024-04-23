def parse_input(input_string):
    cursor = 0

    def E():
        nonlocal cursor
        print(f"{'':<16}E -> T E'")
        if T():
            if Edash():
                return True
            else:
                return False
        else:
            return False

    def Edash():
        nonlocal cursor
        if cursor < len(input_string) and input_string[cursor] == '|':
            print(f"{'':<16}E' -> | T E'")
            cursor += 1
            if T():
                if Edash():
                    return True
                else:
                    return False
            else:
                return False
        else:
            print(f"{'':<16}E' -> $")
            return True

    def T():
        nonlocal cursor
        print(f"{'':<16}T -> F T'")
        if F():
            if Tdash():
                return True
            else:
                return False
        else:
            return False

    def Tdash():
        nonlocal cursor
        if cursor < len(input_string) and input_string[cursor] == '&':
            print(f"{'':<16}T' -> & F T'")
            cursor += 1
            if F():
                if Tdash():
                    return True
                else:
                    return False
            else:
                return False
        else:
            print(f"{'':<16}T' -> $")
            return True

    def F():
        nonlocal cursor
        if cursor < len(input_string) and input_string[cursor] == '(':
            print(f"{'':<16}F -> ( E )")
            cursor += 1
            if E():
                if cursor < len(input_string) and input_string[cursor] == ')':
                    cursor += 1
                    return True
                else:
                    return False
            else:
                return False
        elif cursor < len(input_string) and input_string[cursor] == 'a':
            print(f"{'':<16}F -> a")
            cursor += 1
            return True
        else:
            return False

    if E() and cursor == len(input_string):
        print("--------------------------------")
        print("String is successfully parsed")
        return True
    else:
        print("--------------------------------")
        print("Error in parsing String")
        return False


# Main function
def main():
    print("Enter the string:")
    input_string = input().strip()
    print("\nInput          Action")
    print("--------------------------------")
    if parse_input(input_string):
        return 0
    else:
        return 1


if __name__ == "__main__":
    exit_code = main()
    exit(exit_code)


"""Enter the string:
a&(a|a)

Input          Action
--------------------------------
                E -> T E'
                T -> F T'
                F -> a
                T' -> &
                T' -> $
                E' -> |
                E' -> T E'
                T -> F T'
                F -> a
                T' -> $
                E' -> |
                E' -> T E'
                T -> F T'
                F -> a
                T' -> $
                E' -> $
--------------------------------
String is successfully parsed"""