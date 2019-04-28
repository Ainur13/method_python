file = open("journal.txt", "r")
text = file.read()

final_marks=[]
students=text.split("\n")
for s in students:
    content=s.split()
    name = content[0]
    marks=content[1:]

    summa=0
    for m in marks:
        summa=summa+int(m)
    average=summa/len(marks)
    result = round(average)
    final_marks.append(result)
    
    print(name, result)

file.close()

file = open("journal_final.txt", "w")

for i in range(len(students)):
    students[i] = students[i] + " Final: " + str(final_marks[i]) + "\n"
    file.write(students[i])
    
file.close()
