import multiprocessing as mp
def cube(x):
    return x**3
if __name__ == '__main__':
    pool = mp.Pool(processes = 2)
    # results = [pool.apply(cube, [x]) for x in range (1,5)]
    # print(results)

    results = [pool.apply_async(cube, [x]) for x in range(1, 5)]
    output = [p.get() for p in results]
    print(output)