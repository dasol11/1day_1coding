
def getPopularityOrder(song_preferences):
    dic ={}
    for i in range(len(song_preferences[0])):
        dic[str(i)] = 0
    
    
    for song_list in song_preferences:
        for i in range(len(song_list)):
            dic[str(song_list[i])] += i
    
    sort_dic = list(sorted(dic.items(), key=lambda x: x[1]))
    
    return [i[0] for i in sort_dic]



print(getPopularityOrder([[0,2,3,1],[1,0,3,2],[2,1,0,3],[0,3,1,2]]))