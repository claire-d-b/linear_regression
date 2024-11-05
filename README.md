python -m venv venv
source venv/bin/activate

pip install numpy matplotlib pandas
pip install flake8
alias norminette=flake8

deactivate
