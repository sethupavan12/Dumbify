import os
import openai
import config
openai.api_key = config.api_key

response = openai.Completion.create(
  engine="davinci",
  prompt="##### Translate this function  from Python into Haskell\n### Python\n    \n    def predict_proba(X: Iterable[str]):\n        return np.array([predict_one_probas(tweet) for tweet in X])\n    \n### Haskell",
  temperature=0,
  max_tokens=54,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0,
  stop=["###"]
)