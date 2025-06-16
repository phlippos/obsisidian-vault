
Instance Based Learning (Lazy Learning)

• Why it’s considered “lazy”:
	• No Training Phase: It doesn’t attempt to understand the underlying structure of the
	data during training.
	• Learning stage: given a training set D:[(x1 , y1), ..., (xm, ym)] do nothing
• Instance-Based Learning: The algorithm memorizes the entire training
	dataset, and when a prediction is needed, it looks up the most similar
	instances (neighbors) in the training data.
	• Classification stage: given an instance xq to classify find the training-set instance xi
	that is most similar to xq return the class value of yi
• No Generalization: Since no model is created during training, it doesn’t
generalize well to new, unseen data. Each prediction is based on the
specific instances in the training set.

## k-Nearest Neighborhood
### How k-NN Works:

1. **Learning stage**: Simply store all training examples
2. **Classification stage**:
    - Calculate distance between query point and all training examples
    - Find k nearest neighbors
    - Assign the most common class label from these neighbors

![[Pasted image 20250504135014.png]]
### Distance Metrics:

- **Euclidean distance**: Square root of sum of squared differences (common for continuous features)
- **Manhattan distance**: Sum of absolute differences
- **Minkowski distance**: Generalization of Euclidean and Manhattan
- **Hamming distance**: Counts features where instances differ (for categorical data)

k-NN: Inductive Bias
• Similar data points tend to have similar labels

1-NN Hypothesis Space
• Voronoi Diagram: Each polyhedron indicates the region of feature
space that is in the nearest neighborhood of each training instance


### Feature Normalization:

Feature scaling is crucial since distance-based algorithms are sensitive to feature magnitudes:

- **Min-Max normalization**: Scales features to [0,1] or [-1,1] range
- **Standardization**: Transforms data to have zero mean and unit variance
- ![[Pasted image 20250504135537.png]]
- ![[Pasted image 20250504135551.png]] 
# Normalization vs. Standardization in Data Preprocessing

When preparing data for machine learning algorithms, especially distance-based methods like k-NN, proper scaling is essential. Let me explain when to use each approach:

## Choosing Between Normalization and Standardization

<mark style="background: #FFB86CA6;">The decision between normalization and standardization depends on:</mark>

1. **Data distribution**:
    - **Normal distribution** → Use standardization
    - **Non-normal distribution** → Use normalization
2. **Value range magnitude**:
    - **Large ranges** (10s, 100s, 1000s) → Scaling needed
    - **Very small ranges** (0.01, 0.0001) → Scaling needed
    - **Already near 0-1 with limited distribution** → Minimal or no scaling may be acceptable
3. **Algorithm requirements**:
    - **Distance-based algorithms** (k-NN, k-means, SVM) → Very sensitive to scale
    - **Tree-based algorithms** (Decision Trees, Random Forests) → Less sensitive to scale
## Practical Advice

- **When uncertain**: Start with normalization as a default approach
- **Best practice**: Compare model performance with raw data, normalized data, and standardized data
- **Combined approach**: In some cases, standardizing first and then normalizing afterward can be beneficial
- **Consistency**: Apply the same scaling parameters to both training and test datasets

## Weighted k-NN
- Give more weight to the points which are nearby and less weight to the points which are farther away
- ![[Pasted image 20250504140244.png]]

# Edited k-NN: Enhancing Instance Selection

<mark style="background: #FFB86CA6;">Edited k-NN algorithms address one of the key limitations of traditional k-NN: the need to store all training instances. By intelligently selecting which instances to keep in memory, these techniques can:</mark>

1. Reduce memory requirements
2. Speed up classification
3. Remove redundant or noisy data points
4. Potentially improve classification accuracy

## Two Main Approaches

### Incremental Deletion

This is a pruning approach that starts with a comprehensive dataset and selectively removes redundant instances:

```
Algorithm: Incremental Deletion
1. Initialize memory with all training instances
2. For each training instance (xi, yi):
   a. Temporarily remove (xi, yi) from memory
   b. Classify (xi, yi) using the remaining instances
   c. If classification is correct:
      - Permanently delete (xi, yi) (redundant instance)
   d. Otherwise:
      - Keep (xi, yi) (essential for correct classification)
```

**Benefits:**

- Retains only necessary boundary instances
- Removes instances in the interior of class regions
- Reduces the dataset size while maintaining decision boundaries

### Incremental Growth

This is a constructive approach that starts with an empty set and selectively adds informative instances:

```
Algorithm: Incremental Growth
1. Initialize memory as empty
2. For each training instance (xi, yi):
   a. Classify (xi, yi) using current instances in memory
   b. If classification is incorrect:
      - Add (xi, yi) to memory (important for decision boundary)
   c. Otherwise:
      - Discard (xi, yi) (already well-represented)
```

**Benefits:**

- Builds a minimal set of critical instances
- Focuses on boundary cases that define the decision surface
- Often results in a much smaller set than the original

## Practical Considerations

- The order in which instances are processed can affect the final subset
- Multiple passes through the data may improve results
- The choice of k value affects which instances are retained
- The choice between deletion and growth approaches depends on:
    - Initial dataset size (deletion better for smaller datasets)
    - Noise level (growth better for noisy data)
    - Class distributions (growth better for imbalanced data)

