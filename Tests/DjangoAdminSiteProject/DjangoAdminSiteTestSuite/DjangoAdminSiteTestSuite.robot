*** Settings ***
Documentation       This is a test suite for admin login page
Library             SeleniumLibrary
Resource            ../Common/CommonKeywords.robot
Resource            Resources/DjangoAdminSiteTestSuite_resource.robot
Suite Setup         Suite Setup
Suite Teardown      Suite Teardown

# To Run:
# robot  --pythonpath Libraries/Src --noncritical failure-expected -d Results/ -v browser:'firefox' Tests/DjangoAdminSiteProject/DjangoAdminSiteTestSuite/DjangoAdminSiteTestSuite.robot

*** Keywords ***
Suite Setup
    Open Browser  browser=${browser}
    Maximize Browser Window

Suite Teardown
    Close Browser

*** Test Cases ***
Login As An Admin
    Go To Admin Login Page
    Login   ${CREDENTIALS.valid_admin.username}     ${CREDENTIALS.valid_admin.password}     # opens admin_main_page
    Verify Admin Main Page      ${CREDENTIALS.valid_admin.username}

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



