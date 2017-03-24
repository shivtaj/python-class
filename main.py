a=int(raw_input("press 1 for student to teacher\npress 2 for battleship \npress 3 for exam statistics\n "))
if a==1:
    import student_to_teacher
elif a==2:
    import battleship
elif a==3:
    import exam_stats
else:
    print "wrong choice"
