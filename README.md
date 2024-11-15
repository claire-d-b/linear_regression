# Activate python virtual environment

- python -m venv venv
- source venv/bin/activate

# Install required libraries

- pip install numpy matplotlib pandas flake8
- alias norminette=flake8

# Delete python environment

deactivate

# There are 3 programs here:

- estimate.py gives a predicted price for a given mileage, based on computed theta_0 and theta_1. Thetas to be used are stored in a csv file - thetas.csv. If the file does not exist, the predicted price will be 0.

- train.py "trains" the model. For each mileage in the dataset, a function is called and returns w and b values in the equation y = wx + b that minimizes the difference between predicted and actual price. We will make the slope w take various values from -0.01 to 0.01 and update the b accordingly using the affine function equation. We will take all w and b values and get the mean from them. Resulting theta_0 will be the average of all computed b values and theta_1 will be the average of all computed w values.

- cost.py computes the square errors values, that is, the difference - always positive - between predicted price and actual price. It maps mileage and actual prices as well as a cost value which refers to the gap between predicted and actual price. We can see where there are major discrepancies in predicted vs accurate price. This is pointed out by a 'light' color in the figure.
