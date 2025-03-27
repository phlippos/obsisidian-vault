
> Daten bereinigung
	- warum wichtig:
		- ungenaue und unvolständige DAten können die Effektivität von Machinelles Leaning Models beeinträchtigen.
		- und zu fehlerhaften Analysen führen.
	- Datenbereinigung und -transformation beinhalten:
		- Entfernen von Duplikaten -> die Analyse beeinträchtigen können
		- Behandeln von fehlenden Werten -> Analysen fehlerhaft oder inkostintent werden können
		- Entfernen von Ausreißer
		- überprüfen von Daten auf Konsistenz
		- Formatieren von Daten in das richtige Format
	- Imputation von Fehlenden Werten
		- Imputation beinhaltet das Ersetzen fehlender Werte durch geschätze oder repräsentative Werte
		- Mittelwert-Imputation
			- kann zu verzerrungen führen, wenn die fehlenden Werte nicht zufällig verteilt sind
		- Median-Imputation
			- robuster gegenüber Ausreißern als die Mittelwert-Imputation
			- geeignet für Daten mit nicht notmaler Verteilung
		- Modus-Imputation
			- speziell für kategoriale Daten geeignet
		- Weitere Beispiele:
			- Regression-Imputation
				- Fehlende Werte werden mithilfe einer Regressionsanalyse geschätzt.
			- K-Nearest-Neighbors-Imputation
				- Fehlende Werte werden anhand der Werte benachbarter Datens ̈atze gesch ̈atzt, wobei
					die ”K” n ̈achsten Nachbarn ber ̈ucksichtigt werden.
			- Multiple Imputation
				- Erzeugt mehrere Imputationssets und kombiniert die Ergebnisse, um Unsicherheiten in
				den Imputationen zu ber ̈ucksichtigen.
			- Hot-Deck-Imputation
				- Fehlende Werte werden durch einen Wert aus einer  ̈ahnlichen Beobachtung im
				Datensatz ersetzt, entweder zuf ̈allig oder nach bestimmten Kriterien ausgew ̈ahlt.
    Feature-Engineering
			-Schaffung neuer, relevanter Features aus den vorhandenen Daten.
			- Warum ?
				- Bessere Features k ̈onnen die Leistung von Machine Learning Modellen erheblich verbessern.
			- Mögliche Techniken:
				- Datenreduktion
				- Spezielle Techniken des Feature Engineering wie One-Hot-Encoding
				- Korrektur von Fehlern in den Daten
				- Zusammenf ̈uhren von Daten aus verschiedenen Quellen
				- Uberpr ̈ufung der Daten auf Verzerrungen und Vorurteile.
				- Scaling
	Datenintegration
			- Zusammenf ̈uhren von Daten aus verschiedenen Quellen.
			- Im Idealfall sollten die Daten zusammengef ̈uhrt werden, um eine einzige Quelle von Wahrheit zu schaffen.
			- Verwendung von Standardabfragen und -typen zur Datenintegration, Uberpr ̈ufung der  Integrität und Konsistenz der Daten beim Zusammenf ̈uhren.
	Web-Scrapping
			-  Web Scraping ist eine Technik, um automatisch Daten von Webseiten zu extrahieren.
			- Web Scraping erm ̈oglicht es Ihnen, relevante Informationen von anderen Websites oder Quellen zu sammeln, um n ̈utzliche Erkenntnisse zu gewinnen.
	 Datenvisualisierung
			 - Datenvisualisierung ist der Prozess der Darstellung von Daten in Form von visuellen Elementen wie Diagrammen, Tabellen oder Graphen.
			 - Datenvisualisierung hilft dabei, komplexe Daten leichter zu verstehen und zu interpretieren.
			 - 
			


