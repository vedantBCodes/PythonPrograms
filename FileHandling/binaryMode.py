"""
There are two modes in which file can be opened
1.text mode
2.binary mode

By default file opens in text mode
But one can open file in binary mode also.

Examples of binary files are
1.Executable files (.exe file)
2.Compressed files (zip files)
3.python files (.py files)
4.Images and audios

"""

obj=open("ReadingFromAFile.py","r+b");

data=obj.read();

print(type(data));  #Here the type of data will be bytes (not string)

print(data);