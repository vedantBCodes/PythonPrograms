import random

names=input("Enter everybody's name seperated by comma:");

name_list=names.split(",");

lucky_guy=random.choice(name_list)
print(f"{lucky_guy} will pay the bill.");