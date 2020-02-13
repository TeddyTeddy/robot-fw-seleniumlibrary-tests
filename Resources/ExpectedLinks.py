base_link = 'https://glacial-earth-31542.herokuapp.com/'

admin_login_page_url = f'{base_link}admin/login/?next=/admin/'
expected_admin_main_page_url = f'{base_link}admin/'
expected_add_group_page_url = f'{base_link}admin/auth/group/add/'
expected_groups_page_url = f'{base_link}admin/auth/group/'

links = {
    'admin_main_page': {
        'main_title_link': f'{base_link}admin/',           # on the upper left corner
        'view_site_link': f'{base_link}',                               # on the upper right corner
        'change_password_link': f'{base_link}admin/password_change/',   # on the upper right corner
        'logout_link': f'{base_link}admin/logout/',                     # on the upper right corner
        # authentication and authorization section
        'authentication_and_authorization_link': f'{base_link}admin/auth/',  # under site_administration_link
        'groups_link': f'{base_link}admin/auth/group/',                            # under authentication_and_authorization_link
        'users_link': f'{base_link}admin/auth/user/',                              # under groups
        'add_group_link': f'{base_link}admin/auth/group/add/',
        'change_group_link': f'{base_link}admin/auth/group/',
        'add_user_link': f'{base_link}admin/auth/user/add/',
        'change_user_link': f'{base_link}admin/auth/user/',
        # postings section
        'postings_link': f'{base_link}admin/postings/',  # under users_link
        'blog_posts_link': f'{base_link}admin/postings/blogpost/',                    # under postings_link
        'add_blog_post_link': f'{base_link}admin/postings/blogpost/add/',
        'change_blog_post_link': f'{base_link}admin/postings/blogpost/',
    },
    'add_group_page': {
        'home_link': f'{base_link}admin/',
        'authentication_and_authorization_link': f'{base_link}admin/auth/',
        'groups_link': f'{base_link}admin/auth/group/',
        'choose_all_permissions_link':  f'{base_link}admin/auth/group/add/#',
        'remove_all_permissions_link_inactive': '#',
    },
    'groups_page': {
        'home_link': f'{base_link}admin/',
        'authentication_and_authorization_link': f'{base_link}admin/auth/',
        'add_group_link': f'{base_link}admin/auth/group/add/',
    },
    'confirm_groups_deletions_page': {
        'home_link': f'{base_link}admin/',
        'authentication_and_authorization_link': f'{base_link}admin/auth/',
        'groups_link': f'{base_link}admin/auth/group/',
        'cancel_deletion_button_link': f'{base_link}admin/auth/group/#',
    }
}
