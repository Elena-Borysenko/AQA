def display_box(width: int, height: int, character="*"):

    if width < 2 or height < 2:
        print("The height and width should be more than 1.")
        return

    print(character * width)

    for _ in range(height - 2):
        print(character + " " * (width - 2) + character)

    if height > 1:
        print(character * width)


display_box(15, 7, "x")









