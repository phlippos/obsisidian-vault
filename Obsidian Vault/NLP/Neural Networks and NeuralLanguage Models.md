**Feedforward Neural Language Modeling**

+  predicting upcoming words from prior words
+ A feedforward neural language model (LM) is a feedforward network that takes as input at time t a representation of some number of previous words (wt−1,wt−2, etc.) and outputs a probability distribution over possible next words.
+ the feedforward neural LM approximates the probability of a word given the entire prior context P(wt |w1:t−1) by approximating based on the N − 1 previous words
+ Neural language models represent words in this prior context by their embeddings, rather than just by their word identity as used in n-gram language models. Using embeddings allows neural language models to generalize better to unseen data. For example, suppose we’ve seen this sentence in training:
	+ I have to make sure that the cat gets fed.
+ but have never seen the words “gets fed” after the word “dog”. Our test set has the prefix “I forgot to make sure that the dog gets”. What’s the next word? An n-gram language model will predict “fed” after “that the cat gets”, but not after “that the dog gets”. But a neural LM, knowing that “cat” and “dog” have similar embeddings, will be able to generalize from the “cat” context to assign a high enough probability to “fed” even after seeing “dog”.
+ 