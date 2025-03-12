#Tuple
#Giống list nhưng không thể thay đổi(immutable)
#Không thể thay đổi phần tử trong tuple
numbers = (1,2,3,4,5)
print(numbers)
print(numbers[0])
print(numbers[-1])

#Set
#Tập hợp (set) chứa các giá trị không trùng lặp và không có thứ tự cố định
numbers = {1,2,3,4,5,6,6,6}
numbers.add(7)
numbers.remove(2)
print(numbers)
if 3 in numbers:
    print("có số 3")

#Dictionary
#Từ điển (dict) lưu trữ dữ liệu dưới dạng key: value.
student = {
    "Name": "Phúc",
    "Age": "21",
    "Major": "CNTT"
}
student["city"] = "Long An" #Thêm Key mới
student["Age"] = "30" #Cập nhật value
print(student)
#items giúp lấy toàn bộ cặp (key, value) trong dictionary
#Dùng f-string (f"{key}: {value}") để in ra key và giá trị tương ứng
for key, value in student.items():
    print(f"{key}: {value}")

print("==============================================")

fruits = ["Táo", "Chuối", "Cam", "Dưa Hấu"]

for fruit in fruits:
    print(fruit)

for i in range(len(fruits)):
    print(f"Phần tử {i}: {fruits[i]}")


print("==============================================")

#Duyệt nhiều danh sách cùng lúc với zip()
#Nếu có 2 danh sách và muốn duyệt cùng lúc, ta có thể dùng zip()
#zip() ghép phần từ tương ứng từ các danh sách lại với nhau

names = ["Phuc", "Huy", "Minh"]
ages = ["21", "21", "17"]

for names, ages in zip(names, ages):
    print(f"{names} - {ages} tuổi")


print("==============================================")

#List comprehension giúp viết code gọn hơn khi tạo danh sách mới

squares = [x**2 for x in range(1,6)]
print(squares)
#split() là phương thức của chuỗi string, dùng để tách chuỗi thành danh sách các phần tử dựa trên dấu phân cách
#map()
numbers = list(map(int, input("nhập danh sách số: ").split()))
squares = [x**2 for x in numbers]
print("bình phương: ", squares)