> machinelles Lernen
> 	- Supervised Learning
> 		- the algorithm learns from a set of labeled training data.
> 		- Classification
> 			- the goal is to assign data points to predefined classes or categories.
> 			- Decision Tree Classifier
> 				- Structure:
> 					- Consists of nodes representing features and branches representing decision rules.
> 					- Starts from a root node and splits the data based on feature values.
> 					- Ends with leaf nodes representing class labels.
> 				- Splitting
> 					- The tree recursively splits data at each node based on criteria like Gini Impurity or Information Gain.
> 				- Advantages
> 					- Easy to interpret and visualize.
> 					- No need for feature scaling or extensive data preprocessing.
> 				- Drawbacks
> 					- Prone to overfitting, especially with deep trees.
> 					- Can be sensitive to small variations in data.
> 			- Accuracy
> 				- Accuracy is a commonly used metric for evaluating classification models.
> 				- ![[Pasted image 20250114161050.png]]
> 				- Accuracy alone may not be sufficient, especially when classes are unevenly distributed (imbalance).
> 			- Balanced Accuracy
> 				- Balanced accuracy is an extended metric that is particularly useful in classification models with unevenly distributed classes.
> 				- In imbalanced datasets, simple accuracy can be misleading because a model that simply predicts the majority class can achieve high accuracy.
> 				- Balanced accuracy takes into account the distribution of the classes and assigns equal importance to each class.
> 				- ![[Pasted image 20250114161222.png]]
> 			- F1-score
> 				- The F1-score is a metric that provides a balanced measure between precision and recall.
> 				- ![[Pasted image 20250114161316.png]]
> 			- Precision: 
> 				- The proportion of correct positive predictions out of all positive predictions.
> 				- ![[Pasted image 20250114161357.png]]
> 			- Recall:
> 				- The proportion of correct positive predictions out of all actual positive instances:
> 					- ![[Pasted image 20250114161422.png]]
> - Cross-Validation
> 	- K-fold cross-validation
> 	- Addresses the problem of simple train-test split
> 	- Cross-Validation is a technique for model evaluation and reducing overfitting.
> 	- The dataset is split into multiple subsets (folds).
> 	- The model is trained and validated over multiple iterations:
> 		- In each iteration, different folds are used as training or validation sets.
> 	- The most common method is k-Fold Cross-Validation, where the dataset is divided into k equal parts.
> 	- For each fold, a performance metric is calculated; the average across all folds provides a more stable model evaluation.
> 	- Helps improve the model’s generalization capability.
> - Unsupervised Learning
> 	- the algorithm extracts patterns or structures from unlabeled training data, without knowing the target variable in advance.
> 	- Application areas for unsupervised learning include:
> 		- Clustering: Identification of groups or clusters in the data, grouping similar instances together.
> 		- Anomaly Detection: Identification of data points that significantly differ from the majority, possibly due to errors or unusual behavior.
> 	- Cluster Analysis
> 		- Cluster analysis involves identifying groups of similar objects in a dataset.
> 		- Goal: Grouping data points that are similar or connected in some way.
> 		- K-Means Algorithm:
> 			- The algorithm divides data points into K clusters, where K is specified in advance.
> 			- Process:
> 				- Initialize k cluster centroids randomly.
> 				- Assign each data point to the nearest centroid, forming clusters.
> 				- Update centroids by calculating the mean of each cluster.
> 				- Repeat assignment and update steps until centroids stabilize.
> 			- Objective:
> 				- Minimize the sum of squared distances between data points and their nearest cluster centroids.
> 				- This minimizes intra-cluster variance and maximizes inter-cluster separation.
> 			- Limitations:
> 				- Sensitive to initial centroids and choice of k.
> 				- Assumes clusters are spherical and equally sized, which may not always be the case.
> 		- Internal Metrics:
> 			- Measure the quality of clusters relative to the data within the dataset.
> 				- Inertia: Sum of squared distances of data points to their respective cluster centers (lower is better).
> 				- Silhouette Score: A measure of how similar a data point is to its own cluster compared to other clusters (higher is better).
> 		- External Metrics:
> 			- Compare the quality of clusters with external information, such as true class labels.
> 				- Adjusted Rand Index(ARI):Compares the similarity between true and assigned clusters (1 means perfect similarity).
> 				- Normalized Mutual Information (NMI): Measures the amount of shared information between true and assigned clusters (1 means perfect similarity).

### K-Nearest-Neighbors
- simple, non-parametric and lazy learning algorithm used for classification and regression
- Training phase :
	- The algorithm stores all the training examples in the memory.
	- instance-based learning algorithm
- Prediction phase:
	- Classification: To classify a new data point, the algorithm finds k training examples that are closet to the new data point(using distance metric). The class of the new data point is detemined by the majority class among the k neighbors.
	- Regression: The output is the avarage of the values of the k nearest neighbors.
