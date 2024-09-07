def test_function():
    print('Вижу работу функции test_function')
    def inner_function():
        print("Я в области видимости функции test_function")

    # Вызовем inner_function внутри test_function
    inner_function()
# Вызываем test_function, чтобы увидеть результат
test_function()
# tryinner_function() вызов вызовет ошибку