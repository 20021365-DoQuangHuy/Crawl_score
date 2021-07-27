import plot
import matplotlib.pyplot as plt

# Nên chạy ở trong máy để có thể phóng to biểu đồ
# Dữ liệu điểm được lưu dưới dạng List trong plot.py dưới tên super_list
# Hoàn toàn có thể import dữ liệu theo cách khác thuận tiện hơn

Mlist = []
for i in range(10 * 2 + 1):
	Mlist.append(0)
count = 0
for i in plot.super_list:
	count += 1
	"""
	if i["Van"] * i["Su"] * i["Dia"] != 0:
		d = i["Van"] + i["Su"] + i["Dia"]
		Mlist[int(d * 2)] += 1
	"""
	d = i["Anh"]
	if i["Anh"] == 10:
		print("*")
	Mlist[int(d * 2)] += 1
for i in Mlist:
	print(i, end = " ")
Mlist[0] = 0

xlist = []
for i in range(0, len(Mlist) - 1):
	xlist.append(str(i / 2) + "+")
  # print(str(i * 0.5 + 20) + "+", end = " ")
xlist.append(str(10.0))



plt.title('Phổ điểm tỉnh')
plt.xticks(rotation='vertical')
plt.bar(xlist, Mlist)

for i, v in enumerate(Mlist):
    plt.text(i - .25, v + 7, str(v),rotation=90)

plt.show()