- key components:
	- 1-choosing k:
		- hyperparameter
		- high values can lead to underfitting while low values may cause overfitting
		- use cross-validation to find the optimal k.
	- Distance Metric:
		- is eesential for identifying the nearest neighbors
		- Euclidian Distance : sensitive to scale
		- Manhattan Distance : useful for data with grid-like structures
	- optional Neighbor weighting:
		- might be beneficial to weight the neighbors so that closer neighbors have a larger influence.
		- inverse of distance 
		- $$w_i=\frac{1}{d(x, x_i)}$$
		- for classification :
			- $$ y = argmax_c(\sum_{i=1}^kw_i*\delta(y_i=c))$$
		- for regression:
			- $$y = \frac{\sum_{i=1}^kw_i*y_i}{\sum_{i=1}^kw_i}$$
		- pro : 
			- simple to understand and implement
			- flexible with large dataset
			- no assumption about data distribution
		- contra:
			- sensitive to outliers
			- requires selecting an optimal k value
			- computationally expensive with large datasets

### Naive Bayes Classifiers
- probabilistics models based on Bayes Theorem
- naive assumption of conditional independence between every pair of features given the class label.
- naive assumption:
	- $$ P(X_1, X_2, \dots, X_n \mid Y) = \prod_{i=1}^n P(X_i \mid Y) $$
	- where x_i represents each feature
- Multinomial Naive Bayes Assumptions
	- effective for discrete data, especially in text classification problems where data typically represent word counts or frequencies
	- steps:
		- calculate prior probobilities:
			- $$ P(C_k) = \frac{Number \space of\space samples \space in\space class\space C_k}{Total\space number\space of\space samples}$$
		- calculate Likelihoods : For each feature x_i and class c_k
			- $$ P(x_i \mid c_k) = \frac{\text{count of } x_i \text{ in documents of class } c_k + \alpha}{\text{Total count of all words in documents of class } c_k + \alpha \cdot \text{Number of unique words}}$$
		- calculate posterior probabilities:
			- $$P(C \mid X) = P(x_1, x_2, \dots, x_n \mid C) = P(C) \cdot \prod_{i=1}^n P(x_i \mid C)^{f_i}$$
	- Maximum Likelihood Estimation:
		- is a method for estimating model parametes that maximize the likelihood of the observed data.
		- Goal of MLE: Find parameter values that maximize the probability of the observed data.
	- Advantages:
		- highly efficient for high-dimensional data like text words
		- low memory requirements fast prediction
	- Limitations:
		- performs less effectively with numerical features(continuous values)
		- sensitive to irrelevant features, so feature selection can be helpful
	- Roc-Curve
		- The **ROC-AUC curve** is a performance evaluation metric used for binary classification tasks.
		- The ROC curve plots the **True Positive Rate (TPR)** against the **False Positive Rate (FPR)** at various threshold settings.
		- **True Positive Rate (TPR)**, also called Sensitivity or Recall: It is the proportion of actual positive cases correctly identified by the model.
		- **False Positive Rate (FPR)**: It is the proportion of actual negative cases incorrectly classified as positive.
		- Area Under the Curve (AUC)
			- **AUC** represents the area under the ROC curve. It quantifies the overall ability of the model to distinguish between the two classes
			- An **AUC of 1** means the model perfectly classifies all positive and negative cases.
			- An **AUC of 0.5** indicates that the model performs no better than random chance.
			- An **AUC < 0.5** implies the model is worse than random chance, potentially making reverse predictions.
			- The closer the ROC curve is to the top-left corner, the better the model is at distinguishing between classes.
			- The **AUC score** is a summary measure of the performance, with higher values indicating better performance.
			- ![[Pasted image 20250115150400.png]]
		- The only "hyperparameter" in Naive Bayes classifiers is the smoothing factor.
		- In Laplace smoothing, a value is added to all value counts, and the smoothing can be controlled with "alpha."
		- Depending on the use case, other classifiers can also be used:
		    - **MultinomialNB**:
		        - For discrete values (e.g., word count).
		    - **BernoulliNB**:
		        - For binary data (discrete probability calculation).
		    - **GaussianNB**:
		        - For continuous data.

