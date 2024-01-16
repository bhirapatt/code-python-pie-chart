import matplotlib.pyplot as plt

#ชุดข้อมูล
labels = 'Bhirapatt', 'Ingkawat', 'Noppadol'
#ชื่อ
sizes = [20, 45, 35,]
#กำหนดขนาดของช่องแต่ละช่อง
colors = ["#007500","#00A300","#00D100"]
#กำหนดสีของแต่ละช่อง
explode = (0.0,0.0,0.0)
#ระยะห่างระหว่างช่อง
plt.pie(sizes, explode, colors=colors, labels=labels, startangle=125,)
#กำหนดค่าต่างๆ ของกราฟวงกลม
plt.title("Vote Leader of Class")
#แสดงหัวข้อของกราฟวงกลม
plt.show()
#แสดงกราฟ
