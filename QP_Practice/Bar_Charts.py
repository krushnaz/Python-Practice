import matplotlib.pyplot as plt

courses = ['C++','Java','Python','MongoDB','Android']
student_enrolled = [25,30,40,20,35]

bar_width = 0.5

bar_color = ['red','blue','green','orange','purple']

edge_color = 'black'

plt.bar(courses,student_enrolled,width=bar_width,color= bar_color,edgecolor= edge_color)

plt.title("Students Enrolled in difference courses")
plt.xlabel("Courses")
plt.ylabel('Number of Students')

plt.legend(['Student Enrolled'], loc='upper right')

plt.show()