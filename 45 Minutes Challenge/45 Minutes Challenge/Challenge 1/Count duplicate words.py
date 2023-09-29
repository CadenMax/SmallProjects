lst = ["Your Honours degree is a direct pathway into a PhD or other research degree at Griffith",
       "A research degree is a postgraduate degree which primarily involves completing a supervised project of original research",
       "Completing a research program is your opportunity to make a substantial contribution to",
       "and develop a critical understanding of",
       "a specific discipline or area of professional practice",
       "The most common research program is a Doctor of Philosophy",
       "or PhD which is the highest level of education that can be achieved",
       "It will also give you the title of Dr"]
new_lst = []
myDict = {}


new_items = []
for item in lst:
    new_lst.extend(item.split())


def return_dict(my_list):
    for i in range(len(my_list)):
        myDict[my_list[i]] = myDict[my_list[i]] + 1 if my_list[i] in myDict else 1


return_dict(new_lst)
print(myDict)
