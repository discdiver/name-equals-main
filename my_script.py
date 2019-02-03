# my_script
print(f"My __name__ is: {__name__}")

def i_am_main():
    print("I'm main!")

def i_am_imported():
    print("I'm iported!")

if __name__ == "__main__":
    i_am_main()
else:
    i_am_imported()
