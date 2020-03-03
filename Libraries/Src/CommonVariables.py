from ExpectedTexts import expected

BLOG_EDITORS_PERMISSIONS = [expected['add_group_page']['postings-blog post-can_add_blog_post'],
                            expected['add_group_page']['postings-blog post-can_change_blog_post'],
                            expected['add_group_page']['postings-blog post-can_delete_blog_post']]

GROUP_EDITORS_PERMISSIONS = [expected['add_group_page']['auth-group-can_add_group'],
                             expected['add_group_page']['auth-group-can_change_group'],
                             expected['add_group_page']['auth-group-can_delete_group']]


def get_variables():
    variables = {
        'BROWSER': 'ff',
        # 'HOST_URL': 'https://glacial-earth-31542.herokuapp.com/admin/login/?next=/admin/',
        'CREDENTIALS': {
                'valid_admin': {
                    'username': 'hakan',
                    'password': 'h1a2k3a4',
                },
        },
        'BLOG_EDITORS_PERMISSIONS': BLOG_EDITORS_PERMISSIONS,
        'GROUP_EDITORS_PERMISSIONS': GROUP_EDITORS_PERMISSIONS,
    }
    return variables

