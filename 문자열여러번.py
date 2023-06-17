def solution(my_string, queries):
    string = my_string
    for n,m in queries:
        st = string[n:m+1]
        st = st[::-1]
        string = string[:n] +st +string[m+1:]
        print(string)
    return my_string

a = solution("rermgorpsam",[[2, 3], [0, 7], [5, 9], [6, 10]])


"""
    queries	my_string
"rermgorpsam"
[2, 3]	"remrgorpsam"
[0, 7]	"progrmersam"
[5, 9]	"prograsremm"
[6, 10]	"programmers"
    """