expected = {
    'admin_login_page': {
        'title_text': 'Django administration',
        'username_text': 'Username:',
        'password_text': 'Password:',
        'login_button_text': 'Log in',
    },
    'admin_main_page': {
        'main_title_text': 'Django administration',         # on the upper left corner
        'dynamic_user_tab_text': 'WELCOME, %s. VIEW SITE / CHANGE PASSWORD / LOG OUT',
        'welcome_text': 'WELCOME,',                         # on the upper right corner
        'view_site_text': 'VIEW SITE',                      # on the upper right corner
        'change_password_text': 'CHANGE PASSWORD',          # on the upper right corner
        'logout_text': 'LOG OUT',                           # on the upper right corner
        'site_administration_text': 'Site administration',  # under main_title_text
        'authentication_and_authorization_text': 'AUTHENTICATION AND AUTHORIZATION',  # under site_administration_text
        'groups_text': 'Groups',                            # under authentication_and_authorization_text
        'users_text': 'Users',                              # under groups
        'postings_text': 'POSTINGS',                        # under users_text
        'blog_posts_text': 'Blog posts',                    # under postings_text
        'add_button_text': "'Add'",                         # in the upper central part, 3 of them
        'change_button_text': "'Change'",                   # in the upper central part, 3 of them
        'recent_actions_text': 'Recent actions',            # in the right column in the middle
        'my_actions_text': 'My actions',                    # on the right column in the middle
    },
    'add_group_page': {
        'breadcrumbs_text': 'Home › Authentication and Authorization › Groups › Add group',
        'add_group_text': 'Add group',
        'name_text': 'Name:',
        'permissions_text': 'Permissions:',
        'available_permissions_title_text': 'Available permissions',
        'available_permissions_dropdown_content': 'admin | log entry | Can add log entry\nadmin | log entry | Can change log entry\nadmin | log entry | Can delete log entry\nauth | group | Can add group\nauth | group | Can change group\nauth | group | Can delete group\nauth | permission | Can add permission\nauth | permission | Can change permission\nauth | permission | Can delete permission\nauth | user | Can add user\nauth | user | Can change user\nauth | user | Can delete user\ncontenttypes | content type | Can add content type\ncontenttypes | content type | Can change content type\ncontenttypes | content type | Can delete content type\npostings | blog post | Can add blog post\npostings | blog post | Can change blog post\npostings | blog post | Can delete blog post\nsessions | session | Can add session\nsessions | session | Can change session\nsessions | session | Can delete session',
        'admin-log_entry-can_add_log_entry': 'admin | log entry | Can add log entry',
        'admin-log_entry-can_change_log_entry': 'admin | log entry | Can change log entry',
        'admin-log_entry-can_delete_log_entry': 'admin | log entry | Can delete log entry',
        'auth-group-can_add_group': 'auth | group | Can add group',
        'auth-group-can_change_group': 'auth | group | Can change group',
        'auth-group-can_delete_group': 'auth | group | Can delete group',
        'auth-permission-can_add_permission': 'auth | permission | Can add permission',
        'auth-permission-can_change_permission': 'auth | permission | Can change permission',
        'auth-permission-can_delete_permission': 'auth | permission | Can delete permission',
        'auth-user-can_add_user': 'auth | user | Can add user',
        'auth-user-can_change_user': 'auth | user | Can change user',
        'auth-user-can_delete_user' : 'auth | user | Can delete user',
        'contenttypes-content type-can_add_content_type' : 'contenttypes | content type | Can add content type',
        'contenttypes-content type-can_change_content_type': 'contenttypes | content type | Can change content type',
        'contenttypes-content type-can_delete_content_type': 'contenttypes | content type | Can delete content type',
        'postings-blog post-can_add_blog_post': 'postings | blog post | Can add blog post',
        'postings-blog post-can_change_blog_post': 'postings | blog post | Can change blog post',
        'postings-blog post-can_delete_blog_post': 'postings | blog post | Can delete blog post',
        'sessions-session-can_add_session': 'sessions | session | Can add session',
        'sessions-session-can_change_session': 'sessions | session | Can change session',
        'sessions-session-can_delete_session': 'sessions | session | Can delete session',
        'available_permissions_tooltip_text': 'This is the list of available permissions. You may choose some by selecting them in the box below and then clicking the "Choose" arrow between the two boxes.',
        'choose_all_permissions_text': 'Choose all',
        'help_to_select_multiple_permissions_text': 'Hold down "Control", or "Command" on a Mac, to select more than one.',
        'chosen_permissions_text': 'Chosen permissions',
        'chosen_permissions_tooltip_text': 'This is the list of chosen permissions. You may remove some by selecting them in the box below and then clicking the "Remove" arrow between the two boxes.',
        'chosen_permissions_dropdown_text': '',
        'remove_all_permissions_text': 'Remove all',
        'save_and_add_another_button_text': 'Save and add another',
        'save_and_continue_editing_button_text': 'Save and continue editing',
        'save_button_text': 'Save',
    },
    'groups_page': {
        'breadcrumbs_text': 'Home › Authentication and Authorization › Groups',
        'home_link_text': 'Home',
        'authentication_and_authorization_link_text': 'Authentication and Authorization',
        'group_x_added_successfully_text': 'The group "%s" was added successfully.',
        'select_group_to_change_text': 'Select group to change',
        'search_button_text': 'Search',
        'action_text': 'Action:\n---------\nDelete selected groups',
        'delete_selected_groups_option_text': 'Delete selected groups',
        'go_button_text': 'Go',
        'select_all_groups_text': 'GROUP',
    },
    'confirm_groups_deletions_page': {
        'breadcrumbs_text': 'Home › Authentication and Authorization › Groups › Delete multiple objects',
        'are_you_sure_headline_text': 'Are you sure?',
        'are_you_sure_question_text': 'Are you sure you want to delete the selected group? All of the following objects and their related items will be deleted:',
        'summary_text': 'Summary',
        'objects_text': 'Objects',
        'confirm_deletion_button_text': "Yes, I'm sure",
        'cancel_deletion_button_text': "No, take me back",
    }
}
