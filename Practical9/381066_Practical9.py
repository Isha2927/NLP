from transformers import pipeline

# Load multilingual sentiment analysis pipeline
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment"
)

# Test sentences (Indian languages)
texts = [
    "मुझे यह बहुत पसंद आया",        # Hindi (Positive)
    "मला हे आवडलं नाही",           # Marathi (Negative)
    "This is amazing",             # English
    "यह ठीक है"                    # Neutral-ish Hindi
]

# Perform sentiment analysis
for text in texts:
    result = sentiment_pipeline(text)[0]
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']}, Confidence: {result['score']:.4f}")
    print("-" * 50)