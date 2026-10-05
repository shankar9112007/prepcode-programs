students=int(input("enter number of students:"))
bench_capacity=int(input("enter bench capacity:"))
occupied_benches=students//bench_capacity
print("occupied benches:",occupied_benches)
students_left=occuiped_benches*bench_capacity-students
print("students_left:",students_left)