# Classification and Bayesian Learning in Machine Learning

## 1. Introduction to Classification

Classification is a fundamental task in machine learning that involves predicting a categorical label for a given input instance. It's a supervised learning technique where the algorithm learns from labeled training data to make predictions on new, unseen data.

### What is Classification?

At its core, classification aims to construct a prediction rule $f: X \rightarrow Y$ where:

- $X$ represents the input feature space
- $Y$ represents the set of possible class labels

The goal is to learn this mapping function from labeled examples so that we can accurately predict the class of new instances.

### Importance in Machine Learning

Classification is crucial in various applications:

- Email spam filtering
- Disease diagnosis from medical images
- Credit risk assessment
- Sentiment analysis
- Object recognition in computer vision
- Fraud detection in financial transactions

### Real-world Example

Consider a medical diagnosis system where:

- Input features ($X$) could be patient data like brain scans
- Output labels ($Y$) could be stress levels: High, Moderate, or Low

## 2. Types of Classification

### Binary Classification

Binary classification involves categorizing instances into one of two possible classes.

**Example**: In stress detection:

- Stress (positive class)
- No Stress (negative class)

A classifier might use the average brain activity in the amygdala as a feature to determine if a person is experiencing stress or not.

### Multi-class Classification

Multi-class classification categorizes instances into one of three or more classes.

**Example**: Classifying stress levels as:

- High Stress
- Moderate Stress
- Low Stress

### Multi-label Classification

Multi-label classification assigns multiple labels to a single instance.

**Example**: A medical diagnosis system might classify a patient as having:

- Stress
- Anxiety
- Sleep disorder

## 3. Discriminative vs. Generative Classifiers

Classification approaches can be broadly divided into two categories: discriminative and generative.

### Discriminative Classifiers

Discriminative models learn the boundary between classes directly. They model $P(Y|X)$ - the probability of a class given the features.

**Key characteristics**:

- Focus on finding decision boundaries to separate classes
- Learn mappings directly from inputs to class labels
- Typically perform well with limited training data
- Examples: Logistic Regression, Decision Trees, Neural Networks, Support Vector Machines

Discriminative classifiers ask: **"How do I separate the classes?"**

### Generative Classifiers

Generative models learn the distribution of features within each class. They model $P(X,Y)$ or $P(X|Y)$ - the joint probability or the probability of features given the class.

**Key characteristics**:

- Model how the data was generated
- Learn what data for each class "looks like"
- Can generate new samples from the learned distribution
- Examples: Naive Bayes, Bayesian Networks, Hidden Markov Models, Generative Adversarial Networks

Generative classifiers ask: **"What does each class look like?"**

### Visual Comparison

Discriminative approaches focus on finding a decision boundary (like a line or hyperplane) that separates classes, while generative approaches model the distribution of data points within each class (often represented as probability densities).
![[Pasted image 20250320164835.png]]

## 4. Probability Basics

### Random Variables

A random variable is a value assigned to every outcome of an experiment.

**Example**:

- When rolling a die, the random variable could be the number that appears (1-6)

### Sample Space

A sample space is the set of all possible outcomes of a random experiment.

**Example**:

- For a coin toss, the sample space $S = {Head, Tail}$

### Probability

Probability measures the likelihood that an event will occur in a random experiment.

**Properties**:

- Probabilities are always between 0 and 1 inclusive: $0 \leq P(X) \leq 1$
- The sum of probabilities of all possible outcomes equals 1

**Example**:

- For a fair coin toss: $P(Head) = P(Tail) = 1/2$

## 5. Conditional Probability

### Definition

Conditional probability is the probability of an event occurring, given that another event has already occurred.

**Formula**: $$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

where:

- $P(A|B)$ is the probability of event A occurring given that B has occurred
- $P(A \cap B)$ is the joint probability of both A and B occurring
- $P(B)$ is the probability of event B occurring (and must be greater than 0)

### Example

If we know a patient has a positive test result, what's the probability they have the disease?

$P(\text{Disease}|\text{Positive Test})$ depends on:

- The accuracy of the test
- The prevalence of the disease in the population

## 6. Joint and Marginal Probabilities

### Joint Probability

Joint probability is the probability of two events happening together.

**Formula**: $$P(A,B) = P(A \cap B)$$

### Marginal Probability

Marginal probability is the probability of an event regardless of the outcome of another variable.

**Formula**: $$P(A) = \sum_b P(A,b)$$

## 7. Fundamental Rules of Probability

### Product Rule

The product rule relates joint and conditional probabilities:

$$P(A \cap B) = P(B|A)P(A) = P(A|B)P(B)$$

### Sum Rule

The sum rule for calculating the probability of either event occurring:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

The last term prevents double-counting events that are in both A and B.

### Theorem of Total Probability

If events $A_1, A_2, ..., A_n$ are mutually exclusive and their union is the entire sample space, then for any event B:

