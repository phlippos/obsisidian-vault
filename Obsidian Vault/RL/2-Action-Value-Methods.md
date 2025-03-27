![[Pasted image 20240807183038.png]]![[Pasted image 20240807183050.png]]
![[Pasted image 20240807183107.png]]![[Pasted image 20240807183119.png]]![[Pasted image 20240807183135.png]]
The action-value methods we have discussed so far all estimate action values as sample averages of observed rewards. The obvious implementation is to maintain, for each action a, a record of all the rewards that have followed the selection of that action. Then, when the estimate of the value of action a is needed at time t where here R1, . . . , RNt(a) are all the rewards received following all selections of action a prior to play t. A problem with this straightforward implementation is that its memory and computational requirements grow over time without bound. That is, each additional reward following a selection of action a requires more memory to store it and results in more computation being required to determine Qt(a)
### Incremental Implementation
![[Pasted image 20240819170947.png]]
![[Pasted image 20240819171001.png]]
### Tracking a nonstationary Problem
The key idea here is to modify the update rule to give more weight to recent rewards, which is particularly useful in non-stationary environments where the reward distribution might change over time. This method uses a **constant step-size parameter** α\alphaα to control the degree of this weighting.
![[Pasted image 20240819171711.png]] - α is the step-size parameter, where 0<α≤10 
- The parameter α\alphaα determines how quickly the algorithm adapts to new information. A larger α\alphaα means more weight is given to recent rewards, making the estimate more responsive to changes.
### Optimistic Initial Values
Sometimes it is convenient to vary the step-size parameter from step to step. Let αk(a) denote the step-size parameter used to process the reward received after the kth selection of action a. As we have noted, the choice αk(a) = 1 k results in the sample-average method, which is guaranteed to converge to the true action values by the law of large numbers. But of course convergence is not guaranteed for all choices of the sequence {αk(a)}. A wellknown result in stochastic approximation theory gives us the conditions required to assure convergence with probability 1:
![[Pasted image 20240819172919.png]]
- First condition 
	- - This condition ensures that the sum of the step sizes over time is infinite. It means that, although the step sizes might decrease, they do so slowly enough to guarantee that the algorithm can eventually "overcome" any initial biases or fluctuations in the estimates. This is essential for the algorithm to explore sufficiently and adjust the estimates toward the true value.(Infinite Sum of Step Sizes): Ensures that the steps are large enough, on average, to make significant progress and not get stuck due to initial conditions or random noise.
- Second Condition
	- This condition ensures that the sum of the squares of the step sizes is finite. This guarantees that the step sizes decrease rapidly enough over time to stabilize and converge to a fixed value. If the step sizes did not decrease, the algorithm might continue to oscillate and never settle on an accurate estimate.(Finite Sum of Squared Step Sizes): Ensures that the steps are small enough, in the long run, to settle down and converge rather than continue fluctuating indefinitely.
	- ![[Pasted image 20240819173341.png]]
- ### Optimistic vs. Realistic Initial Estimates

- **Optimistic Initial Estimates (Black Line):** The initial action values Q1(a) are set to 5, which is significantly higher than the true expected reward values (mean = 0). This approach is paired with a greedy policy (ϵ=0), meaning the algorithm always selects the action with the highest estimated value.
    
- **Realistic Initial Estimates (Gray Line):** The initial action values Q1(a) are set to 0, which is a more realistic assumption. This is paired with an ϵ\epsilonϵ-greedy policy (ϵ=0.1), meaning the algorithm mostly chooses the best-known action but occasionally explores random actions to avoid local optima.

### Effect on Exploration and Learning

- **Exploration Encouragement:** The optimistic initial estimates encourage exploration. Since the initial value of 5 is overly optimistic, every action will likely yield a reward lower than 5. The algorithm, therefore, becomes "disappointed" with each action and continues exploring other actions until it finds one that seems satisfactory. This behavior ensures that all actions are explored multiple times, allowing the algorithm to gather more information about the true reward distribution.

