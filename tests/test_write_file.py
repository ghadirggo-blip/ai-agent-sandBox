from functions.write_file import write_file

def main():

    print(write_file("calculator", "lorem.txt", "1234567890123456789012345678"))
    
    
    print(write_file("calculator", "pkg/morelorem.txt", "12345678901234567890123456"))
    
    print(write_file("calculator", "../outside.txt", "error test"))

if __name__ == "__main__":
    main()