$$P(B) = \sum_{i=1}^{n} P(B|A_i)P(A_i)$$

## 8. Independent and Conditional Independence

### Independent Events

Two events A and B are independent if the occurrence of one does not affect the probability of the other.

**Mathematically**: $$P(A \cap B) = P(A) \times P(B)$$

Or equivalently: $$P(A|B) = P(A)$$

### Conditional Independence

Events A and B are conditionally independent given event C if:

$$P(A \cap B|C) = P(A|C) \times P(B|C)$$

This means that once we know C has occurred, information about whether B occurs does not change the probability of A occurring.

## 9. Bayes' Rule

### Formula

Bayes' rule is a fundamental theorem that relates conditional probabilities:

$$P(A|B) = \frac{P(B|A)P(A)}{P(B)}$$

Where:

- $P(A|B)$ is the posterior probability
- $P(B|A)$ is the likelihood
- $P(A)$ is the prior probability
- $P(B)$ is the evidence or normalization term

### Interpretation

Bayes' rule allows us to update our beliefs about an event A after observing evidence B:

- Prior: What we believe before seeing the evidence
- Likelihood: How probable the evidence is given our hypothesis
- Posterior: Our updated belief after seeing the evidence

### Application

In a disease diagnosis scenario:

- Prior: Prevalence of disease in population ($P(\text{Disease})$)
- Likelihood: Probability of positive test given disease ($P(\text{Positive}|\text{Disease})$)
- Evidence: Overall frequency of positive tests
- Posterior: Probability of disease given positive test ($P(\text{Disease}|\text{Positive})$)

## 10. Bayesian Classification

### Concept

Bayesian classification uses Bayes' rule to predict the most likely class for a given input:

$$f(X) = \arg\max_y P(Y=y|X)$$

Using Bayes' rule:

$$f(X) = \arg\max_y \frac{P(X|Y=y)P(Y=y)}{P(X)}$$

Since $P(X)$ is constant for all classes, we can simplify:

$$f(X) = \arg\max_y P(X|Y=y)P(Y=y)$$

Where:

- $P(X|Y=y)$ is the class conditional distribution of features
- $P(Y=y)$ is the prior distribution of class y

## 11. Maximum a Posteriori (MAP) Estimation

### Definition

MAP estimation is a method for estimating the most likely value of an unobserved quantity based on observed data:

$$y^* = \arg\max_{y \in Y} P(y|x)$$

Using Bayes' rule:

$$y^* = \arg\max_{y \in Y} \frac{P(x|y)P(y)}{P(x)} = \arg\max_{y \in Y} P(x|y)P(y)$$

### Example: Cancer Test

Consider a cancer screening test:

- The test is 98% accurate for true positives
- The test is 97% accurate for true negatives
- Only 0.1% (0.001) of the population has this cancer

If a patient receives a positive test result, what's the probability they have cancer?

Using Bayes' rule: $$P(\text{cancer}|\text{positive}) = \frac{P(\text{positive}|\text{cancer}) \times P(\text{cancer})}{P(\text{positive})}$$

$$= \frac{0.98 \times 0.001}{P(\text{positive}|\text{cancer})P(\text{cancer}) + P(\text{positive}|\neg\text{cancer})P(\neg\text{cancer})}$$

$$= \frac{0.00098}{0.98 \times 0.001 + 0.03 \times 0.999} \approx 0.032$$

Despite the positive test, there's only about a 3.2% chance the patient has cancer.

## 12. The Monty Hall Problem

### Problem Statement

The Monty Hall problem is a famous probability puzzle:

1. There are three doors, behind one is a car and behind the other two are goats
2. You choose one door (say door A)
3. The host, who knows what's behind each door, opens one of the other doors (say door B) to reveal a goat
4. The host gives you the option to either stick with your original choice or switch to the remaining door (door C)

### Solution Using Bayes' Rule

Let's analyze using Bayes' theorem. The question is: What is $P(\text{Car at C}|\text{Host opens B})$?

For the three doors, the initial probabilities are:

- $P(\text{Car at A}) = 1/3$
- $P(\text{Car at B}) = 1/3$
- $P(\text{Car at C}) = 1/3$

The probability that the host opens door B given the car locations:

- $P(\text{Host opens B}|\text{Car at A}) = 1/2$ (host can open either B or C)
- $P(\text{Host opens B}|\text{Car at B}) = 0$ (host never reveals the car)
- $P(\text{Host opens B}|\text{Car at C}) = 1$ (host must open B)

Using Bayes' rule:

$$P(\text{Car at C}|\text{Host opens B}) = \frac{P(\text{Host opens B}|\text{Car at C}) \times P(\text{Car at C})}{P(\text{Host opens B})}$$

$$= \frac{1 \times 1/3}{(1/2 \times 1/3) + (0 \times 1/3) + (1 \times 1/3)} = \frac{1/3}{1/6 + 0 + 1/3} = \frac{1/3}{1/2} = \frac{2}{3}$$

