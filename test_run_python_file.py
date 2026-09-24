


from functions.run_python_file import run_python_file

def main():
    print("=== Test 1: main.py ===")
    print(run_python_file("calculator", "main.py"))
    
    print("\n=== Test 2: main.py with args ===")
    print(run_python_file("calculator", "main.py", ["3 + 5"]))
    
    print("\n=== Test 3: tests.py ===")
    print(run_python_file("calculator", "tests.py"))
    
    print("\n=== Test 4: outside working directory ===")
    print(run_python_file("calculator", "../main.py"))
    
    print("\n=== Test 5: nonexistent file ===")
    print(run_python_file("calculator", "nonexistent.py"))
    
    print("\n=== Test 6: non-python file ===")
    print(run_python_file("calculator", "lorem.txt"))

if __name__ == "__main__":
    main()