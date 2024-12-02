# load and prepare data
data =[]

with open("day2/input.txt","r") as file:
    for line in file:
        data.append([int(num) for num in line.split()])


# example data
# data = [[7, 6, 4, 2, 1],
# [1, 2, 7, 8, 9],
# [9, 7, 6, 2, 1],
# [1, 3, 2, 4, 5],
# [8, 6, 4, 4, 1],
# [1, 3, 6, 7, 9]]

def is_report_safe(report):
    if len(report) <=1:
        return True
    else:
        if (report[0] > report[1]):
            adj = -1
        else:
            adj = 1

        for i in range(1,len(report)):
            diff = (report[i] - report[i-1])*adj
            if (diff<1 or diff>3):
                return False
        return True

safe_reports_num = 0
safe_reports_num_with_dampener = 0

for report in data:
    if is_report_safe(report=report):
        safe_reports_num+=1


print("Number of safe reports: ",safe_reports_num)

for report in data:
    if is_report_safe(report=report):
        safe_reports_num_with_dampener+=1
    else:
        for i in range(len(report)):
            creport = report.copy()
            creport.pop(i)
            if is_report_safe(creport):
                safe_reports_num_with_dampener+=1
                break

print("Number of safe reports with problem dampener: ",safe_reports_num_with_dampener)
