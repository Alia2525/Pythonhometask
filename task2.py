# Маємо три кортежі цілих чисел. Знайдіть елементи, які унікальні для кожного списку.

kor1 = (1, 2, 3, 4)
kor2 = (3, 4, 5, 6)
kor3 = (0, 4, 3, 7)


unique_kor1 = set(kor1) - set(kor2) - set(kor3)
unique_kor2 = set(kor2) - set(kor1) - set(kor3)
unique_kor3 = set(kor3) - set(kor1) - set(kor2)

print("Унікальні елементи для 1 кортежу:", unique_kor1)
print("Унікальні елементи для 2 кортежу:", unique_kor2)
print("Унікальні елементи для 3 кортежу:", unique_kor3)