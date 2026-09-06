from sklearn.metrics import classification_report, confusion_matrix
import logging

def process_evaluate(y_test, pred, logger):
    logger.info("Evaluating model")
    print(classification_report(y_test, pred))
    print(confusion_matrix(y_test, pred))