# Функция для обработки текста
def recognize(data, vectorizer, clf):
    # Получаем вектор полученного текста
    text_vector = vectorizer.transform([data]).toarray()[0]
    answer = clf.predict([text_vector])[0]
    return answer





