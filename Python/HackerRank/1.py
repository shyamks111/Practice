if __name__ == '__main__':
    
    s = "qA2"
    s1 = [False,False,False,False,False]

    for i in range(len(s)):
        
        if(s[i].isalnum()):
            s1[i] = True
        if(s[i].isalpha()):
            s1[i] = True
        if(s[i].isdigit()):
            s1[i] = True
        if("qa".islower()):
            s1[i] = True
        if('A'.isupper()):
            s1[i] = True
    print(s1)