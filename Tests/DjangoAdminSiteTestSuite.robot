*** Settings ***
Documentation       This is a test suite for admin login page
Library             SeleniumLibrary
Library             ../Resources/AdminLoginPage.py
Library             ../Resources/AdminMainPage.py
Library             ../Resources/AddGroupPage.py
Library             ../Resources/GroupsPage.py
Library             ../Resources/ConfirmGroupsDeletionsPage.py
Resource            ../Resources/CommonKeywords.robot
Variables           ../Resources/CommonVariables.py
Suite Setup         Suite Setup
Suite Teardown      Suite Teardown

# To Run:
# robot  --pythonpath Resources --noncritical failure-expected -d Results/ -v browser:'firefox' Tests/DjangoAdminSiteTestSuite.robot

*** Keywords ***
Suite Setup
    Open Browser  browser=${browser}
    Maximize Browser Window

Suite Teardown
    Close Browser

*** Test Cases ***
Login As An Admin
    Go To Admin Login Page
    Login As Valid Admin User   # opens admin_main_page

Create "Blog Editors" Group
    Click On Add Group Button   # opens add_group_page
    Verify Add Group Page
    Add Group With Permissions  group_name=blog_editors     permissions=${BLOG_EDITORS_PERMISSIONS}     # opens groups_page

Create "Group Editors" Group
    Go To Admin Main Page
    Click On Add Group Button  # opens add_group_page
    Verify Add Group Page
    Add Group With Permissions  group_name=group_editors     permissions=${GROUP_EDITORS_PERMISSIONS}   # opens groups_page

Delete "Blog Editors" Group
    Delete Group  group_name=blog_editors

Delete "Group Editors" Group
    Delete Group  group_name=group_editors



