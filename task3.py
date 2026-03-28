# Маємо три кортежі цілих чисел. Знайдіть елементи, які є в кожному з кортежів
# і знаходяться в кожному з них на тій самій позиції.

kor1 = (1, 2, 3, 4)
kor2 = (0, 2, 3, 5)
kor3 = (7, 2, 3, 8)


position_elements = [kor1[i] for i in range(min(len(kor1), len(kor2), len(kor3))) if kor1[i] == kor2[i] == kor3[i]]

print("Елементи, що збігаються за позицією:", position_elements)