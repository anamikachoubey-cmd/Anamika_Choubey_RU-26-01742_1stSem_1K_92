
dayslist = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

print("Classroom Timetable Generator")

try:
    days = int(input("Enter number of days: "))
    periods = int(input("Enter periods per day: "))

except ValueError:
    print("Please enter whole numbers only")
    quit()

if days < 1 or days > 6:
    print("Invalid number of days")

elif periods <= 0:
    print("Periods should be positive")

else:

    total = days * periods

    try:
        num = int(input("Enter number of subjects: "))

    except ValueError:
        print("Please enter a whole number")
        quit()

    if num <= 0:
        print("Number of subjects should be positive")

    else:

        subjects = {}
        check = True

        for i in range(num):

            name = input("Enter subject name: ")

            if name == "":
                print("Subject name cannot be empty")
                check = False
                break

            if name in subjects:
                print("Subject already entered")
                check = False
                break

            try:
                p = int(input("Enter weekly periods: "))

            except ValueError:
                print("Please enter whole numbers only")
                check = False
                break

            if p <= 0:
                print("Periods should be positive")
                check = False
                break

            subjects[name] = p

        if check:

            totalperiods = 0

            for x in subjects:
                totalperiods = totalperiods + subjects[x]

            if totalperiods != total:

                print("Error: Total weekly periods (" + str(totalperiods) +
                      ") must equal available slots (" + str(total) + ").")

            else:

                for x in subjects:

                    if subjects[x] > days * 2:
                        print("Timetable cannot be generated:",
                              x, "needs", subjects[x], "periods in",
                              days, "days, but limit is 2 per day.")
                        check = False

                if check:

                    timetable = []
                    possible = True

                    for i in range(days):

                        today = []
                        count = {}

                        for x in subjects:
                            count[x] = 0

                        for j in range(periods):

                            selected = None
                            highest = -1

                            for x in subjects:

                                if subjects[x] > 0 and count[x] < 2:

                                    if subjects[x] > highest:
                                        highest = subjects[x]
                                        selected = x

                            if selected == None:
                                print("Timetable cannot be generated")
                                possible = False
                                break

                            today.append(selected)

                            subjects[selected] = subjects[selected] - 1
                            count[selected] = count[selected] + 1

                        if possible:
                            timetable.append(today)
                        else:
                            break

                    if possible and len(timetable) == days:

                        print()
                        print("Weekly Timetable")

                        for i in range(days):

                            print()
                            print(dayslist[i])

                            for j in range(periods):

                                print("Period", j + 1, ":",
                                      timetable[i][j])