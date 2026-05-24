# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This model is a Logistic Regression classifier built using scikit-learn. The model predicts whether an individual's income exceeds $50K per year based on census demographic data. The model was trained using processed categorical and numerical features from the census dataset. Categorical variables were transformed using OneHotEncoder and labels were transformed using LabelBinarizer.

## Intended Use

The intended use of this model is educational and experimental purposes for demonstrating machine learning pipeline development, model training, model evaluation, and deployment workflows. The model predicts income classification based on census features and is not intended for real-world employment, financial, legal, or governmental decision-making.

## Training Data

The training data comes from the census.csv dataset. The dataset contains demographic and employment-related information such as workclass, education, marital status, occupation, relationship, race, sex, native country, and salary classification. The dataset was split into training and testing subsets using a train-test split with 70% used for training and 30% used for testing.

## Evaluation Data

The evaluation dataset consists of the 30% testing split generated from the original census dataset. The testing data was processed using the fitted OneHotEncoder and LabelBinarizer from the training pipeline to ensure consistent transformations between training and evaluation.

## Metrics

The model was evaluated using Precision, Recall, and F1 Score.

Model performance:

- Precision: 0.7221
- Recall: 0.5610
- F1 Score: 0.6314

Performance metrics were also calculated across categorical feature slices to 
evaluate model behavior on different demographic subgroups.

## Ethical Considerations

This model uses demographic information that may introduce bias into predictions. Features such as race, sex, and native country can contribute to unfair or discriminatory outcomes if used in real-world applications. Predictions from this model should not be used for hiring, compensation, lending, legal, or other high-stakes decisions involving individuals.

The dataset may also contain historical societal biases that are reflected in the training data and therefore reproduced by the model.

## Caveats and Recommendations

This model is intended primarily for learning and demonstration purposes. The model performance is moderate and may not generalize well to unseen real-world data. Additional preprocessing, feature engineering, hyperparameter tuning, and fairness analysis would likely improve performance and reliability.
