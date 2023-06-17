def solution(my_string, is_suffix):
    answer_list = [my_string[i:] for i in range(len(my_string))]
    print(answer_list)
    return 1 if is_suffix in answer_list else 0
     

a = solution("banana","dsdsbanana")
print(a)