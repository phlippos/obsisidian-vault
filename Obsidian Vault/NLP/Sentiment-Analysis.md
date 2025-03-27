**Sentiment Analysis** is the process of ‘computationally’ determining whether a piece of writing is positive, negative or neutral. It’s also known as **opinion mining**, deriving the opinion or attitude of a speaker.


**VADER Sentiment Analysis :**
**VADER (Valence Aware Dictionary and sEntiment Reasoner)** is a lexicon and rule-based sentiment analysis tool that is specifically attuned to sentiments expressed in social media. **VADER** uses a combination of A sentiment lexicon is a list of lexical features (e.g., words) which are generally labeled according to their semantic orientation as either positive or negative. **VADER** not only tells about the Positivity and Negativity score but also tells us about how positive or negative a sentiment is.

![[Pasted image 20240407223452.png]]

The Compound score is a metric that calculates the sum of all the lexicon ratings which have been normalized between -1(most extreme negative) and +1 (most extreme positive).

positive sentiment : (compound score >= 0.05)  neutral sentiment : (compound score > -0.05) and (compound score < 0.05)   
negative sentiment : (compound score <= -0.05)