### Clustering
- unsupervised ML technique
- that involves grouping a set of objects in such a way, that objects in the same group(called cluster) are more similar to each other than to those in other groups
- used for pattern recognition
- partition-based clustering
	- divides data into k groups.
	- K-Means clustering
		- It aims to partition a dataset into K distinct, non-overlapping subsets (or clusters) where each data point belongs to the cluster with the nearest mean.
		- steps:
			- initialization:
				- choose K
				- initialize K centroids randomly.
			- Assignment:
				- Assign each data point to the nearest centroid. This forms K clusters.
			- update:
				- calculate the new centroids as the mean of the data points in each cluster.
			- repeat:
				- repeat the assignment do not change significantly, or a maximum number of iterations is reached.
	- Hierarchical Clustering
		- Builds a tree of clusters
		- two types: Agglomerative (bottom-up) and diviside (top-down)
		- no need to specify the number of clusters in advance
		- steps in Agglomerative:
			- initialization:
				- Start with each data point as its own cluster
			- Merge
				- Find the pair of clusters that are closet to each other (based on a chosen distance metric)
				- update the distances between the new cluster and the remaining clusters.
			- Repeat
				- continue merging the closet pairs of clusters until only one cluster remains or a stopping criterion(such as desired n umber of clusters) is met.
			- Form Hierarchical Tree:
				- the merging process forms a dendogram, a tree-like diagram that records the sequence of merges.
	- Density based Clustering
		- DBSCAN
			- it works by grouping together points that are closely packed(high density regions) and marking as outliers points that lie done in low density regions
			- Key concepts:
				- Core points:
					- A point is a core point if it has at least a specified number of points(Min pts) within a given radius(Epsilon)
				- border points: 
					- A point that is not a core point but falls within the epsilon radius of a core point
				- Noise points 
					- points that are neither core points nor corder points.
			- ![[Pasted image 20250115161555.png]]
			- - **Inertia** is the sum of the squared distances of the points to their nearest centroid.
		    - **Cohesion**
		    - Smaller values indicate points that are closer together ("better" clusters).
		    
			- $$ \text{Inertia} = \sum_{i=1}^{k} \sum_{j=1}^{n_i} ||x_{ij} - \mu_i||^2 $$
			-  $$ k := \text{Number of clusters} $$
			- $$ n_i := \text{Number of points in cluster i} $$  
			- $$ x_{ij} := \text{Point j in cluster i} $$  
			- $$ \mu_i := \text{Centroid of cluster i} $$ 
			- Elbow Method to select the best K
				- The **Elbow Method** is a popular technique used to determine the optimal number of clusters in a clustering algorithm like **K-Means**.
				- It helps identify the point where adding more clusters doesn't significantly improve the model's performance, which is where the "elbow" occurs on a plot.
				- steps:
					- Fit the Model for Different K Values
					- **Compute the Inertia** (or within-cluster sum of squared distances)
					- Plot the Inertia vs. K
					- Look for the "Elbow"


### Decision Tree
- A decision tree is a model used to represent decisions and their possible consequences
- it consists of :
	- Nodes: represent decisions or tests on attributes
	- Edges: represent decision flow based on attribute values
	- leaves: represent the class assignment or prediction
- S: The current dataset or a subset of the dataset being analyzed.
	- initially, S the entire dataset
	- At each decision point in the tree, S is divided into subsets.
- v: A possible value of an attribute used to split S.
	- each of values v generates a seperate subset of S
- relationship between S and v:
	- Each split of the dataset S produces subsets S_v , one for each value v of the selected attribute.
	- The information gain is maximized by the attribute that most reduces the entropy over the subsets S_v.

| Applicant | Experience | Hired |
|-----------|------------|-------|
| 1         | Junior     | No    |
| 2         | Senior     | Yes   |
| 3         | Senior     | Yes   |
| 4         | Junior     | No    |
| 5         | Senior     | Yes   |
- Entropy H(S) of the entire dataset:
- $$ H(S) = -\sum_{i=1}^{n} p_i \log_2 p_i $$
- where pi is the proportion of examples in S that belong to class i.
- $$ H(S) = -\frac{3}{5} \log_2 \frac{3}{5} + \frac{2}{5} \log_2 \frac{2}{5} $$

$$ \approx 0.971 $$
- General formula for calculating the Information Gain IG(S, A) of an attribute A:
	- $$ IG(S, A) = H(S) - \sum_{v \in \text{Values}(A)} \frac{|S_v|}{|S|} H(S_v) $$
	- Junior (2 applicants): 0 Yes, 2 No ⇒ H(Junior) = 0
	- Senior (3 applicants): 3 Yes, 0 No ⇒ H(Senior) = 0
	- $$IG(S, \text{Experience}) = H(S) - \frac{2}{5} \times H(\text{Junior}) + \frac{3}{5} \times H(\text{Senior})$$
	- $$IG(S, \text{Experience}) = 0.971 - \frac{2}{5} \times 0 + \frac{3}{5} \times 0$$
	- $$IG(S, \text{Experience}) = 0.971 - 0 - 0$$
	- $$IG(S, \text{Experience}) = 0.971$$
	- Since the information gain is maximal for this attribute, we choose Experience for the split.
	- ![[Pasted image 20250115205406.png]]
	- Entropy measures the ”impurity” or ”disorder” in the dataset – how mixed the class assignments within a subset are.
	- Information Gain shows how much impurity is reduced when the dataset is split based on a particular feature.
	- We calculate the information gain for each feature and choose the feature with the highest information gain to determine the best split.
	- Algorithms for Decision Tree Construction
		- ID3 (Iterative Dichotomiser 3):
			- Uses entropy to calculate the information gain.
			- Performs splits based on the attribute with the largest information gain.
		- C4.5:
			- Uses information gain ratio.
			- Improves ID3 by preferring attributes that provide a better balance when splitting.
		- CART (Classification and Regression Trees):
			- Uses the Gini index to measure purity.
			- Used in Scikit-learn to create binary decision trees.

