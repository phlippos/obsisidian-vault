#### N-gram Language Models
> Let’s begin with the task of computing P(w|h), the probability of a word w given some history h. Suppose the history h is “its water is so transparent that” and we want to know the probability that the next word is the:
> 			P(the|its water is so transparent that)
> One way to estimate this probability is from relative frequency counts: take a very large corpus, count the number of times we see its water is so transparent that, and count the number of times this is followed by the. This would be answering the question “Out of the times we saw the history h, how many times was it followed by the word w”, as follows:
> 
> P(the|its water is so transparent that) = C(its water is so transparent that the) / C(its water is so transparent that)
> 
> With a large enough corpus, such as the web, we can compute these counts and estimate the probability
> To represent the probability of a particular random variable Xi taking on the value “the”, or P(Xi = “the”), we will use the simplification P(the).
> The intuition of the n-gram model is that instead of computing the probability of a word given its entire history, we can approximate the history by just the last few words.
> The bigram model, for example, approximates the probability of a word given all the previous words P(wn|w1:n−1) by using only the conditional probability of the preceding word P(wn|wn−1). In other words, instead of computing the probability
> 				P(the|Walden Pond’s water is so transparent that)
>we approximate it with the probability 				P(the|that)
>We can generalize the bigram (which looks one word into the past) to the trigram (which looks two words into the past) and thus to the n-gram (which looks n−1 words into the past)
>N here to mean the n-gram size, so N = 2 means bigrams and N = 3 means trigrams.
>P(wn|w1:n−1) ≈ P(wn|wn−N+1:n−1)
>![[Pasted image 20240521162458.png]]
#### Evaluating Language Models : Training and Test Sets
>![[Pasted image 20240521164847.png]]
>



![[Pasted image 20240520094416.png]]
### RNN-Advantages
- Can process any length input 
-  Computation for step t can (in theory) use information from many steps back 
- Model size doesn’t increase for longer input context 
- Same weights applied on every timestep, so there is symmetry in how inputs are processed.
### RNN-Disadvantages
- Recurrent computation is slow 
- In practice, difficult to access information from many steps back
![[Pasted image 20240520095137.png]]
![[Pasted image 20240520102144.png]]
### Steps in Backpropagation Through Time (BPTT)

1. **Forward Pass**:
    
    - Compute the output for each time step.
    - Store the hidden states and outputs at each time step.
2. **Loss Calculation**:
    
    - Compute the loss at each time step.
    - Sum the losses to get the total loss over the sequence.
3. **Backward Pass**:
    
    - Compute the gradient of the loss with respect to the output at each time step.
    - Backpropagate the gradients through the network to update the weights.
    - Accumulate the gradients over time for each weight in the network.
4. **Weight Update**:
    
    - Use an optimization algorithm (e.g., SGD, Adam) to update the weights based on the accumulated gradients.

### Mathematical Formulation

For an RNN with a hidden state ℎ𝑡ht​, input 𝑥𝑡xt​, output 𝑦𝑡yt​, and weights 𝑊W and 𝑈U, the forward pass equations are:

ℎ𝑡=𝑓(𝑊⋅𝑥𝑡+𝑈⋅ℎ𝑡−1)ht​=f(W⋅xt​+U⋅ht−1​) 𝑦𝑡=𝑔(𝑉⋅ℎ𝑡)yt​=g(V⋅ht​)

where 𝑓f is the activation function (e.g., tanh or ReLU), and 𝑔g is the output function.

The loss 𝐿L at each time step 𝑡t is computed using a loss function (e.g., cross-entropy loss for classification tasks):

𝐿𝑡=loss(𝑦𝑡,target)Lt​=loss(yt​,target)

### Backward Pass
![[Pasted image 20240520100938.png]]
### One big Problem
- the more we unroll a rnn, the harder it is to train. (Vanishing/exploiding Gradient problem) 
- ![[Pasted image 20240520101427.png]]
- In other words, in order to find the parameter values that give us the lowest value for the loss, we usually want to take relatively small steps
- However the gradient contains a huge number, and we will end up taking relatively large steps.(if the weight > 1)
- if the weight is between 0 and 1 then we will take relatively very small step.
- ![[Pasted image 20240520104357.png]]
- ![[Pasted image 20240520104603.png]]

