def leastFrequentCharcter(str1):
    leastFreq=str1.count(str1[0]);
    for charcter in str1:
        freq=str1.count(charcter);
        if(freq<leastFreq):
            leastFreq=freq;
            leastFreqCharacter=charcter;
    cnt=0;
    leastFreqCharacterList=[];    #Empty list
    for charcter in str1:
        freq=str1.count(charcter);
        if(freq==leastFreq):
            leastFreqCharacterList.append(charcter);
            cnt+=1;
    if(cnt==1):
        print(f"Least frequent character from a given string is {leastFreqCharacter}");
    else:
        print(f"Least frequent characters from a given string are {leastFreqCharacterList}");

str1="geeksfgeeks";
leastFrequentCharcter(str1);