def tim_dong(file_name, tu_khoa):
    f = open(file_name, "r")
    dong = 1
    kq = []

    for line in f:
        if tu_khoa in line:
            kq.append(dong)
        dong = dong + 1

    f.close()
    return kq


print(tim_dong("myfile.txt", "hello"))