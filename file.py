# "W" is used for writing, "A" for appending, "R" for reading, "R+" for reading/writing. (in lowercase):
# To open file is file = open("./data.csv", "w")
#file = open("./data.csv", "r+")
"""
file.write("id, name, age, email, phone no\n ".upper())

file.write("1, Paul, 35, maduabuchi07@gmail.com, 07038550939\n ")
file.write("2, Benardine, 23, ife023@gmail.com, 07042484633\n ")
file.write("3, Alexander, 4, alexboy04@gmail.com, 09068928214\n ")
file.write("4, Jason, 2, Jayboy02@gmail.com, 08144715128\n ")
file.write("5, Emmanuel, 78, Emma78@gmail.com, 08064649057\n ")
file.write("6, Benedeth, 65, Benny65@gmail.com, 08063652620\n ")
file.write("7, Blessing, 48, BB48@gmail.com, 08038528095\n ")
file.write("8, Daniel, 46, Madanny46@gmail.com, 08034029596\n ")
file.write("9, Christopher, 45, Chris45@gmail.com, 07033660866\n ")
file.write("10, Anthony, 43, ceeyay43@gmail.com, 08039584250\n ")
file.write("11, Juliana, 43, Jully43@gmail.com, 08068627549\n ")
file.write("12, Amarachi, 39, Amy39@gmail.com, 08038162264\n ")
file.write("13, Peter, 35, Sirpee35@gmail.com, 09167042433\n ")
file.write("14, Esther, 31, Esty31@gmail.com, 09047551791\n ")

#print(file.read())
#print(file.readlines())
#print(file.readline())
#file.close()
"""
import os.path

filename = "./data.csv" # OR "data.csv"

if os.path.isfile(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"file {filename} does not exist")
"""

#for line in file:
   # print(line)
#ANOTHER WAY TO READ A FILE WITHOUT CLOSING LATER: WE DON'T HAVE TO SAY "FILE.CLOSE() AGAIN":
#with open("./data.csv", "r") as file:
    #print(file.read())
"""
