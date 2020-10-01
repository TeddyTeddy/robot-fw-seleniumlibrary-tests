*** Settings ***
Documentation    Keywords available only to DjangoAdminSiteTestSuite.robot

*** Keywords ***
Start Maximized Browser
    Open Browser  browser=${BROWSER}
    Maximize Browser Window

Close Active Browser
    Close Browser

Add Group With Permissions
    [Arguments]     ${group_name}       ${permissions}
    Enter name for new group    group_name=${group_name}
    FOR  ${permision}  IN   @{permissions}
        ${found_permissions} =  Enter search term in available permissions filter   permission_search_term=${permision}
        Run Keyword If  ${found_permissions}    Choose all filtered permissions
        Clear Available Permissions Filter
    END
    Click on save button      # opens groups_page
    Verify groups page loaded   group_name=${group_name}
    Verify group added     group_name=${group_name}

Delete Group
    [Arguments]     ${group_name}
    Select Checkbox For Group  group_name=${group_name}
    Select Delete Selected Groups Dropdown
    Press Go    # opens confirm_groups_deletions_page
    Verify Confirm Group Deletions Page     group_name=${group_name}
    Press Confirm Button

Login As Admin
    Go to admin login page
    Login    ${CREDENTIALS}[valid_admin][username]     ${CREDENTIALS}[valid_admin][password]    # opens admin_main_page
    Verify admin main page      ${CREDENTIALS}[valid_admin][username]

Create Group
    [Arguments]     ${group_name}       ${permissions}
    Go To Admin Main Page
    Click On Add Group Button   # opens add_group_page
    Verify Add Group Page
    Add Group With Permissions  group_name=${group_name}     permissions=${permissions}     # opens groups_page

Create "Blog Editors" Group
    Create Group  group_name=${BLOG_EDITORS_GROUP_NAME}  permissions=${BLOG_EDITORS_PERMISSIONS}

Create "Group Editors" Group
    Create Group  group_name=${GROUP_EDITORS_GROUP_NAME}  permissions=${GROUP_EDITORS_PERMISSIONS}

Delete "Blog Editors" Group
    Delete Group  group_name=${BLOG_EDITORS_GROUP_NAME}

Delete "Group Editors" Group
    Delete Group  group_name=${GROUP_EDITORS_GROUP_NAME}
