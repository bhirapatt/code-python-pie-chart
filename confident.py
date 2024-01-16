import matplotlib.pyplot as plt

#ชุดข้อมูล
labels = 'Bhirapatt', 'Ingkawat', 'Noppadol'
#ชื่อ
sizes = [20, 45, 35,]
#กำหนดขนาดของช่องแต่ละช่อง
colors = ["#007500","#00A300","#00D100"]
#ระยะห่างจากส่วนอื่นๆ
explode = (0.0,0.0,0.0)
#subplots มีหน้าช่วยให้แสดงข้อมูลในแนวแกน x และ y
fig1, ax1 = plt.subplots()
#ทำให้อัตราส่วนของวงกลมเท่ากันและถูกวาดเป็นวงกลม
ax1.pie(sizes, explode,counterclock=3,colors=colors, labels=labels,startangle=125)
#equal เป็นการกำหนดให้แผนภูมิที่วาดออกมานั้นเท่ากัน
ax1.axis('equal')
plt.title("Vote Leader of Class")
plt.show()