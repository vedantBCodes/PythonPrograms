

def stringReverse(str1):
    str2=str1[::-1];
    return str2;

def stringPallindrome(str1):
    str2=str1[::-1];
    if(str1==str2):
        return True;
    else:
        return False;

def wordsInAString(str1):
    strList=str1.split();
    return len(strList);
