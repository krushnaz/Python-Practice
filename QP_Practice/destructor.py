class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} object created.")

    def __del__(self):
        print(f"{self.name} object destroyed.")

def main():
    # Create an object of MyClass
    obj = MyClass("obj")
    
    # Delete the object explicitly
    # del obj

    # Create another object of MyClass
    obj2 = MyClass("obj2")

    # Exit the program
    print("Exiting the program.")

if __name__ == "__main__":
    main()
