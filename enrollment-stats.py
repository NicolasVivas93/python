# Challenge list of  lists

universities = [
    ['California Institute of Technology',2175,37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

total_universities = len(universities)


def enrollment_stats(lista):
    lista_de_listas = []
    student_enrollment = [lista[i][1] for i in range(total_universities)]

    tuition_fees = [lista[i][2] for i in range(total_universities)]

    lista_de_listas.append(student_enrollment)
    lista_de_listas.append(tuition_fees)

    return lista_de_listas


def mean(lista):
    promedio = sum(lista) / len(lista)
    return round(promedio,2)

def median(lista):
    lista.sort()

    valor_central1 = lista[len(lista) // 2]
    valor_central2 = lista[(len(lista) // 2) - 1]

    if len(lista) % 2 == 0:
        mediana = (valor_central1 + valor_central2) / 2
    else:
        mediana = valor_central1

    return mediana

students_and_tuitions = enrollment_stats(universities)


total_students = sum(students_and_tuitions[0])
total_tuition_fees = sum(students_and_tuitions[1])

print(f"""
****************************
Total students: {total_students:,}
Total tuition: $ {total_tuition_fees:,}

Student mean: {mean(students_and_tuitions[0]):,}
Student median: {median(students_and_tuitions[0]):,}

Tuition mean: $ {mean(students_and_tuitions[1]):,}
Tuition median: $ {median(students_and_tuitions[1]):,}
****************************
""")

