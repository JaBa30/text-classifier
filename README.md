## Problem

Модель классифицирует SMS-сообщения на spam и ham.

## Dataset

Датасет содержит текст сообщения и его label.

После удаления дубликатов осталось N записей.

Классы:
- ham — ...
- spam — ...

## Approach

1. Загрузка данных
2. Удаление пустых значений и дубликатов
3. Очистка текста
4. Train/test split
5. TF-IDF
6. Logistic Regression
7. Evaluation

## Metrics

              precision    recall  f1-score   support

         ham       1.00      1.00      1.00        44
        spam       1.00      1.00      1.00        27

    accuracy                           1.00        71
   macro avg       1.00      1.00      1.00        71
weighted avg       1.00      1.00      1.00        71

[[44  0]
 [ 0 27]]

## Project structure

```text
text-classifier/
├── README.md
├── requirements.txt
├── data/
├── src/
└── tests/