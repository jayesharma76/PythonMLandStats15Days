# Python ML and Stats: 15-Day Learning Plan

## Phase 1: Descriptive Stats & Linear Models (Days 1–5)
Focus: Understanding data distribution and the "Line of Best Fit."

### Day 1: Descriptive Statistics & NumPy
**Concepts:** Mean, Median, Mode, Variance, and Standard Deviation.  
**Practical:** Use numpy to calculate these from scratch on a synthetic dataset.

### Day 2: Distributions & Data Visualization
**Concepts:** Normal (Gaussian) Distribution and the Central Limit Theorem.  
**Practical:** Use seaborn to plot histograms and KDE plots to identify "normality."

### Day 3: Linear Regression (The Math)
**Concepts:** Correlation vs. Causation, Intercept, and Slope.  
**Practical:** Implement Simple Linear Regression using scikit-learn on a housing dataset.

### Day 4: Multiple Regression & Overfitting
**Concepts:** Bias-Variance Tradeoff and Adjusted R-Squared.  
**Practical:** Build a model with multiple features and evaluate performance.

### Day 5: Gradient Descent Basics
**Concepts:** Cost functions (MSE) and how models "learn" by minimizing error.  
**Practical:** Plot a loss curve to see the error decrease over iterations.

## Phase 2: Classification & Probability (Days 6–10)
Focus: Moving from continuous values to categories.

### Day 6: Logistic Regression
**Concepts:** The Sigmoid function and binary classification.  
**Practical:** Predict a binary outcome (e.g., "Will this customer churn?") using LogisticRegression.

### Day 7: Classification Metrics
**Concepts:** Precision, Recall, F1-Score, and the Confusion Matrix.  
**Practical:** Use sklearn.metrics to evaluate your Day 6 model.

### Day 8: K-Nearest Neighbors (KNN)
**Concepts:** Distance metrics (Euclidean vs. Manhattan) and the "K" hyperparameter.  
**Practical:** Build a KNN classifier and visualize the decision boundaries.

### Day 9: Probability & Naive Bayes
**Concepts:** Bayes' Theorem and Conditional Probability.  
**Practical:** Build a simple "Spam vs. Ham" email filter.

### Day 10: Support Vector Machines (SVM)
**Concepts:** Hyperplanes, Margins, and the "Kernel Trick."  
**Practical:** Apply an SVM with different kernels (Linear vs. RBF) to see boundary changes.

## Phase 3: Trees, Ensembles & Unsupervised (Days 11–15)
Focus: Non-linear logic and discovering hidden patterns.

### Day 11: Decision Trees
**Concepts:** Entropy, Information Gain, and Gini Impurity.  
**Practical:** Train a DecisionTreeClassifier and export the tree graphic.

### Day 12: Random Forest (Ensemble Learning)
**Concepts:** "The Wisdom of the Crowd" and Bagging (Bootstrap Aggregating).  
**Practical:** Compare Random Forest performance against a single Decision Tree.

### Day 13: K-Means Clustering
**Concepts:** Unsupervised learning and Centroids.  
**Practical:** Segment a customer dataset into "clusters" based on spending habits.

### Day 14: Dimensionality Reduction (PCA)
**Concepts:** Principal Component Analysis—how to compress data while keeping info.  
**Practical:** Reduce a 10-feature dataset to 2 features and plot them.

### Day 15: Final Practical Review
**Practical:** Take a small dataset (like the Titanic or Iris dataset) and run a full pipeline: Preprocessing -> Scaling -> Modeling -> Evaluation.
