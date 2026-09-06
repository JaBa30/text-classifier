from data import load_data
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import logging
from evaluate_ai import process_evaluate

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
logger = logging.getLogger(__name__)

path = "data/messages.csv"
logger.info("Loading dataset")
data = load_data(path)
logger.info(f"Loaded {len(data)} rows")
X = data["text"]
y = data["label"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
    )
logger.info(f"Train size: {len(X_train)}")
logger.info(f"Test size: {len(X_test)}")

vectorizer = TfidfVectorizer(
    max_features=20_000,
    ngram_range=(1, 2),
    min_df = 2,
)
logger.info("TF-IDF vectorization completed")

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
logger.info("Training Logistic Regression")
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)
logger.info("Training completed")
pred = model.predict(X_test_vec)

process_evaluate(y_test, pred, logger)