The Skip-gram model with negative sampling is a popular method used in training word embeddings, such as those produced by Word2Vec. This approach is particularly effective because it balances the task of predicting context words with a method to reduce computational complexity, making it feasible to train on large corpora of text.
The Skip-gram model aims to learn word embeddings by predicting the surrounding context words for a given target word in a sentence. For example, if the target word is "cat" in the sentence "The cat sits on the mat," the model tries to predict words like "The," "sits," "on," and "mat."
### Negative Sampling:

Negative sampling is a technique used to efficiently train the Skip-gram model. Instead of updating the model based on all words in the vocabulary, negative sampling selectively updates the model for a few "negative" samples (words not in the context) along with the positive context words.
![[Pasted image 20240901003916.png]]