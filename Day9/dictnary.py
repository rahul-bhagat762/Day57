# programming_dic = {
#     "Bug" : "An error in a program that prevents the program from running as expected.",
#     "function" : "A piece of code that you can easily call over and over again.",
#     "Loop" : "The action of doing something over and over again"
# }
# print(programming_dic["Bug"])

# # Adding new items to dictionary
# programming_dic['print'] = "This is function is used for printing something"
# print(programming_dic['print'])


# empty_dict = {}
# empty_dict['Ram'] = "A devotional person"
# print(empty_dict['Ram'])
# for things in programming_dic:
#     print(things)
#     print(programming_dic[things])

capital = {
    "france":"Paris",
    "Germany": "Berlin",
}

travel_log = {
    "france": ['paris','lille','Bijon'],
    "germany" : ["Berlin","Hamburg","Stuttgart"]
}

# Nesting dict in dict
travel_log = {
    "france": {"cities_visited":['paris','lille','Bijon'],"total_visits":12},
    "germany" : ["Berlin","Hamburg","Stuttgart"]
}

print(travel_log["france"])