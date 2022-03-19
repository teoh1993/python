import os

f = open("raw_data.txt", "a")
f.write("id=001;name=Johan Strauss;address=58 Jalan Jelutong, 11600 Pulau Pinang, Malaysia;gender=male\nid=002;name=Jennifer Teng;address=Q-2-4,Desa Indah, Lorong Minyak, 13000 Kedah, Malaysia;gender=female\n")
f.close()

with open('raw_data.txt', 'r+') as file:

	lines = file.readlines()

res01 = []
for line in lines:
	line = line.rstrip("\n")
	info = line.split(';')
	res02 = []

	for x in info:
		data = x.split('=')
		if data[0] == 'address':
			address = data[1].split(',');
			val01 = address[0].split(' ')
			val02 = address[-2].split(' ')
			state = '';
			for idx, val in enumerate(val02):
				if idx != 0 and idx != 1:
					state += val+' '
			res02.append(['House number',val01[0]])
			res02.append(['Postcode',val02[1]])
			res02.append(['State',state])

		elif data[0] == 'id':
			res02.append(['Student',data[1]])
		elif data[0] == 'name':
			res02.append(['Name',data[1]])
		else:
			res02.append([data[0].capitalize(),data[1].capitalize()])
	res01.append(res02)

f = open("formatted.txt", "a")

for array in res01:
	for val in array:
		f.write(val[0]+": "+val[1]+"\n")
		f.write("\n")

# os.remove("formatted.txt")
os.remove("raw_data.txt")















import os

f = open("raw_data.txt", "a")
f.write("23,26,19,47,40,37,16,28,29,20,38,18,45,31,25,30,46,17,21,13,32,12,33,43,10,3,4,27,14,2,11,42,34,6,5,39,36,7,35,8,50,41,44,49,48,24,15,9,1,22")
f.close()

with open('raw_data.txt', 'r+') as file:
	lines = file.read()

numbers = lines.split(',')

odd = []
even = []
for number in numbers:
	# print(type(number))
	# print(number)
	if int(number) % 2 != 0:
		odd.append(int(number))
	else:
		even.append(int(number))

print(odd)
print(even)

def algo_sort(item):
	for i in range(len(item)):
		for j in range(len(item)):
			if item[i] < item[j]:
				temp = item[j]
				item[j] = item[i]
				item[i] = temp
	return item

# print(x)

odd_res = algo_sort(odd)
print(odd_res)
even_res = algo_sort(even)
print(even_res)



odd.sort()
print(odd)
even.sort()
print(even)

# os.remove("formatted.txt")
os.remove("raw_data.txt")
