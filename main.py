def popular_words(text, words):
    # Переводимо текст в нижній регістр
    text = text.lower()

    # Створюємо словник для зберігання результатів
    result = {word: 0 for word in words}

    # Розділяємо текст на слова
    text_words = text.split()

    # Підраховуємо кількість входжень кожного слова
    for word in words:
        result[word] = text_words.count(word)

    return result

# Тестуємо функцію
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

