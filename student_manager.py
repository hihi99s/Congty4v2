students = []


def add_student():
    student_id = input("Nhập mã sinh viên: ").strip()
    name = input("Nhập tên sinh viên: ").strip()
    age = input("Nhập tuổi: ").strip()

    if not student_id or not name or not age:
        print("Vui lòng nhập đầy đủ thông tin.\n")
        return

    students.append({
        "id": student_id,
        "name": name,
        "age": age,
    })
    print("Thêm sinh viên thành công.\n")


def delete_student():
    if not students:
        print("Chưa có sinh viên nào để xóa.\n")
        return

    student_id = input("Nhập mã sinh viên cần xóa: ").strip()

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Xóa sinh viên thành công.\n")
            return

    print("Không tìm thấy sinh viên có mã này.\n")


def show_students():
    if not students:
        print("Chưa có sinh viên nào.\n")
        return

    print("\nDanh sách sinh viên:")
    for index, student in enumerate(students, start=1):
        print(
            f"{index}. Mã SV: {student['id']} | Tên: {student['name']} | Tuổi: {student['age']}"
        )
    print()


def main():
    while True:
        print("===== QUẢN LÝ SINH VIÊN =====")
        print("1. Thêm sinh viên")
        print("2. Xem danh sách sinh viên")
        print("3. Xóa sinh viên")
        print("4. Thoát")

        choice = input("Chọn chức năng: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            print("Tạm biệt!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.\n")


if __name__ == "__main__":
    main()