# Import necessary libraries
from sklearn import tree

# Define the features (attributes) and labels (ripe or not)
# Features: [weight in grams, color (0 for green, 1 for yellow, 2 for red)]
# Labels: 0 for unripe, 1 for ripe
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [1, 1, 0, 0]

# Create a decision tree classifier
clf = tree.DecisionTreeClassifier()

# Train the classifier on the data
clf = clf.fit(features, labels)

# Define a function to predict ripeness based on weight and color
def predict_ripeness(weight, color):
    prediction = clf.predict([[weight, color]])
    if prediction[0] == 0:
        return "Unripe"
    else:
        return "Ripe"

# Test the classifier with new data
test_weight = 160
test_color = 0
prediction = predict_ripeness(test_weight, test_color)
print(f"A fruit with weight {test_weight}g and color {test_color} is predicted to be: {prediction}")
