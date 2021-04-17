word=input()
yuanyin=list('aeiou')
if word[0] in yuanyin:
    print('no')
else:
    i=1
    a=1
    while i<len(word):
        if word[i] not in yuanyin:
            i+=1
        else:
            a+=1
            break

    while i<len(word):
        if word[i] in yuanyin:
            i+=1
        else:
            a+=1
            break

    while i<len(word):
        if word[i] not in yuanyin:
            i+=1
        else:
            a+=1
            break
    while i<len(word):
        if word[i] in yuanyin:
            i+=1
        else:
            a+=1
            break
            
        
        
    if a==4:
        print('yes')
    else:
        print('no')
        
        
        
