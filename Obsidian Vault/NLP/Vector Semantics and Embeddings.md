

### **Vector Semantics**
to define the meaning of a word by its distribution in language use, meaning its neighboring words or grammatical environments. Their idea was that two words that occur in very similar distributions (whose neighboring words are similar) have similar meanings. For example, suppose you didn’t know the meaning of the word ongchoi (a recent borrowing from Cantonese) but you see it in the following contexts: 
(6.1) Ongchoi is delicious sauteed with garlic. 
(6.2) Ongchoi is superb over rice. (
6.3) ...ongchoi leaves with salty sauces... 
And suppose that you had seen many of these context words in other contexts: 
(6.4) ...spinach sauteed with garlic over rice... 
(6.5) ...chard stems and leaves are delicious... 
(6.6) ...collard greens and other salty leafy greens

The fact that ongchoi occurs with words like rice and garlic and delicious and salty, as do words like spinach, chard, and collard greens might suggest that ongchoi is a leafy green similar to these other leafy greens.1 We can do the same thing computationally by just counting words in the context of ongchoi.

**Embeddings**
The idea of vector semantics is to represent a word as a point in a multidimensional semantic space that is derived (in ways we’ll see) from the distributions of embeddings word neighbors. Vectors for representing words are called embeddings (although the term is sometimes more strictly applied only to dense vectors like word2vec
rather than sparse tf-idf or PPMI vectors.
![[Pasted image 20240325164420.png]]
Fig. 6.1 shows a visualization of embeddings learned for sentiment analysis, showing the location of selected words projected down from 60-dimensional space into a two dimensional space. Notice the distinct regions containing positive words, negative words, and neutral function words.


**Words and Vectors**
“The most important attributes of a vector in 3-space are {Location, Location, Location}”

Vector or distributional models of meaning are generally based on a co-occurrence matrix, a way of representing how often words co-occur.

 + **Vectors and documents**
	 + **term-document matrix**
		 + In a term-document matrix, each row represents a word in the vocabulary and each term-document matrix column represents a document from some collection of documents.
		 + ![[Pasted image 20240325164655.png]]
		 + So As You Like It is represented as the list [1,114,36,20] (the first **column vector**)
		 + A **vector space** is a collection of vectors, characterized by their dimension
		 + in real term-document matrices, the vectors representing each document would have dimensionality |V|, the vocabulary size.
		+ Term-document matrices were originally defined as a means of finding similar documents for the task of document **information retrieval**. Two documents that are similar will tend to have similar words, and if two documents have similar words their column vectors will tend to be similar.
		+ ![[Pasted image 20240325165056.png]]
		+ ![[Pasted image 20240325165130.png]]
		+ **Information retrieval** (IR) is the task of finding the document d from the D documents in some collection that best matches a query q. For IR we’ll therefore also represent a query by a vector, also of length |V|, and we’ll need a way to compare two vectors to find how similar they are. (Doing IR will also require efficient ways to store and manipulate these vectors by making use of the convenient fact that these vectors are sparse, i.e., mostly zeros).
	+ **Words as vectors: document dimensions**
		+ vector semantics can also be used to represent the meaning of words. We do this row vector by associating each word with a word vector— a row vector rather than a column vector, hence with different dimensions
		+ ![[Pasted image 20240325165322.png]]
		+ For documents, we saw that similar documents had similar vectors, because similar documents tend to have similar words. This same principle applies to words: similar words have similar vectors because they tend to occur in similar documents. The term-document matrix thus lets us represent the meaning of a word by the documents it tends to occur in.
	+ **Words as vectors: word dimensions**
		+ term-term matrix, also called the word-word matrix or the term-context matrix, in which the columns are labeled by words rather word-word matrix than documents. This matrix is thus of dimensionality |V|×|V| and each cell records the number of times the row (target) word and the column (context) word co-occur in some context in some training corpus. The context could be the document, in which case the cell represents the number of times the two words appear in the same document.
		+ It is most common, however, to use smaller contexts, generally a window around the word, for example of 4 words to the left and 4 words to the right, in which case the cell represents the number of times (in some training corpus) the column word occurs in such a ±4 word window around the row word.
+ **TF-IDF**
	+ If we want to know what kinds of contexts are shared by cherry and strawberry but not by digital and information, we’re not going to get good discrimination from words like the, it, or they, which occur frequently with all sorts of words and aren’t informative about any particular word.
	+ It’s a bit of a paradox. Words that occur nearby frequently (maybe pie nearby cherry) are more important than words that only appear once or twice. Yet words that are too frequent—ubiquitous, like the or good— are unimportant.
	+ the **tf-idf** weighting, usually used when the dimensions are documents.
	+ The first is the **term frequency**
		+ the frequency of the word t in the document d.
		+ $$tf_{t,d} = count(t,d)$$
		+ More commonly we squash the raw frequency a bit, by using the log10 of the frequency instead.The intuition is that a word appearing 100 times in a document doesn’t make that word 100 times more likely to be relevant to the meaning of the document.
		+ $$ tf_{t,d}=\biggl\{ \begin{align*} 
		   1+log_{10}count(t,d) ,\ if\ count(t,d)>0 \\
		   0, \ otherwise
		   \end{align*}
		   $$
		   If we use log weighting, terms which occur 0 times in a document would have tf = 0, 1 times in a document tf = 1 + log10(1) = 1 + 0 = 1, 10 times in a document tf = 1+log10(10) = 2, 100 times tf = 1+log10(100) = 3, 1000 times tf = 4, and so on.
	+ The second factor in tf-idf is used to give a higher weight to words that occur only in a few documents.Terms that are limited to a few documents are useful for discriminating those documents from the rest of the collection;terms that occur frequently across the entire collection aren’t as helpful.
	+ The **document frequency** df_t of a term t is the number of documents it occurs in. **Document frequency** is not the same as the **collection frequency** of a term, which is the total number of times the word appears in the whole collection in any document.
	+ Consider in the collection of Shakespeare’s 37 plays the two words Romeo and action. The words have identical collection frequencies (they both occur 113 times in all the plays) but very different document frequencies, since Romeo only occurs in a single play. If our goal is to find documents about the romantic tribulations of Romeo, the word Romeo should be highly weighted, but not action:
	+ ![[Pasted image 20240325201542.png]]
	+ We emphasize discriminative words like Romeo via the **inverse document frequency** or **idf** term weight.
	+ The **idf** is defined using the fraction N/dft , where N is the total number of documents in the collection, and dft is the number of documents in which term t occurs.
	+ $$ idf = N/df_t$$
	+ The fewer documents in which a term occurs, the higher this weight.
	+ Occasionally your corpus might not have appropriate document divisions and you might need to break up the corpus into documents yourself for the purposes of computing idf.Because of the large number of documents in many collections, this measure too is usually squashed with a log function. The resulting definition for inverse document frequency (idf) is thus
	+  $$ idf_t = log_{10}(N/df_t)$$
	+ **tf-idf** 
	+ $$ w_{t,d} = tf_{t,d} *idf_t $$
	+ tf-idf is high if and only if term frequency and inverse document frequency are high. This means that the term t occurs frequently in certain documents and in a small number of documents.
	+ ![[Pasted image 20240325202823.png]]
+ **Pointweise Mutual Information(PMI**
	+ PPMI (positive pointwise mutual information), is used for term-term-matrices, when the vector dimensions correspond to words rather than documents. PPMI draws on the intuition that the best way to weigh the association between two words is to ask how much more the two words co-occur in our corpus
	+ than we would have a priori expected them to appear by chance.
	+ It is a measure of how often two events x and y occur, compared with what we would expect if they were independent:
	+ $$ I(x,y) = log_2{P(x,y)/(P(x)P(y))}$$
	+ The numerator tells us how often we observed the two words together.The denominator tells us how often we would expect the two words to co-occur assuming they each occurred independently
	+ PMI is a useful tool whenever we need to find words that are strongly associated.
	+ PMI values range from negative to positive infinity. But negative PMI values tend to be unreliable unless our corpora are enormous.
		$$ I(X,Y)=\sum_x \sum_y P(x,y)log_2{\frac{P(x,y)}{(P(x)P(y))}}$$

	+ **Positive PMI** (called PPMI) which replaces all negative PMI values with zero
	+ $$ PPMI(w,c)=\max(log_2{\frac{P(w,c)}{P(w)P(c)}},0)$$
	+ More formally,let’s assume we have a co-occurrence matrix F with W rows (words) and C columns (contexts), where fi,j gives the number of times word wi occurs with context cj . This can be turned into a PPMI matrix where PPMIi j gives the PPMI value of word wi with context cj (which we can also express as PPMI(wi , cj) or PPMI(w = i, c = j))
	+ $$PPMI_{ij}=\max(log_2{\frac{P_{ij}}{P_iP_j}},0)$$
	+ ![[Pasted image 20240325204941.png]]
	+ ![[Pasted image 20240325205030.png]]
	+ PMI has the **problem** of being biased toward infrequent events; very rare words tend to have very high PMI values. One way to reduce this bias toward low frequency events is to slightly change the computation for P(c), using a different function Pα(c) that raises the probability of the context word to the power of α:
	+ ![[Pasted image 20240325205302.png]]
	+ a setting of α = 0.75 improved performance of embeddings on a wide range of tasks. This works because raising the count to α = 0.75 increases the probability assigned to rare contexts, and hence lowers their PMI (Pα(c) > P(c) when c is rare).
+ **Centroid and document vector**
	+ The **centroid** is the multidimensional version of the mean; the centroid of a set of vectors is a single vector that has the minimum sum of squared distances to each of the vectors in the set. Given k word vectors w1,w2,...,wk , the centroid **document vector** d is:
	+ $$ d = \frac{w_1+w_2+ ... +w_k}{k}$$
	+ Given two documents, we can then compute their document vectors d1 and d2, and estimate the similarity between the two documents by cos(d1,d2). Document similarity is also useful for all sorts of applications; information retrieval, plagiarism detection, news recommender systems, and even for digital humanities tasks like comparing different versions of a text to see which are similar to each other
	+ Either the PPMI model or the tf-idf model can be used to compute word similarity, for tasks like finding word paraphrases, tracking changes in word meaning, or automatically discovering meanings of words in different corpora. For example, we can find the 10 most similar words to any target word w by computing the cosines between w and each of the V −1 other words, sorting, and looking at the top 10.
+ **Word2vec**
	+ long vector with dimensions corresponding to words in the vocabulary or documents in a collection.
	+ **embeddings**, short dense vectors.
	+ embeddings are short, with number of dimensions d ranging from 50-1000, rather than the much larger vocabulary size |V| or number of documents D we’ve seen.
	+ instead of vector entries being sparse, mostly-zero counts or functions of counts, the values will be real-valued numbers that can be negative.
	+ Representing words as 300-dimensional dense vectors requires our classifiers to learn far fewer weights than if we represented words as 50,000-dimensional vectors, and the smaller parameter space possibly helps with generalization and avoiding overfitting.
	+ Dense vectors may also do a better job of capturing synonymy.
	+ **skip-gram**
	+ The word2vec methods are fast, efficient to train, and easily available online with code and pretrained embeddings.
	+ Word2vec embeddings are **static embeddings**, meaning that the method learns one fixed embedding for each word in the static embeddings vocabulary.
	+ The intuition of word2vec is that instead of counting how often each word w occurs near, say, apricot, we’ll instead train a classifier on a binary prediction task: “Is word w likely to show up near apricot?” We don’t actually care about this prediction task; instead we’ll take the learned classifier weights as the word embeddings. The revolutionary intuition here is that we can just use running text as implici
	+ The intuition of skip-gram is:
		+ Treat the target word and a neighboring context word as positive examples.
		+ Randomly sample other words in the lexicon to get negative samples.
		+ Use logistic regression to train a classifier to distinguish those two cases.
		+ Use the learned weights as the embeddings.
	+ **The classifier**
	+ ![[Pasted image 20240325212647.png]]
	+ window size  +-2
	+ Our goal is to train a classifier such that, given a tuple (w, c) of a target word w paired with a candidate context word c (for example (apricot, jam), or perhaps (apricot, aardvark)) it will return the probability that c is a real context word (true for jam, false for aardvark).
	+ How does the classifier compute the probability P?
		+ a word is likely to occur near the target if its embedding vector is similar to the target embedding.
		+ two vectors are similar if they have a high dot product.
		+ The dot product c · w is not a probability, it’s just a number ranging from −∞ to ∞.
		+ To turn the dot product into a probability, we’ll use the logistic or sigmoid function σ(x).
		+ $$ P(+|w,c)=σ(c*w)=\frac{1}{1+e^{-c*w}}$$
		+ sigmoid gives us the probability for one word, but there are many context words in the window. Skip-gram makes the simplifying assumption that all context words are independent, allowing us to just multiply their probabilities:
		+ ![[Pasted image 20240325213618.png]]
		+ Skip-gram actually stores two embeddings for each word, one for the word as a target, and one for the word considered as context. Thus the parameters we need to learn are two matrices W and C, each containing an embedding for every one of the |V| words in the vocabulary V.
		+ ![[Pasted image 20240325214035.png]]
		+ **Learning skip-gram embeddings**
		+ It begins by assigning a random embedding vector for each of the N vocabulary words, and then proceeds to iteratively shift the embedding of each word w to be more like the embeddings of words that occur nearby in texts, and less like the embeddings of words that don’t occur nearby.
		+ ![[Pasted image 20240325214515.png]]
		+ For training a binary classifier we also need negative examples. In fact skipgram with negative sampling (SGNS) uses more negative examples than positive examples (with the ratio between them set by a parameter k).
		+ So for each of these (w, cpos) training instances we’ll create k negative samples, each consisting of the target w plus a ‘noise word’ cneg.A noise word is a random word from the lexicon, constrained not to be the target word w.
		+ The noise words are chosen according to their weighted unigram frequency pα(w), where α is a weight. If we were sampling according to unweighted frequency p(w), it would mean that with unigram probability p(“the”) we would choose the word the as a noise word, with unigram probability p(“aardvark”) we would choose aardvark, and so on.
		+ the goal of the learning algorithm is to adjust those embeddings to:
			+ • Maximize the similarity of the target word, context word pairs (w, cpos) drawn from the positive examples
			+ Minimize the similarity of the (w, cneg) pairs from the negative examples.
			+ ![[Pasted image 20240325215433.png]]
			+ here the first term expresses that we want the classifier to assign the real context word cpos a high probability of being a neighbor, and the second term expresses that we want to assign each of the noise words cnegi a high probability of being a non-neighbor, all multiplied because we assume independence.
			+ That is, we want to maximize the dot product of the word with the actual context words, and minimize the dot products of the word with the k negative sampled nonneighbor words.
			+ Shorter context windows tend to lead to representations that are a bit more syntactic, since the information is coming from immediately nearby words.
			+ When vectors are computed from long context windows, the highest cosine words to a target word w tend to be words that are topically related but not similar.
			+ Two words have  **first-order co-occurrence** (sometimes called syntagmatic association) if they are typically nearby each other.
			+ Two words have second-order co-occurrence (sometimes called paradigmatic association) if they have similar neighbors.
			+ **parallelogram model**: Another semantic property of embeddings is their ability to capture relational meanings.the parallelogram model parallelogram model for solving simple analogy problems of the form a is to b as a* is to what?.pple is to tree as grape is to ____ , and must fill in the word vine.
			+ ![[Pasted image 20240325225937.png]]
			+ 