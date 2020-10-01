from ExpectedTexts import expected

number_of_add_buttons = 3
number_of_change_buttons = 3

locator = {
    'admin_login_page': {
        'title': '//*[@id="site-name"]/a',
        'username_title': '//*[@id="login-form"]/div[1]/label',
        'username_field': '//*[@id="id_username"]',
        'password_title': '//*[@id="login-form"]/div[2]/label',
        'password_field': '//*[@id="id_password"]',
        'login_button': '//*[@id="login-form"]/div[3]/input'
    },
    'admin_main_page': {
        'main_title': '//*[@id="site-name"]/a',             # on the upper left corner
        'welcome_user_x': '//*[@id="user-tools"]',          # on the upper right corner, the navigation bar for the user
        'view_site': '//*[@id="user-tools"]/a[1]',          # on the upper right corner
        'change_password': '//*[@id="user-tools"]/a[2]',    # on the upper right corner
        'logout': '//*[@id="user-tools"]/a[3]',             # on the upper right corner
        'site_administration': '//*[@id="content"]/h1',      # under main_title
        # authentication and authorization section
        'authentication_and_authorization': '//*[@id="content-main"]/div[1]/table/caption/a',  # under site_administration
        'groups': '//*[@id="content-main"]/div[1]/table/tbody/tr[1]/th/a', # under authentication and authorization
        'users': '//*[@id="content-main"]/div[1]/table/tbody/tr[2]/th/a',  # under groups
        'add_group': '//*[@id="content-main"]/div[1]/table/tbody/tr[1]/td[1]/a',
        'change_group': '//*[@id="content-main"]/div[1]/table/tbody/tr[1]/td[2]/a',
        'add_user': '//*[@id="content-main"]/div[1]/table/tbody/tr[2]/td[1]/a',
        'change_user': '//*[@id="content-main"]/div[1]/table/tbody/tr[2]/td[2]/a',
        # postings section
        'postings': '//*[@id="content-main"]/div[2]/table/caption/a',      # under users
        'blog_posts': '//*[@id="content-main"]/div[2]/table/tbody/tr/th/a',     # under postings
        'add_blog_post': '//*[@id="content-main"]/div[2]/table/tbody/tr/td[1]/a',
        'change_blog_post': '//*[@id="content-main"]/div[2]/table/tbody/tr/td[2]/a',
        # generic add and change buttons
        'add_button': f'//div[@id="content-main"]//a[contains(., {expected["admin_main_page"]["add_button_text"]})]',    # in the upper center, 3 of them
        'change_button': f'//div[@id="content-main"]//a[contains(., {expected["admin_main_page"]["change_button_text"]})]',    # in the upper center, 3 of them
        # Recent Actions section
        'recent_actions': '//div[@id="recent-actions-module"]/h2',  # right column in the middle
        'my_actions': '//*[@id="recent-actions-module"]/h3'
    },
    'add_group_page': {
        'title': '//*[@id="content"]/h1',
        'breadcrumbs': '//*[@id="container"]/div[2]',
        'home_link': '//*[@id="container"]/div[2]/a[1]',
        'authentication_and_authorization_link': '//*[@id="container"]/div[2]/a[2]',
        'groups_link': '//*[@id="container"]/div[2]/a[3]',
        'add_group': '//*[@id="content"]/h1',
        'name': '//*[@id="group_form"]/div/fieldset/div[1]/div/label',
        'input_name_field': '//*[@id="id_name"]',
        'permissions': '//*[@id="group_form"]/div/fieldset/div[2]/div/label',
        'available_permissions_title': '//*[@id="group_form"]/div/fieldset/div[2]/div/div[1]/div/div[1]/h2',
        'input_permission_field': '//*[@id="id_permissions_input"]',
        'available_permissions_tooltip': '//*[@id="group_form"]/div/fieldset/div[2]/div/div[1]/div/div[1]/h2/span',
        'available_permissions_dropdown': '//*[@id="id_permissions_from"]',
        'generic_filtered_permission': '//*[@id="id_permissions_from"]/option',
        'choose_all_permissions_option': '//*[@id="id_permissions_add_all_link"]',
        'choose_all_permissions': '//*[@id="id_permissions_add_all_link"]',
        'help_to_select_multiple_permissions': '//*[@id="group_form"]/div/fieldset/div[2]/div/div[2]',
        'chosen_permissions_title': '//*[@id="group_form"]/div/fieldset/div[2]/div/div[1]/div/div[2]/h2',
        'chosen_permissions_tooltip': '//*[@id="group_form"]/div/fieldset/div[2]/div/div[1]/div/div[2]/h2/span',
        'chosen_permissions_dropdown': '//*[@id="id_permissions_to"]',
        'generic_chosen_permission': '//*[@id="id_permissions_to"]/option',
        'remove_all_permissions_option': '//*[@id="id_permissions_remove_all_link"]',
        'save_and_add_another_button': '//*[@id="group_form"]/div/div/input[2]',
        'save_and_continue_editing_button': '//*[@id="group_form"]/div/div/input[3]',
        'save_button': '//*[@id="group_form"]/div/div/input[1]',
    },
    'groups_page': {
        'breadcrumbs': '//*[@id="container"]/div[2]',
        'home_link': '//*[@id="container"]/div[2]/a[1]',
        'authentication_and_authorization_link': '//*[@id="container"]/div[2]/a[2]',
        'group_x_added_successfully': '//*[@id="container"]/ul/li[@class="success"]',
        'select_group_to_change': '//*[@id="content"]/h1',
        'add_group': '//*[@id="content-main"]/ul/li/a',
        'search_button': '//*[@id="changelist-search"]/div/input[2]',
        'action': '//*[@id="changelist-form"]/div[1]/label',
        'delete_selected_groups_option': f'//*[@id="changelist-form"]/div[1]/label/select/option[contains(.,"{expected["groups_page"]["delete_selected_groups_option_text"]}")]',
        'go_button': '//*[@id="changelist-form"]/div[1]/button',
        'x_of_y_selected': '//*[@id="changelist-form"]/div[1]/span',
        'select_all_groups': '//*[@id="result_list"]/thead/tr/th[2]/div[1]/span',
        'generic_group_element_checkbox': '//*[@id="result_list"]/tbody/tr[contains(.,"%s")]/td/input[@type="checkbox"]',
        'generic_group_element': '//table[@id="result_list"]/tbody/tr/th/a[contains(.,"%s")]',
        'y_groups': '//*[@id="changelist-form"]/p',
    },
    'confirm_groups_deletions_page': {
        'breadcrumbs': '//*[@id="container"]/div[2]',
        'home': '//*[@id="container"]/div[2]/a[1]',
        'authentication_and_authorization': '//*[@id="container"]/div[2]/a[2]',
        'groups': '//*[@id="container"]/div[2]/a[3]',
        'are_you_sure_headline': '//*[@id="content"]/h1',
        'are_you_sure_question': '//*[@id="content"]/p',
        'summary': '//*[@id="content"]/h2[1]',
        'objects': '//*[@id="content"]/h2[2]',
        'generic_group_element': '//*[@id="content"]/ul[2]/li/a[contains(.,"%s")]',
        'confirm_deletion_button': '//*[@id="content"]/form/div/input[4]',
        'cancel_deletion_button': '//*[@id="content"]/form/div/a',
    }
}