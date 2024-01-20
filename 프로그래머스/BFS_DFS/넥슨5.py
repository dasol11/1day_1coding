



def getProductSuggestions(products, search):
    li = [search[:i+1] for i in range(len(search)) ]
    result = []
    
    for word in li:
        save_word = []
        l = len(word)
        for pro in products:
            if word == pro[:l]:
                save_word.append(pro)
        
        if save_word:
            print(word ,save_word)
            result.append(sorted(save_word)[:3])
        
    return result
    
    
    
    
    


# print(getProductSuggestions(["capet", "cart","car","camera","crate"],"camera"))



print(getProductSuggestions(["abcda","abdca","abaaa","acfda"],"aaada"))