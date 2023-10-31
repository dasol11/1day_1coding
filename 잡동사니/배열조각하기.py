def solution(arr, query):
    for i in range(len(query)):
        if i % 2 ==0:
            del arr[query[i]+1:]
        else:
            del arr[:query[i]]
        print(arr)
    return arr


a = solution([0, 1, 2, 3, 4, 5], [4, 1, 2]	)
