# python3

def parallel_processing(n, m, data):
    output = [[0]*2]*m
    nums = [0]*n
    step = 0
    data_used = 0
    while True:
        for i in range(n):
            if nums[i]==step:
                nums[i]+=int(data[data_used])
                output[data_used] = [i,step]
                data_used+=1
        step+=1
        if(data_used==m):
            break

    

    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n,m = input().split()
    n = int(n)
    m = int(m)

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    
    data = input().split()
    

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    for i in range(m):
        print(*result[i], sep = ' ')

    # TODO: print out the results, each pair in it's own line



if __name__ == "__main__":
    main()
