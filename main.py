
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    match i:= input("Enter 1 for document cloning, 2 for game character creation, 3 for object pooling: "):
        case "1":
            import document_cloning
        case "2":
            import game_character_creation
        case "3":
            import object_pooling
        case _:
            print("Invalid Input")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