- **Convergence to Optimal Action:** The graph shows that the optimistic initial estimates lead to a rapid increase in the percentage of optimal actions chosen as more steps are taken. Over time, this method eventually converges to the optimal action more effectively than the realistic initial estimates paired with an ϵ\epsilonϵ-greedy policy.

### Bias in Estimates

- **Bias in Constant Step-Size Methods:** The text mentions that for methods using a constant step-size parameter α, the initial bias from optimistic estimates does not disappear completely. However, this bias decreases over time as the algorithm continues to update the action-value estimates.

### Practical Implications

- **User-Defined Parameters:** The initial action values become parameters that the user can set based on prior knowledge or to encourage exploration. Setting these values requires some consideration, as they can influence the learning process.
- **Exploration Strategy:** Optimistic initial values are a simple and effective way to ensure sufficient exploration, especially in greedy policies that might otherwise exploit too soon and miss out on finding the best actions.
- ![[Pasted image 20240820185739.png]]
- ![[Pasted image 20240820185747.png]]
- ![[Pasted image 20240820185755.png]]
- We call this technique for encouraging exploration optimistic initial values. We regard it as a simple trick that can be quite effective on stationary problems, but it is far from being a generally useful approach to encouraging exploration. For example, it is not well suited to nonstationary problems because its drive for exploration is inherently temporary. If the task changes, creating a renewed need for exploration, this method cannot help.

### Upper-Confidence-Bound Action Selection
- is a popular action selection strategy in reinforcement learning, especially in multi-armed bandit problems. The core idea of UCB is to balance exploration and exploitation by selecting actions based not only on their estimated value (exploitation) but also on how uncertain or unexplored they are (exploration).
- ![[Pasted image 20240820191605.png]]
- ![[Pasted image 20240820191616.png]]
- However, UCB will continue to occasionally try other actions to ensure that it hasn't missed a potentially better option due to initial random fluctuations or limited data.
- ![[Pasted image 20240820191930.png]]
- s actions are selected more frequently, Nt(a)N_t(a)Nt​(a) increases, reducing the exploration term. The algorithm will gradually settle on Action C if it consistently provides higher rewards.
- Pros: 
	- **Efficient Exploration**: UCB intelligently balances exploration and exploitation without requiring a fixed exploration parameter like ϵ\epsilonϵ in ϵ\epsilonϵ-greedy strategies.
	- **No Need for Hyperparameter Tuning**: The exploration is naturally guided by the uncertainty in the estimates, reducing the need for extensive parameter tuning.
- Use Cases : 
	- **Multi-Armed Bandit Problems**: UCB is particularly well-suited for situations where actions correspond to different strategies or options (like different slot machines), and the goal is to maximize cumulative reward over time.
	- **Dynamic Environments**: UCB can adapt to changing environments by continuing to explore actions, ensuring that the chosen strategy remains optimal even as conditions change.

### Gradient bandits
- **Gradient Bandits** are a class of reinforcement learning algorithms that use gradient ascent to directly optimize the action selection probabilities based on the rewards received. This approach is particularly useful in settings where the goal is to maximize the average reward over time, rather than just the immediate reward.
- Action Preferences
	- Unlike other methods that estimate the value of actions (e.g., Qt(a), gradient bandits maintain a set of **preferences** Ht(a) for each action a.
	- These preferences are not directly interpretable as action values, but they are used to determine the probability of selecting each action.
- Action Probability
	- The probability of selecting action aaa at time ttt is given by a softmax function over the preferences.
	- ![[Pasted image 20240820202422.png]]
- Gradient Ascent
	- The algorithm updates the action preferences Ht(a) using gradient ascent on the expected reward:
	- ![[Pasted image 20240820202551.png]]
	- For the action at​ that was actually selected:
		- ![[Pasted image 20240820202624.png]]
	- For all other actions a≠at:
		- ![[Pasted image 20240820202709.png]]
	- 
	- The baseline reward Rˉt is typically the running average of the rewards received so far. It helps normalize the update and reduce variance in the gradient estimate, leading to more stable learning.
	- ![[Pasted image 20240820202939.png]]
	- ![[Pasted image 20240820203220.png]]