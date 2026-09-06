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

The model achieved 96% accuracy and a macro F1-score of 0.91. It performs very well on ham messages, but spam recall is 0.72, meaning that 36 out of 128 spam messages were incorrectly classified as ham. The model is therefore conservative when predicting spam: its spam precision is 0.99, but it misses a noticeable portion of actual spam.

2026-09-06 16:55:39,080 | INFO | __main__ | Evaluating model
              precision    recall  f1-score   support

         ham       0.96      1.00      0.98       904
        spam       0.99      0.72      0.83       128

    accuracy                           0.96      1032
   macro avg       0.98      0.86      0.91      1032
weighted avg       0.97      0.96      0.96      1032

[[903   1]
 [ 36  92]]

## Project structure

```text
text-classifier/
├── README.md
├── requirements.txt
├── data/
├── src/
└── tests/