### Gradient Method
- Goal of Optimization: Find model parameters that minimize a defined error or maximize the likelihood of the data.
- Gradient Method: An iterative optimization method that uses the direction and magnitude of a function’s change to find its minima or maxima.
- Adjusting weights in neural networks
- why needed ? 
	- Many computer science problems can be modeled with a function f (x) whose minimum is sought.
	- Example: Minimizing the error of a model when predicting data.
	- The gradient method provides an efficient way to iteratively refine a solution without needing to analyze the entire function.
	- Advantages of the gradient method:
		- Iterative approximation to the solution
		- Flexible and widely applicable
		- Suitable for high dimensionality and large data sets
	- Mathematical Foundations:
		- Definition of the Gradient:
			- The gradient ∇f (x) of a function f : Rn → R indicates the direction of steepest ascent.
		- Principle of Gradient Descent: 
			- To find the minimum of f (x), one moves in the opposite direction of the gradient −∇f (x).
		- Update Formula:
			- $$ x_{k+1} = x_k - \alpha \nabla f(x_k) $$
			- α is the learning rate.
			- ∇f(xk​) is the gradient of the function f at the point xk.
	- Batch Gradient Descent:
		- Calculates the gradient over the entire dataset in each step.
		- Stable and converges steadily, but computationally intensive for large datasets.
	- Mini-Batch Gradient Descent:
		- Uses small, random data subsets (mini-batches) to calculate the gradient.
		- Combines speed and stability, frequently used in machine learning.
	- Stochastic Gradient Descent (SGD):
		- Calculates the gradient for a single random data point in each step.
		- Very fast but prone to fluctuations; often converges closer to global minima.
	- Advantages of Variants: Mini-Batch and SGD are faster and require less memory, making them suitable for very large datasets.
	- ![[Pasted image 20250115230651.png]]
	- Gradient for Multi-Variable Functions
		- For functions with multiple variables, the gradient describes the rate of change in all dimensions.
		- Example: For the function \( f(x, y, z) = x^2 + y^2 + z^2 \), the gradient is:
		- $$ \nabla f(x, y, z) = \begin{pmatrix} \frac{\partial f}{\partial x} \\\frac{\partial f}{\partial y} \\\frac{\partial f}{\partial z}\end{pmatrix}= \begin{pmatrix}2x \\2y \\2z\end{pmatrix} $$
		- ![[Pasted image 20250115230950.png]]
		- Loss Landscape: The 3D surface shows f (x, y, z) = x2 + y2 + z2, indicating that f decreases toward (0, 0, 0).
		- Optimization Path: The SGD optimizer moves step-by-step along the negative gradient toward the global minimum at (0, 0, 0).
		- Convergence: The path shows a gradual approach to the minimum.
		- Choosing the Learning Rate: A high learning rate may lead to instability; a low rate slows convergence.

