**Named entitiy**: named entity for, roughly speaking, anything that can be referred to with a proper name: a person, a location, an organization.

**Parts Of Speech**:Parts of speech (also known as POS) and named entities are useful clues to sentence structure and meaning.. Knowing whether a word is a noun or a verb tells us about likely neighboring words and syntactic structure (verbs have dependency links to nouns),making part-of-speech tagging a key aspect of parsing. Knowing if a named entity like Washington is a name of a person, a place, or a university is important to many natural language processing tasks like question answering, stance detection, or information extraction

**Sequence labeling**:we assign, to each word xi in an input word sequence, a label yi , so that the output sequence Y has the same length as the input sequence X are called sequence labeling tasks.

**English Word Classes**
![[Pasted image 20240411221236.png]]
**Function Word**:Closed class words are generally function words like of, it, and, or you, which tend to be very short, occur frequently, and often have structuring uses in grammar.

### **Noun**
>**Nouns** are words for people, places, or things, but include others as well. **Common nouns** include concrete terms like cat and mango, abstractions like algorithm and beauty, and verb-like terms like pacing as in His pacing to and fro became quite annoying. Nouns in English can occur with determiners (a goat, this bandwidth) take possessives (IBM’s annual revenue), and may occur in the plural (goats, abaci).
>
>Many languages, including English, divide common nouns into **count nouns** and **mass noun**. **Count nouns** can occur in the **singular and plural** (goat/goats, relationship/relationships) and can be **counted** (one goat, two goats). **Mass nouns** are used when something is **conceptualized** as a homogeneous group. So snow, salt, and proper noun communism are **not counted** .
>
>**Proper nouns** like Regina, Colorado, and IBM, are names of specific persons or entities.
>
>**Adverb**: Adverbs generally modify something (often verbs, hence the name “adverb”, but also other adverbs and entire verb phrases).
>
>**Directional adverbs or locative adverbs**(home, here, downhill) specify the direction or location of some action
>
>**degree adverbs** (extremely, very, somewhat) specify the extent of some action, process, or manner property.
>
>**manner adverbs** (slowly, slinkily, delicately) describe the manner of some action or process.
>
>**temporal adverbs** describe the time that some action or event took place (yesterday, Monday).

![[Pasted image 20240411233028.png]]

### **Part-Of-Speech-Tagging**
>Part-of-speech tagging is the process of assigning a part-of-speech to each word in
>a text. The input is a sequence x1, x2,..., xn of (tokenized) words and a tagset, and the output is a sequence y1, y2,..., yn of tags, each output yi corresponding exactly to one input xi
>
>Tagging is a **disambiguation** task; words are **ambiguous** —have more than one possible part-of-speech—and the goal is to find the correct tag for the situation.
>
>For example, book can be a verb (book that flight) or a noun (hand me that book). That can be a determiner (Does that flight serve dinner) or a complementizer (I thought that your flight was earlier).
>
>The goal of **POS-tagging** is to resolve these **ambiguity** resolution ambiguities, choosing the proper tag for the context.
>
>Nonetheless, many words are easy to disambiguate, because their different tags aren’t equally likely. For example, a can be a determiner or the letter a, but the determiner sense is much more likely.
>
>This idea suggests a useful baseline: given an ambiguous word, choose the tag which is most frequent in the training corpus.


