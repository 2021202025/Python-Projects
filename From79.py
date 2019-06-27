while True:
    password = input("Enter the password: ")
    if (any(char.isdigit() for char in password)):
        if(len(password) >= 5):
            if(any(char.isupper() for char in password)):
                print("Success")
                break
            else:
                print("Must contain at least 1 Upper Case")
        else:
            print("Must over 5 chars in length")
    else:
        print("Must contain a number")

print(password)


while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)

with open("countries-raw.txt", "r") as file:
    content = file.readlines()

content = [i.strip("\n") for i in content if "\n" in i]
content = [i for i in content if i != ""]
content = [i for i in content if i != "Top of Page"]
content = [i for i in content if len(i) > 1]
# for i in content:
#     print(i)


checklist = ["Portugal", "Germany", "Munster", "Spain"]

for i in content:
    if i in checklist:
        continue
    else:
        checklist.append(i)
print(sorted(checklist))

import pandas

dataFrame = pandas.read_csv("countries-by-area.txt")
dataFrame = dataFrame.T
area = dataFrame.iloc[2]
population = dataFrame.iloc[3]
pop_density = []
count = 0
for a,p in zip(area,population):
    pop_density.append(population[count]/area[count])
    count += 1
    if count >= 50:
        break

# print(pop_density)
dataFrame = dataFrame.T
dataFrame = dataFrame.assign(Density = pop_density)

# print(dataFrame)
dataFrame = dataFrame.T
# most_dense = dataFrame.iloc[4]
# print(sorted(most_dense, reverse=True))
# dataFrame = dataFrame.T
print(sorted(dataFrame.iloc[4], reverse=True))

import pandas

data = pandas.read_csv("countries_by_area.txt")
data["density"] = data["population_2013"] / data["area_sqkm"]
data = data.sort_values(by="density", ascending=False)

for index, row in data[:5].iterrows():
    print(row["country"])