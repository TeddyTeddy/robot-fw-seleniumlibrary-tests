*** Keywords ***
Add Group With Permissions
    [Arguments]     ${group_name}       ${permissions}
    Enter Name For New Group    group_name=${group_name}
    FOR  ${permision}  IN   @{permissions}
        ${found_permissions} =  Enter Search Term In Available Permissions Filter   permission_search_term=${permision}
        Run Keyword If  ${found_permissions}    Choose All Filtered Permissions
        Clear Available Permissions Filter
    END
    Click On Save Button      # opens groups_page
    Verify Groups Page Loaded   group_name=${group_name}
    Verify Group Added     group_name=${group_name}

Delete Group
    [Arguments]     ${group_name}
    Select Checkbox For Group  group_name=${group_name}
    Select Delete Selected Groups Dropdown
    Press Go    # opens confirm_groups_deletions_page
    Verify Confirm Group Deletions Page     group_name=${group_name}
    Press Confirm Button