### **Named Entities and Named Entity Tagging**
>being a proper noun is a grammatical property of these words. But viewed from a semantic perspective, these proper nouns refer to different kinds of entities: Janet is a person, Stanford University is an organization, and Colorado is a location.
>
>A **named entity** is, roughly speaking, anything that can be referred to with a proper name: a person, a location, an organization.
>
>The task of **named entity recognition (NER)** is to find spans(aralık) of text that constitute(oluşturmak) proper names and tag the type of the entity.
>
>Four entity tags are most common: **PER (person), LOC (location), ORG (organization), or GPE (geo-political entity)**. However, the term named entity is commonly extended to include things that aren’t entities per se, including dates, times, and other kinds of temporal expressions, and even numerical expressions like prices.
>
>**named entity tagging** is also central to tasks involving building semantic representations, like extracting events and the relationship between participants.
>
>Unlike part-of-speech tagging, where there is no segmentation problem since each word gets one tag, the task of named entity recognition is to find and label spans of text, and is difficult partly because of the ambiguity of segmentation; we need to decide what’s an entity and what isn’t, and where the boundaries are.
>
>Indeed, most words in a text will not be named entities. Another difficulty is caused by type ambiguity. The mention JFK can refer to a person, the airport in New York, or any number of schools, bridges, and streets around the United States. 
>
>**BIO**
>
>In BIO tagging we label any token that begins a span of interest with the label B, tokens that occur inside a span are tagged with an I, and any tokens outside of any span of interest are labeled O. While there is only one O tag, we’ll have distinct B and I tags for each named entity class. BIO has the advantage that we can represent the task in the same simple sequence modeling way as part-of-speech tagging: assigning a single label yi to each input word xi :![[Pasted image 20240411235920.png]]
>IO tagging, which loses some information by eliminating the B tag, and BIOES tagging, which adds an end tag E for the end of a span, and a span tag S for a span consisting of only one word.
>
>**HMM Part-of-Speech Tagging**
>the Hidden Markov Model
>
>sequence labeler is a model whose job is to assign a label to each unit in a sequence, thus mapping a sequence of observations to a sequence of labels of the same length.
>
>An HMM is a probabilistic sequence model: given a sequence of units (words, letters, morphemes, sentences, whatever), it computes a probability distribution over possible sequences of labels and chooses the best label sequence.
>**Markov Chains**
>A Markov chain is a model that tells us something about the probabilities of sequences of random variables, states, each of which can take on values from some set.
>These sets can be words, or tags, or symbols representing anything, for example the weather. A Markov chain makes a very strong assumption that **if we want to predict the future in the sequence, all that matters is the current state. All the states before the current state have no impact on the future except via the current state.** It’s as if to predict tomorrow’s weather you could examine today’s weather but you **weren’t allowed** to look at yesterday’s weather.
>
>![[Pasted image 20240412002250.png]]
>**Markov Assumption**: A Markov model embodies the Markov assumption on the probabilities of this sequence: that when predicting the future, the past doesn’t matter, only the present.
>$$P(q_i=a|q_1,...,q_{i-1}) = P(q_i=a|q_{i-1})$$
>Markov chain for assigning a probability to a sequence of weather events, for which the vocabulary consists of HOT, COLD, and WARM. The states are represented as nodes in the graph, and the transitions, with their probabilities, as edges. The transitions are probabilities: the values of arcs leaving a given state must sum to 1.
>![[Pasted image 20240412003214.png]]
>**The hidden Markov Model**
>In many cases, however, the events we are interested in are hidden: we don’t observe them directly. For example we don’t normally observe part-of-speech tags in a text. Rather, we see words, and must infer the tags from the word sequence. We call the tags hidden because they are not observed.
>
>A **hidden Markov model (HMM)** allows us to talk about both observed events(like words that we see in the input) and hidden events (like part-of-speech tags) that we think of as causal factors in our probabilistic model.
>![[Pasted image 20240412004612.png]]
>Second, the probability of an output observation oi depends only on the state that produced the observation qi and not on any other states or any other observations
>$$ P(o_i|q_1...q_i,...q_T,o_1,...o_i,...,o_T)= P(o_i|q_i)$$
>Imagine that you are a climatologist in the year 2799 studying the history of global warming. You cannot find any records of the weather in Baltimore, Maryland, for the summer of 2020, but you do find Jason Eisner’s diary, which lists how many ice creams Jason ate every day that summer. Our goal is to use these observations to estimate the temperature every day. We’ll simplify this weather task by assuming there are only two kinds of days: cold (C) and hot (H). So the Eisner task is as follows:
>	Given a sequence of observations O (each an integer representing the number of ice creams eaten on a given day) find the ‘hidden’ sequence Q of weather states (H or C) which caused Jason to eat the ice cream.
>	![[Pasted image 20240412005142.png]]
>	![[Pasted image 20240412005303.png]]
>	

#### **HMM tagging as decoding**
>For any model, such as an HMM, that contains hidden variables, the task of determining the hidden variables sequence corresponding to the sequence of observations decoding is called decoding.
>![[Pasted image 20240501235459.png]]
>For part-of-speech tagging, the goal of HMM decoding is to choose the tag sequence t1 ...tn that is most probable given the observation sequence of n words w1 ...wn:
>![[Pasted image 20240502000145.png]]
#### **Viterbi Algorithm**
>The Viterbi algorithm is a dynamic programming algorithm for finding the most likely sequence of hidden states—called the Viterbi path—that results in a sequence of observed events, especially in the context of Markov information sources and hidden Markov models (HMM).
>	Algorithm : 
>		1. **Initialization**: Start by setting up a matrix where each cell represents the probability of the most likely path that ends in state 𝑖i at time 𝑡t. Initialize the first column of this matrix based on the initial state probabilities and the emission probabilities of the first observation.
>		2. **Recursion**: For each subsequent observation and each possible state:
>			- Calculate the probability for each path reaching state 𝑗j at time 𝑡t by considering all possible previous states at time 𝑡−1t−1. Multiply the probability of the most likely path ending in these previous states by the transition probability from these states to state 𝑗j, and then by the emission probability of the observed event at state 𝑗j.
>			- Select the path with the highest probability as the most likely path leading to state 𝑗j at time 𝑡t. Store this probability in the matrix.
>			- Optionally, keep track of the path itself using back-pointers which record the state at 𝑡−1t−1 that resulted in the highest probability for each state at time 𝑡t.
>		 3. **Termination**: After all observations have been processed, the cell in the last column with the highest probability will indicate the last state of the most likely path.
>		 4. **Path backtracking**: By following the back-pointers from the state identified in the termination step back to the start, you can reconstruct the most likely sequence of states (the Viterbi path)
>it allows these calculations to be made in a time proportional to 𝑇×𝑁^2 and space proportional to 𝑇×𝑁, where 𝑇 is the length of the observed sequence and 𝑁 is the number of states in the model.
>![[Pasted image 20240502002730.png]]
>![[Pasted image 20240502003015.png]]
>![[Pasted image 20240502003318.png]]

#### **Conditional random Fields**
>in POS tagging as in other tasks, we often run into unknown words: proper names and acronyms unknown words are created very often, and even new common nouns and verbs enter the language at a surprising rate. It would be great to have ways to add arbitrary features to help with this, perhaps based on capitalization or morphology (words starting with capital letters are likely to be proper nouns, words ending with -ed tend to be past tense (VBD or VBN), etc.) Or knowing the previous or following words might be a useful feature (if the previous word is the, the current tag is unlikely to be a verb).
>Although we could try to hack the HMM to find ways to incorporate some of these, in general it’s hard for generative models like HMMs to add arbitrary features directly into the model in a clean way.
>