### Evaluation models
- **Perplexity** : Perplexity is a common metric used to evaluate language models, particularly in natural language processing tasks. It measures how well a probabilistic model predicts a sample and is often used for evaluating language models.
- Perplexity can be understood as the exponentiated average negative log-likelihood of the sequence. For a language model predicting a sequence of words, the perplexity is defined as:
- ![[Pasted image 20240521165138.png]]
- because of the inverse, the higher the probability of the word sequence, the lower the perplexity. Thus the lower the perplexity of a model on the data, the better the model, and minimizing perplexity is equivalent to maximizing the test set probability according to the language model.
- Since this sequence will cross many sentence boundaries, if our vocabulary includes a between-sentence token or separate begin- and end-sentence markers ~~and~~ then we can include them in the probability computation. If we do, then we also include one token per sentence in the total count of word tokens N.
- For example if we use both begin and end tokens, we would include the end-of-sentence marker but not the beginning-of-sentence marker  in our count of N; This is because the end-sentence token is followed directly by the begin-sentence token with probability almost 1, so we don’t want the probability of that fake transition to influence our perplexity
- - **Lower perplexity** indicates a better predictive performance of the language model. A model that assigns higher probabilities to the actual observed words will have lower perplexity.
- - **Higher perplexity** means the model is less certain about its predictions.
- **Weighted Average Branching Factor:**
	- The branching factor in the context of a probabilistic model can be thought of as the average number of choices available at each decision point. In terms of language models, this would correspond to the average number of possible next words given a context.The weighted average branching factor considers the probabilities of different outcomes. The perplexity can be interpreted as the effective branching factor of the model, weighted by the probabilities of the various choices.
	- ![[Pasted image 20240521185408.png]]
	- When applied to language models, perplexity gives a sense of how many different words the model considers likely at each step, on average. For instance, if a model has a perplexity of 10, it means that, on average, the model is as uncertain as if it had to choose between 10 equally probable words at each step.
	- ![[Pasted image 20240521185602.png]]
	- **Sampling sentences from a language model**
		- One important way to visualize what kind of knowledge a language model embodies sampling is to sample from it. Sampling from a distribution means to choose random points according to their likelihood. Thus sampling from a language model—which represents a distribution over sentences—means to generate some sentences, choosing each sentence according to its likelihood as defined by the model.
``` python
import random
import numpy as np

def sample_from_distribution(distribution):
    return np.random.choice(len(distribution), p=distribution)

def generate_sentence(model, initial_context, max_length=20):
    context = initial_context
    sentence = context.split()

    for _ in range(max_length - len(sentence)):
        # Predict the next word probabilities
        next_word_probabilities = model.predict_next_word(context)
        
        # Sample the next word
        next_word_index = sample_from_distribution(next_word_probabilities)
        next_word = model.vocabulary[next_word_index]
        
        # Append the next word to the context and sentence
        sentence.append(next_word)
        context = " ".join(sentence)
        
        # Optionally stop if an end-of-sentence token is generated
        if next_word == '<eos>':
            break

    return " ".join(sentence)

# Example usage
model = load_pretrained_language_model()
initial_context = "Once upon a time"
generated_sentence = generate_sentence(model, initial_context)
print(generated_sentence)
```

#### Smoothing
- What do we do with words that are in our vocabulary (they are not unknown words) but appear in a test set in an unseen context (for example they appear after a word they never appeared after in training)? To keep a language model from assigning zero probability to these unseen events, we’ll have to shave off a bit of probability mass from some more frequent events and give it to the events we’ve never seen. smoothing This modification is called smoothing or discounting.
- ##### Laplace Smoothing
	- The simplest way to do smoothing is to add one to all the n-gram counts, before we normalize them into probabilities. All the counts that used to be zero will now have a count of 1, the counts of 1 will be 2, and so on. This algorithm is called Laplace smoothing. Laplace smoothing does not perform well enough to be used in modern n-gram models
	- ![[Pasted image 20240521195625.png]]
	- The sharp change in counts and probabilities due to add-one smoothing (Laplace smoothing) happens because this method uniformly adds a fixed amount (usually 1) to the counts of all possible events, including those that were not observed in the training data. This can lead to significant shifts in the probabilities, especially when the original counts are large or when the number of possible events (vocabulary size) is large.
	- ![[Pasted image 20240521201032.png]]
	
- ##### Discounting
	-  It helps in redistributing some probability mass from observed events to unobserved events, which avoids assigning a zero probability to unseen events and smooths the probability distribution.
	- ###### Simple Discounting
		- Simple discounting reduces the probability of observed events by a fixed discount value and redistributes the remaining probability mass to unseen events. The formula is: $$ P_{discount}(x) = (c(x)-d)/N + d/V$$
