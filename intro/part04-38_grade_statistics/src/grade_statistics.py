# Write your solution here
def input_from_student():
    count = 0
    point_list = []
    while True:
        points = input("Exam points and exercises completed: ")
        if points == "":
            break
        else:
            str_point = points.split()
            exam_point = int(str_point[0])
            exer_point = 0
            if len(str_point[1])<3:
                exer_point = int(str_point[1][0])
            else:
                exer_point = int(str_point[1][0:2])
            point_list.append([exam_point, exer_point])
            count += 1
    return point_list
def statistics(point_list):
    print("Statistics:")
    point = 0
    total = 0
    g5, g4, g3, g2, g1, g0 = "","","","","",""
    for item in point_list:
        point = sum(item)
        total += point
        if item[0] >= 10:
            if point in range(15, 18):
                g1 += "*"
            elif point in range(18,21):
                g2 += "*"
            elif point in range(21,24):
                g3 += "*"
            elif point in range(24,28):
                g4 += "*"
            elif point in range(28,31):
                g5 += "*"
            elif point in range(0,15):
                g0 += "*"
        elif item[0] < 10:
            g0 += "*"
    avg = total/len(point_list)
    percent = (len(point_list)-len(g0)) * 100 /len(point_list)
    print(f"Points average: {avg:.1f}")
    print(f"Pass percentage: {percent:.1f}")
    print("Grade distribution:")
    print(f"5: {g5}\n4: {g4}\n3: {g3}\n2: {g2}\n1: {g1}\n0: {g0}")

statistics(input_from_student())