### Linear Regression
- statistical method used to model the relationship between a dependent variable and one or more independent variables by fitting a linear equation to the observed data.
- The goal is to find the best-fitting line that describes the relationship between the variables.
- $$ y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_n x_n + \epsilon $$
- y is the dependent variable (target).
- β0​ is the intercept.
- β1​,β2​,…,βn​ are the coefficients of the features x1,x2,…,xnx_1, x_2, \dots, x_nx1​,x2​,…,xn​.
- ϵ is the error term (residual).
- Simple Linear Regression :
	- Simple linear regression is the case with one dependent variable and one independent variable:
		- $$ y = \beta_0 + \beta_1 x_1 + \epsilon $$
		- Goal: Find the best-fit line by determining β0 and β1 that minimize the prediction error.
	- Least Squares Method:
		- To find the best line, we aim to minimize the prediction errors for all data points by minimizing the sum of squared errors (SSE):
			- $$ S(\beta_0, \beta_1) = \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i)^2 $$
			- where:
				- yi is the observed value for each data point i
				- β0 + β1xi is the predicted value for y given xi
			- This error function is quadratic, meaning that it has a unique minimum that we can find by taking derivatives.
			- To find the minimum, we take partial derivatives of S(β0, β1) with respect to β0 and β1, setting each derivative to zero.
				- $$ \frac{\partial S}{\partial \beta_0} = -2 \sum_{i=1}^{n} (y_i - \beta_0 - \beta_1 x_i) = 0 $$
				- $$ \frac{\partial S}{\partial \beta_1} = -2 \sum_{i=1}^{n} x_i (y_i - \beta_0 - \beta_1 x_i) = 0 $$
				- By setting these derivatives to zero, we can solve for the values of β0 and β1 that minimize the SSE.
				- To solve for β1, we start by using the second equation.
					- $$ \sum_{i=1}^{n} x_i (y_i - \beta_0 - \beta_1 x_i) = 0 $$
					- Substitute β0 =  ̄y − β1x ̄:
						- $$ \sum_{i=1}^{n} x_i y_i - (\bar{y} - \beta_1 \bar{x}) \sum_{i=1}^{n} x_i - \beta_1 \sum_{i=1}^{n} x_i^2 = 0 $$
						- $$ \sum_{i=1}^{n} x_i y_i - \bar{y} \sum_{i=1}^{n} x_i + \beta_1 \bar{x} \sum_{i=1}^{n} x_i - \beta_1 \sum_{i=1}^{n} x_i^2 = 0 $$
						- $$ \sum_{i=1}^{n} x_i y_i - \bar{y} \sum_{i=1}^{n} x_i = \beta_1 \sum_{i=1}^{n} x_i^2 - \beta_1 \bar{x} \sum_{i=1}^{n} x_i $$
						- $$ \sum_{i=1}^{n} x_i y_i - \bar{y} \sum_{i=1}^{n} x_i = \beta_1( \sum_{i=1}^{n} x_i^2 - \bar{x} \sum_{i=1}^{n} x_i) $$
						- $$ \beta_1 = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^{n} (x_i - \bar{x})^2} $$
						- This formula represents the slope of the best-fit line in simple linear regression.
- Multiple linear regression
	- Multiple linear regression includes multiple independent variables.
	- In multiple linear regression, we use matrix notation to generalize and simplify the model. The model can be written as:
		- $$ y = X\beta + \epsilon $$
		- y is the vector of target values (dependent variable).
		- X is the matrix of feature values (independent variables).
		- β is the vector of coefficients (parameters) to be learned.
		- ϵ is the vector of errors (or residuals), representing the difference between the predicted and actual values.
	- To solve for β, we set up the least squares objective in matrix form, minimizing the squared error:
		- $$ (y - X\beta)^T (y - X\beta) $$
		- It represents the squared difference between the observed values y and the predicted values Xβ
	- Derivative with respect to β
		- $$ \frac{\partial}{\partial \beta} \left[ (y - X\beta)^T (y - X\beta) \right] $$
		- $$ -2X^T (y - X\beta) $$
	- Setting the derivative to zero
		- $$ -2X^T (y - X\beta) = 0 $$
		- $$ X^T (y - X\beta) = 0 $$
		- $$ X^T y - X^T X \beta = 0 $$
		- $$ \beta = (X^T X)^{-1} X^T y $$
		- This matrix equation provides the solution for the coefficients that minimize the squared error.
- Model Evaluation Metrics
	- $$ R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2} $$
		- An R^2 close to 1 indicates that the model explains a large portion of the variance in the target variable.
		- where ˆyi are the predicted values and  ̄y is the mean of the actual values yi
		- Assumes a linear relationship between the independent and dependent variables.
		- Is sensitive to outliers.
		- Can improve with additional independent variables, even if these do not add relevant information.
	- $$ MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 $$
		- The MSE provides a measure of the average squared error, with a smaller value indicating better model accuracy.
	- $$ RMSE = \sqrt{MSE} $$
	- RMSE gives the error in the same units as the target variable y, and it indicates the typical magnitude of the prediction error. Lower RMSE values suggest a better fit of the model.