Therefore, switching doors gives you a 2/3 probability of winning, while staying with the original door gives only 1/3.

## 13. Naive Bayes Classifier

### The "Naive" Assumption

The Naive Bayes classifier is based on Bayes' theorem with a strong (naive) independence assumption: features are conditionally independent given the class.

Mathematically, if $X = (x_1, x_2, ..., x_n)$ is a feature vector, then:

$$P(X|Y) = \prod_{i=1}^{n} P(x_i|Y)$$

### Algorithm

The Naive Bayes classification rule is:

$$f_{NB}(x) = \arg\max_y P(Y=y) \prod_{i=1}^{n} P(x_i|Y=y)$$

Where:

- $P(Y=y)$ is the prior probability of class y
- $P(x_i|Y=y)$ is the probability of feature $x_i$ given class y

### Conditional Independence Visualization

For example, in a medical diagnosis system, symptoms like runny nose, sinus pressure, cough, fever, and muscle ache are all conditionally independent given the disease (e.g., flu).

## 14. Text Classification using Naive Bayes

### Applications

Text classification is widely used for:

- Spam detection
- Sentiment analysis
- Topic categorization
- Language identification
- Author identification
- Age/gender identification

### Bag of Words Model

The Bag of Words model represents text as an unordered collection of words, disregarding grammar and word order but keeping multiplicity.

### Classification Process

For document classification using Naive Bayes:

$$c_{MAP} = \arg\max_c P(c|d)$$

Using Bayes' rule:

$$= \arg\max_c \frac{P(d|c)P(c)}{P(d)}$$

Since $P(d)$ is constant for all classes:

$$= \arg\max_c P(d|c)P(c)$$

Under the Naive Bayes assumption, a document is represented as a collection of words $(x_1, x_2, ..., x_n)$:

$$= \arg\max_c P(c) \prod_{i=1}^{n} P(x_i|c)$$

## 15. Parameter Estimation in Naive Bayes

### Maximum Likelihood Estimation

For a Naive Bayes model, we need to estimate:

1. The prior probabilities of each class $P(c_j)$
2. The conditional probabilities of each feature given each class $P(x_i|c_j)$

For text classification, the conditional probability of a word given a class is:

$$\hat{P}(w_i|c_j) = \frac{\text{count}(w_i, c_j)}{\sum_{w \in V} \text{count}(w, c_j)}$$

This is the fraction of times word $w_i$ appears among all words in documents of class $c_j$.

### Zero Probability Problem

If a word $w$ never appears in the training documents for a class $c$, then $P(w|c) = 0$. This is problematic because:

1. It might be due to limited training data, not impossibility
2. In the Naive Bayes equation, this zero will make the entire probability zero

### Laplace (Add-One) Smoothing

To solve the zero probability problem, we use Laplace smoothing:

$$\hat{P}(w_i|c) = \frac{\text{count}(w_i, c) + 1}{\sum_{w \in V} \text{count}(w, c) + |V|}$$

Where $|V|$ is the size of the vocabulary.

This ensures no probability is ever exactly zero.

## 16. Naive Bayes Example: Weather Dataset

### Training Data

For a "Play Tennis" dataset with features: Outlook, Temperature, Humidity, and Wind, and the class label "Play" (Yes/No), we calculate:

- $P(Play=Yes) = 9/14$
- $P(Play=No) = 5/14$

And conditional probabilities like:

- $P(Outlook=Sunny|Play=Yes) = 2/9$
- $P(Outlook=Sunny|Play=No) = 3/5$

### Classification Example

For a new day with Outlook=Sunny, Temperature=Cool, Humidity=High, Wind=Strong:

$$P(Yes|x') = P(Sunny|Yes) \times P(Cool|Yes) \times P(High|Yes) \times P(Strong|Yes) \times P(Yes)$$ $$= 2/9 \times 3/9 \times 3/9 \times 3/9 \times 9/14 \approx 0.0053$$

$$P(No|x') = P(Sunny|No) \times P(Cool|No) \times P(High|No) \times P(Strong|No) \times P(No)$$ $$= 3/5 \times 1/5 \times 4/5 \times 3/5 \times 5/14 \approx 0.0206$$

Since $P(No|x') > P(Yes|x')$, we classify this day as "No" for playing tennis.

## 17. Naive Bayes Summary

### Advantages

- Very fast training and prediction
- Low storage requirements
- Robust to irrelevant features
- Performs well with many equally important features
- Optimal if independence assumptions hold
- Good baseline for text classification

### Limitations

- The "naive" conditional independence assumption rarely holds in real-world data
- Can be outperformed by more sophisticated models
- Not ideal for numeric features without proper discretization
- May give poor probability estimates (though class rankings can still be useful)

### When to Use Naive Bayes

- Text classification (spam filtering, sentiment analysis)
- When training data is limited
- When features are indeed relatively independent
- As a quick baseline before trying more complex models
- When computational resources are limited