- ##### Add-k smoothing
	- One alternative to add-one smoothing is to move a bit less of the probability mass from the seen to the unseen events. Instead of adding 1 to each count, we add a fractional count k (.5? .05? .01?). This algorithm is therefore called add-k smoothing.
	- ![[Pasted image 20240521202105.png]]
- ##### Backoff and interpolation
	- The discounting we have been discussing so far can help solve the problem of zero frequency n-grams. But there is an additional source of knowledge we can draw on. If we are trying to compute P(wn|wn−2wn−1) but we have no examples of a particular trigram wn−2wn−1wn, we can instead estimate its probability by using the bigram probability P(wn|wn−1). Similarly, if we don’t have counts to compute P(wn|wn−1), we can look to the unigram P(wn).
	- In other words, sometimes using less context is a good thing, helping to generalize more for contexts that the model hasn’t learned much about. There are two ways to use this n-gram “hierarchy”. In backoff, we use the trigram if the evidence is sufficient, otherwise we use the bigram, otherwise the unigram. In other words, we only “back off” to a lower-order n-gram if we have zero evidence for a higher-order n-gram. By contrast, in interpolation, we always mix the probability estimates from all the n-gram estimators, weighting and combining the trigram, bigram, and unigram counts.
	- In simple linear interpolation, we combine different order n-grams by linearly interpolating them. Thus, we estimate the trigram probability P(wn|wn−2wn−1) by mixing together the unigram, bigram, and trigram probabilities, each weighted by a λ:![[Pasted image 20240521202712.png]]
	- ![[Pasted image 20240521202846.png]]
	- <mark style="background: #FFF3A3A6;">In a backoff n-gram model, the idea is to use higher-order n-grams when they are available and reliable, and to back off to lower-order n-grams when higher-order n-grams have zero counts. </mark>To ensure that the model remains a proper probability distribution (where the total probability sums to 1). it's necessary to discount the higher-order n-grams. This reserved probability mass is then redistributed to the lower-order n-grams using a backoff function, denoted as 𝛼α. 
	- ![[Pasted image 20240521204523.png]]
	- ![[Pasted image 20240521204649.png]]
	- ![[Pasted image 20240522111814.png]]
	- ![[Pasted image 20240522111954.png]]
### Kneser-Ney Smoothing
- #### Absolute discounting
	- Consider an n-gram that has count 4. We need to discount this count by some amount. But how much should we discount it? Church and Gale’s clever idea was to look at a held-out corpus and just see what the count is for all those bigrams that had count 4 in the training set. They computed a bigram grammar from 22 million words of AP newswire and then checked the counts of each of these bigrams in another 22 million words. On average, a bigram that occurred 4 times in the first 22 million words occurred 3.23 times in the next 22 million words.
	- ![[Pasted image 20240522114302.png]]
	- Absolute discounting formalizes this intu- absolute discounting ition by subtracting a fixed (absolute) discount d from each count. The intuition is that since we have good estimates already for the very high counts, a small discount d won’t affect them much. It will mainly modify the smaller counts, for which we don’t necessarily trust the estimate anyway
	- ![[Pasted image 20240522114601.png]]
	- ![[Pasted image 20240522133108.png]]
### Learning Long-Term Dependencies with Gradient Descent is dificult
- Long-term dependencies refer to situations where a prediction at a particular time step depends on input received many time steps earlier. This is especially relevant in tasks such as sequence prediction, time series analysis, and natural language processing.
- #### Main Challenges
	- 1. **Vanishing Gradients**: When training deep neural networks or recurrent neural networks (RNNs), gradients of the loss function with respect to weights can become extremely small. As a result, the weight updates are negligible, causing the learning process to be extremely slow or even stall. This issue becomes more pronounced as the network depth or sequence length increases.
	- 1. **Exploding Gradients**: Conversely, gradients can also grow exponentially, causing the weight updates to be excessively large. This can lead to numerical instability and make the training process erratic.
- #### Impact and Solutions
	- **Long Short-Term Memory (LSTM)**: A type of RNN designed to handle long-term dependencies more effectively by incorporating mechanisms to preserve and regulate gradients.
	- **Gradient Clipping**: A technique to prevent exploding gradients by capping the gradients during training.
	- **Improved Initialization and Normalization**: Methods like careful weight initialization and batch normalization to maintain gradient stability.