### Neural Networks
- Perceptron
	- Perceptron is the simplest model of an artificial neuron
	-  **Vector**: $$( \mathbf{x} = [x_1, x_2, \dots, x_n]^T)$$
	- Bias: $$ b $$
	- Net input :$$z = \mathbf{w}^T \mathbf{x} + b$$
	- Activation Function (Heaviside Function): $$f(z) = \begin{cases} 1 & \text{if } z > 0 \\ 0 & \text{otherwise} \end{cases}$$
	- Output: $$y = f(z)$$
	- Decision boundry $$\mathbf{w}^T \mathbf{x} + b = 0$$
	- Goal : adjust the weight to minimize classification errors
	- Learning rule (for each training step):
		- $$\mathbf{w} \leftarrow \mathbf{w} + \eta (d - y) \mathbf{x}$$
		- $$b \leftarrow b + \eta (d - y)$$
		- η: Learning rate (small positive value)
		- d: Desired output (target output)
		- y: Current output of the perceptron
	- Convergence Theorem:
		- If the data is linearly separable, the algorithm converges to a solution.
	- The perceptron can successfully solve linearly separable problems.
	- Can only solve linearly separable problems.
	- ![[Pasted image 20250116151649.png]]
	- Neural Networks
		- Networks of interconnected neurons.
		- Capable of modeling complex nonlinear relationships.
		- Consist of input, hidden, and output layers.
		- Use activation functions for nonlinearity.
	- Layers:
		- Input layer
		- One or more hidden layers
		- Output layer
	- Full connected: Each neuron in one layer is connected to every neuron in the next layer.
	- Weights determine the strength of the connections.
	- Bias neurons can be added.
	- Feedforward Propagation:
		- Input data is propagated through the network.
		- Each layer computes:
			- $$a^{(l)} = f\left(W^{(l)} a^{(l-1)} + b^{(l)}\right)$$
			- a(l): Activations in layer l
			- W(l): Weight matrix of layer l
			- b(l): Bias vector of layer l
			- f : Activation function
		- The output of the last layer is the network’s prediction.
	- Activation Functions
		- ![[Pasted image 20250116152149.png]]
		- Sigmoid Function:
			- Commonly used in the output layer for binary classification tasks.
			- Maps output to a range between 0 and 1, making it suitable for probabilities.
			- Limitation: Can cause vanishing gradients during training.
		- Hyperbolic Tangent (tanh):
			- Often used in hidden layers of shallow networks.
			- Outputs values between -1 and 1, centering the data and improving convergence.
			- Limitation: Also suffers from vanishing gradients for large inputs.
		- ReLU:
			- Most widely used in hidden layers of deep networks.
			- Computationally efficient and mitigates vanishing gradient problems.
			- Limitation: Can lead to ”dead neurons” (ReLU outputs 0 for all inputs ¡ 0).
	- Backpropagation
		- Step 1: Feedforward Pass
			- Pass input data through the network to compute the output.
		- Step 2: Compute Error
			- Compare the network’s output to the target using a loss function.
		- Step 3: Backward Pass
			- Calculate how much each weight contributed to the error (gradients).
		- Step 4: Update Weights
			- Adjust weights to reduce the error using the gradients and learning rate.
		- Step 5: Repeat
			- Repeat for all training data and multiple epochs to improve accuracy.
		- Goal: Minimize the error and improve predictions by optimizing the network’s weights.
		- Importance for training:
			- Enables the training of deep neural networks.
			- Adjusts weights in the direction of steepest error descent.
			- Iterative process repeated until convergence.
			- Overfitting can be avoided through regularization.
			- Optimization Methods: Stochastic Gradient Descent, Adam, RMSprop, etc.
		- Advantages:
			- Flexibility: Models complex, nonlinear relationships.
			- Automation: Detects patterns and features without manual intervention.
			- Scalability: Works efficiently with large and high-dimensional datasets.
		- Disadvantages:
			- Computationally Intensive:
			- Black-Box:
			- Requires large amounts of high-quality data.