# Choosing the Right k Value in k-NN

<mark style="background: #FFB86CA6;">The selection of k (number of neighbors) is one of the most important hyperparameters in k-NN and significantly affects performance. Here's a comprehensive guide to choosing an appropriate k value</mark>:

## Key Considerations for Selecting k

### 1. Use Odd Numbers

- **Why odd values?** To avoid ties in binary classification problems
- Examples: 1, 3, 5, 7, etc.
- Even values may require tie-breaking mechanisms

### 2. Balance Between Noise and Overfitting

#### Small k Values (k=1 or k=3)

- Creates complex, highly flexible decision boundaries
- Captures fine details in the data
- **Disadvantages**:
    - Highly sensitive to noise
    - Tends to overfit training data
    - Poor generalization to new data

#### Large k Values (k=11 or higher)

- Creates smoother, simpler decision boundaries
- More robust against noise
- **Disadvantages**:
    - May include dissimilar points as neighbors
    - Can blur important class distinctions
    - May cause underfit by oversimplifying the model

### 3. Consider Dataset Size

- **Rule of thumb**: k ≈ √n (where n is the number of samples)
- Larger datasets can support larger k values
- Small datasets typically work better with smaller k values

### 4. Visual Demonstration

As k increases, the decision boundary becomes progressively smoother:

- **k=1**: Jagged boundaries with islands (potentially overfitting)
- **k=3**: Smoother but still adapts to local patterns
- **k=5**: Further smoothing, filtering some noise
- **k=7**: Even smoother boundaries, potentially losing important details

## Practical Approach to Finding Optimal k

1. **Cross-validation**: Use k-fold cross-validation to evaluate different k values
2. **Grid search**: Test a range of k values (1, 3, 5, 7, 9, 11, etc.)
3. **Error curve**: Plot validation error against k values to find the "elbow point"
4. **Domain knowledge**: Consider the expected noise level in your data
5. **Ensemble approach**: For critical applications, combine predictions from multiple k values


k-NN

• Strengths:
	• Simplicity
	• Efficiency at training: No training
	• Handling Multi-class
	• Robust to noisy training data (when k > 1)
	• Often works well in practice
• Weaknesses:
	• Efficiency at testing time: need to calculate all distances (use searching
	algorithms as kd-tree)
	• Redundant training samples are not eliminated
	• Sensitivity to irrelevant or redundant features




# KD-Trees for Efficient Nearest Neighbor Searching

K-dimensional trees (k-d trees) are space-partitioning data structures that organize points in a k-dimensional space to significantly accelerate nearest neighbor searches in k-NN algorithms. They address one of the primary limitations of the k-NN algorithm: computational complexity during prediction.

## Key Characteristics of KD-Trees

<mark style="background: #FFB86CA6;">A k-d tree differs from standard decision trees in several important ways:</mark>

1. **Storage of Instances**:
    - Each internal node stores exactly one training instance (not a decision rule)
    - Leaf nodes represent regions of space containing similar points
2. **Splitting Criterion**:
    - Splits on the median value of the feature with highest variance
    - This creates a balanced partitioning of the space
    - Splitting alternates through dimensions at different levels of the tree
3. **Space Partitioning**:
    - Recursively divides the feature space into smaller regions
    - Each split creates two subspaces containing roughly equal points

## How KD-Trees Work

### Tree Construction

1. Select the feature with highest variance across the dataset
2. Find the median value of this feature
3. Place the median point at the root node
4. Recursively build left subtree with points having lower values on this feature
5. Recursively build right subtree with points having higher values on this feature
6. At the next level, select the feature with next highest variance and repeat

### Nearest Neighbor Search

1. Traverse the tree to find the leaf node containing the query point
2. Check the distance to the point stored at this node
3. Backtrack, checking if other branches could contain closer points
4. Prune branches that cannot contain closer points (based on distance calculations)

## Visual Example

Consider a 2D space with points labeled A(40,45), B(15,70), C(70,10), D(69,50), E(66,85), and F(85,90) in a 128×128 region:

1. **First Level (Root)**:
    - Split on x-coordinate (highest variance)
    - A becomes the root node (median x value is ~40)
    - Points B (left of A) go to left subtree
    - Points C, D, E, F (right of A) go to right subtree
2. **Second Level**:
    - Left branch: Only B exists, becomes leaf node
    - Right branch: Split on y-coordinate (next highest variance)
    - D becomes internal node (median y value among C,D,E,F)
    - Points C (below D in y) go to left subtree
    - Points E, F (above D in y) go to right subtree
3. **Third Level**:
    - C becomes leaf node
    - Split between E and F (on x-coordinate)
    - E becomes internal node
    - F becomes leaf node

## Performance Benefits

- <mark style="background: #FFB86CA6;">Average case search time</mark>: O(log n) vs. O(n) for brute force
- Construction time: O(n log n)
- Most efficient for low to medium dimensional data (typically < 20 dimensions)
- Particularly effective when the number of dimensions is much smaller than the number of points