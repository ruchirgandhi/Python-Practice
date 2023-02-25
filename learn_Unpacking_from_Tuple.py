
work_hours = [("Bill",400), ("Sam",300),("Mike",200)]



def emp_work(work_hours):
    current_max = 0
    employee = ''
    for emp, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee = emp

        else:
            pass


    return (employee,current_max)


x = (emp_work(work_hours))
print(list(x))
print(tuple(x))

