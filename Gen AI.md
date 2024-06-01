### Linear Regression
- **Definition**: A linear approach to modeling the relationship between a dependent variable and one or more independent variables.
- **Equation**: $y = \beta_0 + \beta_1 x_1 + \beta_2 x_2 + \ldots + \beta_n x_n$
- **Use Cases**: Predicting house prices, stock prices, and other continuous outcomes.
- **Assumptions**: Linearity, independence, homoscedasticity, normal distribution of errors.

### Naive Bayes
- **Definition**: A probabilistic classifier based on Bayes' theorem, assuming independence between predictors.
- **Types**: Gaussian, Multinomial, Bernoulli.
- **Use Cases**: Spam detection, text classification, sentiment analysis.
- **Assumptions**: Feature independence, although often violated, still performs well.

### DBSCAN (Density-Based Spatial Clustering of Applications with Noise)
- **Definition**: A clustering algorithm that groups points closely packed together, marking points in sparse regions as outliers.
- **Parameters**: ε (epsilon) - neighborhood radius, MinPts - minimum points to form a dense region.
- **Use Cases**: Geospatial data analysis, noise identification, anomaly detection.
- **Strengths**: Can find arbitrarily shaped clusters, robust to noise.

### Logistic Regression
- **Definition**: A statistical model used for binary classification, modeling the probability that a given input belongs to a particular category.
- **Equation**: $P(Y=1) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \ldots + \beta_n x_n)}}$
- **Use Cases**: Disease prediction, customer churn prediction, fraud detection.
- **Assumptions**: Linearity in logit, independence of errors, large sample size.

### K-Nearest Neighbors (KNN)
- **Definition**: A non-parametric, instance-based learning algorithm used for classification and regression.
- **Mechanism**: Classifies based on the majority label among the k-nearest neighbors.
- **Use Cases**: Image recognition, recommendation systems, anomaly detection.
- **Strengths**: Simple to implement, no training phase, adaptable to multi-class problems.

### Hierarchical Clustering
- **Definition**: A method of cluster analysis which seeks to build a hierarchy of clusters.
- **Approaches**: Agglomerative (bottom-up) and Divisive (top-down).
- **Use Cases**: Taxonomy, gene sequence analysis, market segmentation.
- **Strengths**: Does not require the number of clusters to be specified in advance.

### Decision Trees
- **Definition**: A non-parametric supervised learning method used for classification and regression.
- **Components**: Nodes (features), Edges (decisions), Leaves (outcome).
- **Use Cases**: Credit scoring, diagnostic tests, operations research.
- **Strengths**: Easy to understand and interpret, handles both numerical and categorical data.

### Neural Networks
- **Definition**: A series of algorithms that attempt to recognize underlying relationships in a set of data through a process mimicking the way the human brain operates.
- **Components**: Neurons, weights, biases, activation functions.
- **Use Cases**: Image and speech recognition, autonomous driving, natural language processing.
- **Strengths**: Capable of capturing complex patterns, adaptable to a wide range of tasks.

### Gradient Boosting Machines (GBM)
- **Definition**: An ensemble learning method that builds models sequentially, each new model correcting errors made by the previous ones.
- **Components**: Base learners (usually decision trees), learning rate, number of iterations.
- **Use Cases**: Web search ranking, recommendation systems, predictive analytics.
- **Strengths**: High predictive accuracy, handles mixed types of data well.

### Random Forest
- **Definition**: An ensemble learning method that builds multiple decision trees and merges them to get a more accurate and stable prediction.
- **Mechanism**: Each tree is trained on a bootstrap sample of the data, and splits are based on a random subset of features.
- **Use Cases**: Feature selection, classification tasks, regression tasks.
- **Strengths**: Reduces overfitting, robust to noise, handles large datasets well.

### Principal Component Analysis (PCA)
- **Definition**: A dimensionality reduction technique that transforms a large set of variables into a smaller one that still contains most of the information.
- **Components**: Principal components, eigenvalues, eigenvectors.
- **Use Cases**: Image compression, exploratory data analysis, noise reduction.
- **Strengths**: Reduces dimensionality, improves interpretability while minimizing information loss.

### AdaBoost (Adaptive Boosting)
- **Definition**: An ensemble learning technique that combines multiple weak classifiers to create a strong classifier.
- **Mechanism**: Focuses on training samples that previous classifiers misclassified by adjusting their weights.
- **Use Cases**: Face detection, binary classification problems, text classification.
- **Strengths**: Improves accuracy, reduces bias and variance.

### Support Vector Machines (SVM)
- **Definition**: A supervised learning model used for classification and regression that finds the hyperplane which best separates the classes.
- **Kernel Types**: Linear, polynomial, radial basis function (RBF), sigmoid.
- **Use Cases**: Image classification, bioinformatics, text categorization.
- **Strengths**: Effective in high-dimensional spaces, versatile with different kernel functions.

### K-Means Clustering
- **Definition**: A partitioning method that divides the dataset into K distinct, non-overlapping subsets (clusters).
- **Mechanism**: Assigns each data point to the nearest cluster center, then re-calculates cluster centers until convergence.
- **Use Cases**: Customer segmentation, market research, pattern recognition.
- **Strengths**: Simple and fast, scalable to large datasets.

### Hidden Markov Models (HMM)
- **Definition**: A statistical model that represents systems which are Markov processes with hidden states.
- **Components**: States, observations, transition probabilities, emission probabilities.
- **Use Cases**: Speech recognition, bioinformatics (gene prediction), financial modeling.
- **Strengths**: Handles temporal data, can model sequences with probabilistic frameworks.
