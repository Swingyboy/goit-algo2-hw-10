from teacher import Teacher

def create_schedule(subjects, teachers):
    remaining_subjects = set(subjects)
    schedule = []

    while remaining_subjects:
        best_teacher = None
        best_subjects_covered = set()

        for teacher in teachers:
            subjects_covered = remaining_subjects & teacher.can_teach_subjects
            if (len(subjects_covered) > len(best_subjects_covered) or
                    (len(subjects_covered) == len(best_subjects_covered) and (best_teacher is None or teacher.age < best_teacher.age))):
                best_teacher = teacher
                best_subjects_covered = subjects_covered

        if not best_teacher:
            return None
        best_teacher.assigned_subjects = best_subjects_covered
        remaining_subjects -= best_subjects_covered
        schedule.append(best_teacher)

    return schedule

if __name__ == "__main__":
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}
    teachers = [
        Teacher("Oleksandr", "Ivanenko", 45, "o.ivanenko@example.com", {"Математика", "Фізика"}),
        Teacher("Maria", "Petrenko", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher("Serhii", "Kovalenko", 50, "s.kovalenko@example.com", {"Інформатика", "Математика"}),
        Teacher("Natalia", "Shevchenko", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}),
        Teacher("Dmytro", "Bondarenko", 35, "d.bondarenko@example.com", {"Фізика", "Інформатика"}),
        Teacher("Olena", "Grytsenko", 42, "o.grytsenko@example.com", {"Біологія"})
    ]
    schedule = create_schedule(subjects, teachers)

    # Виведення розкладу
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(teacher)
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
