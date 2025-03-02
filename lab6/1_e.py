def all_elements_true(input_tuple):
    return all(input_tuple)  # это функция чтобы проверить все ли элементы являются истинными
tuple1 = (True, True, True)
tuple2 = (True, False, True)
tuple3 = (1, 2, 3)  # Все ненулевые значения считаются истинными
tuple4 = (0, 1, 2)  # на всякий 0 считается ложным

print(f"All elements in {tuple1} are True: {all_elements_true(tuple1)}")
print(f"All elements in {tuple2} are True: {all_elements_true(tuple2)}")
print(f"All elements in {tuple3} are True: {all_elements_true(tuple3)}")
print(f"All elements in {tuple4} are True: {all_elements_true(tuple4)}")