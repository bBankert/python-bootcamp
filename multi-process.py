from multiprocessing import Pool, Process

def f(x):
    return x*x

def print_name(name):
    print(f"Hello {name}")



if __name__ == '__main__':
    # Pool is for parallelism
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
    # Process
    # p = Process(target=print_name, args=('bob',))
    # p.start()
    # p.join()