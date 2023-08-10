# context manager, properly disposes of vars and opens / closes as needed
# with open("notes.txt","w") as file:
#     file.write("some text...")

from contextlib import contextmanager

# function based context manager, uses generator logic
@contextmanager
def open_managed_file(filename,mode):
    if mode not in ('w', 'r', 'a', 'x'):
        raise ValueError("Invalid file mode, please use 'r','w','a','x'")

    file = open(filename,mode)

    try:
        yield file
    except Exception:
        print("handled exception")
    finally:
        file.close()

# custom context manager - class based
class ManagedFile:
    def __init__(self,filename,mode):
        self.filename = filename
        if mode not in ('w','r','a','x'):
            raise ValueError("Invalid file mode, please use 'r','w','a','x'")
        self.mode = mode

    # called on successful "with"
    def __enter__(self):
        print('Enter')
        self.file = open(self.filename,self.mode)
        return self.file

    # called on error and successful end
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

        if exc_type:
            print('Exception occurred')
        print(f'exc type: {exc_type}, exc value: {exc_val}')
        print('Exit')
        # return true to handle errors
        return True




with ManagedFile('notes.txt','w') as file:
    print("We opened the file!")
    file.cool_guy('test')
    file.write('some text')

print('Continuing!')

with open_managed_file('notes2.txt','w') as file:
    print("We opened the function based context manager!")
    file.write('func based')
    file.dne()
