import os

path = os.path.dirname(os.path.abspath(__file__))
full_path_in = os.path.join(path, 'report.csv')

dataset = open(full_path_in, 'r')

dataset.readline()
lines = dataset.readlines()

result = []

for x in lines:
    y = x.strip().replace('"', "").replace(' ', "").split(",")
    result.append(y)
    z = '|'.join(y)

temp = []
for i in range(len(result)):
    if result[i][3] == "":
        temp.append(i)
co = 0
for i in temp:
    result.pop(i - co)
    co = co + 1

population = []
violent_crimes = []
homicides = []
rapes = []
assaults = []
robberies = []

for i in range(len(result)):
    population.append(result[i][4])
    violent_crimes.append(result[i][5])
    homicides.append(result[i][6])
    rapes.append(result[i][7])
    assaults.append(result[i][8])
    robberies.append(result[i][9])

pop = []
vc = []
hc = []
rp = []
at = []
rb = []

for i in range(len(population)):
    if population[i].isdigit():
        pop.append(int(population[i]))

for i in range(len(violent_crimes)):
    if violent_crimes[i].isdigit():
        vc.append(int(violent_crimes[i]))

for i in range(len(homicides)):
    if homicides[i].isdigit():
        hc.append(int(homicides[i]))

for i in range(len(rapes)):
    if rapes[i].isdigit():
        rp.append(int(rapes[i]))

for i in range(len(assaults)):
    if assaults[i].isdigit():
        at.append(int(assaults[i]))

for i in range(len(robberies)):
    if robberies[i].isdigit():
        rb.append(int(robberies[i]))

max_pop = max(pop)
max_vc = max(vc)
max_hc = max(hc)
max_rp = max(rp)
max_at = max(at)
max_rb = max(rb)

for i in range(len(result)):
    if result[i][9] == str(max_rb):
        print("The highest number of robberies in the US occured in the year", result[i][0], "in the state of",
              result[i][2])

avg_pop = sum(pop) / len(pop)
avg_vc = sum(vc) / len(vc)
avg_hc = sum(hc) / len(hc)
avg_rp = sum(rp) / len(rp)
avg_at = sum(at) / len(at)
avg_rb = sum(rb) / len(rb)

print("The average number of violent crimes committed in the US from 1975 to 2015 are", round(avg_vc))

range_pop = max(pop) - min(pop)
range_vc = max(vc) - min(vc)
range_hc = max(hc) - min(hc)
range_rp = max(rp) - min(rp)
range_at = max(at) - min(at)
range_rb = max(rb) - min(rb)

temp_pop = 0
var_pop = 0
for i in pop:
    temp_pop = temp_pop + ((i - avg_pop) ** 2)
var_pop = temp_pop / (len(pop) - 1)
std_pop = (var_pop ** 0.5)

temp_vc = 0
var_vc = 0
for i in vc:
    temp_vc = temp_vc + ((i - avg_vc) ** 2)
var_vc = temp_vc / (len(vc) - 1)
std_vc = (var_vc ** 0.5)

temp_hc = 0
var_hc = 0
for i in hc:
    temp_hc = temp_hc + ((i - avg_hc) ** 2)
var_hc = temp_hc / (len(hc) - 1)
std_hc = (var_hc ** 0.5)

temp_rp = 0
var_rp = 0
for i in rp:
    temp_rp = temp_rp + ((i - avg_rp) ** 2)
var_rp = temp_rp / (len(rp) - 1)
std_rp = (var_rp ** 0.5)

temp_at = 0
var_at = 0
for i in at:
    temp_at = temp_at + ((i - avg_at) ** 2)
var_at = temp_at / (len(at) - 1)
std_at = (var_at ** 0.5)

temp_rb = 0
var_rb = 0
std_rb = 0
for i in rb:
    temp_rb = temp_rb + ((i - avg_rb) ** 2)
var_rb = temp_rb / (len(rb) - 1)
std_rb = (var_rb ** 0.5)

print('\n')

print("The max value in population is", max_pop)
print("The max value in violent_crimes is", max_vc)
print("The max value in homicides is", max_hc)
print("The max value in rapes is", max_rp)
print("The max value in assaults is", max_at)
print("The max value in robberies is", max_rb)
print('\n')
print("The average value of population is", avg_pop)
print("The average value of violent_crimes is", avg_vc)
print("The average value of homicides is", avg_hc)
print("The average value of rapes is", avg_rp)
print("The average value of assaults is", avg_at)
print("The average value of robberies is", avg_rb)
print('\n')
print("The range of population is", range_pop)
print("The range of violent_crimes is", range_vc)
print("The range of homicides is", range_hc)
print("The range of rapes is", range_rp)
print("The range of assaults is", range_at)
print("The range of robberies is", range_rb)
print('\n')
print("The standard deviation of population is", std_pop)
print("The standard deviation of violent_crimes is", std_vc)
print("The standard deviation of homicides is", std_hc)
print("The standard deviation of rapes is", std_rp)
print("The standard deviation of assaults is", std_at)
print("The standard deviation of robberies is", std_rb)

