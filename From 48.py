# import requests
# response = requests.get("http://www.pythonhow.com/data/universe.txt")
# response_text = response.text
# print(response_text)


# import urllib.request
#
# txt = urllib.request.urlopen("http://www.pythonhow.com/data/sampledata.txt")
# print(txt)
# for line in txt:
#     for x in str(line):
#         if x.isdigit():
#             print(x)


# import webbrowser
#
# query = input("Search: ")
# webbrowser.open("https://www.google.com/search?q=%s" % query)


# import pandas
# import matplotlib.pylab as plt
#
# data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
# data.plot(x='x', y='y', kind='scatter')
# plt.show()

# import random
#
# characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
# # chosen = random.sample(characters, 6)
# # password = "".join(chosen)
# # print(password)
# password = ""
#
# while True:
#     i = random.randrange(0, len(characters))
#     password += characters[i]
#     if len(password) >= 6:
#         break
# print(password)