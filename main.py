def main():
    print("file reading started")

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
    print("file reading finished")
    print(file_contents)







main()