- CNN
	- CNNs are a type of neural network designed to work with structured data like images.
	- Automatically detects important patterns (like edges, shapes) in data.
	- Excellent for image and video analysis tasks.
	- Extract features using small filters (kernels).
	- Simplify data using pooling (reduces size while keeping key information).
	- Make predictions using fully connected layers.
	- Principle of Convolution
		- Convolution:
			- Applies filters (kernels) over the input.
			- Captures spatial patterns like edges, textures, or corners.
		- how it works:
			- The filter slides (convolves) over the image.
			- Computes a dot product between the filter and the input region.
			- Outputs a feature map.
	- Principle of Pooling
		- Pooling:
			- Reduces the size of the feature map while retaining important information.
			- Helps to make the network invariant to small translations and distortions.
		- Types of Pooling:
			- Max Pooling: Selects the maximum value in each pooling region.
			- Average Pooling: Computes the average of values in each pooling region.
			- Global Pooling: Reduces the feature map to a single value per channel.
		- How it works:
			- A pooling filter slides over the feature map.
			- Applies the pooling operation (e.g., max or average) to each region.
			- Produces a smaller, ”pooled” feature map.


### Optimization 
- Momentum
	- Accelerates gradient descent by considering past gradients.
	- 
- Adaptive learning rate
	- to adjust the learning rate dynamically during training.
	- improve the convergence speed and performance by adapting the learning rate based on the gradient information from the previous iterations
	- AdaGrad
		- adapts the learning rate for each parameter based on the history of gradients.
		- It assigns smaller learning rates to parameters associated with frequently occuring features and larger learning rates to parameters associated with infrequent features.
		- Suitable for sparse data.
		- contra: learning rate can become very small, leading to slow convergence
	- RMSProp
		- addresses the diminishing learning rate issue of Adagrad by using exponentially decaying average of squared gradients.
	- Adam
		- Combines advantages of adagrad and rmsprop by computing adaptive learning rates for each parameter
		- robust to noisy data, works well

### Regularization
- to prevent overfitting and improve model generalization.
- adding a penalty to the loss function
- L1 Regularization(Lasso):
	- adds the absolute value of the coefficients to the loss function. 
	- performing feature selection
	- the coefficients of the features that dont contribute the model prediction are set to zero.
	- contra: can be instable
- L2 Regularization(Ridge):
	- adds the squared value of the coefficients to the loss function.
	- It discourages large coefficients, leading to smaller, more overly distributed weights.
	- pro : more robust to multicollinearity
	- contra: doesnt perform feature selection
- Dropout:
	- It works by randomly "dropping out" a fraction of neurons during training, which helps prevent overfitting
	- During each training iteration , each neuron is kept with probability p and dropped with probability 1-p
	- pro:
		- reduces overfitting
		- acts as an ensemble method, as different subsets of the network trained during different iterations
	- contra:
		- increasing training time
- Early stopping:
	- monitors the model's performance on a validation set during training and stops training, when performance starts to degrade, indicating overfitting
- Data Augmentation:
	- increases the size and variability of the training set by applying random transformations to the training data
	- improves generalization
	- can increase training time
- Batch normalization:
	- normalizes the inputs of each layer to have a mean of zero and a variance of one, whic helps to stabilize and accelerate training
	- faster convergence
	- contra: adds computational overhead during training
- RNN
	- RNNs are neural networks designed to recognize patterns in sequences of data.
	- At each step in the sequence, the RNN takes an input and combines it with information from previous steps.
	- This allows the RNN to make decisions based on both current input and past context.
	- Challenges with Standard RNNs:
		- Difficulty in learning long-term dependencies due to issues like vanishing gradients.
- LSTM
	- LSTMs are a special kind of RNN capable of learning long-term dependencies.
	- Designed to remember information for long periods.
	- Gates are mechanisms that decide what information is important to keep or forget.
		- Forget Gate: Decides what information to discard from the cell’s state.
		- Input Gate: Determines which new information to add to the cell’s state.
		- Output Gate: Controls what information from the cell’s state to output.
	- Benefits of LSTMs:
		- Effectively capture long-term dependencies in data.
- Autoencoders
	- Neural networks trained to copy their input to their output.
	- Consist of an encoder and a decoder.
	- Architecture:
		- Encoder: Compresses the input into a latent-space representation.
		- Decoder: Reconstructs the input from the latent representation.
	- Applications:
		- Dimensionality reduction.
- Generative Adversarial Networks (GANs)
	- GANs are a class of machine learning frameworks designed for generating new data.
	- Composed of two neural networks: a Generator and a Discriminator.
	- How do GANs Work?
		- Generator tries to create data that resembles real data.
		- Discriminator tries to distinguish between real data and data produced by the Generator.
		- They are trained together in a loop:
			- The Generator improves its data to fool the Discriminator.
			- The Discriminator gets better at spotting fake data.
	- Challenges:
		- Training GANs can be difficult due to the delicate balance required between the Generator and Discriminator.
		- Issues like mode collapse, where the Generator produces limited types of outputs.



















