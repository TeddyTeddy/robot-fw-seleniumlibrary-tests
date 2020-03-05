python setup_pythonpath.py
FOR /F "tokens=* USEBACKQ" %%F IN (`findstr /v "*" "pythonpath.txt"`) DO (
SET PYTHONPATH=%%F
)

coverage run --branch AdminLoginPageUT/AdminLoginPageUT.py
coverage run --branch -a AdminMainPageUT/AdminMainPageUT.py
coverage run --branch -a AddGroupPageUT/AddGroupPageUT.py
coverage run --branch -a ConfirmGroupsDeletionsPageUT/ConfirmGroupsDeletionsPageUT.py
coverage run --branch -a GroupsPageUT/GroupsPageUT.py
coverage html