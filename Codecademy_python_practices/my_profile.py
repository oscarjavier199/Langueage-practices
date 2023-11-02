# **kwargs practice

def build_profile(first, last, **user_info):
    """Function takes **kwargs to create a user profile"""

    user_info['First Name'] = first
    user_info['Last Name'] = last
    return user_info


user_profile = build_profile(
    'oscar', 'perez',
    field='Student',
    location='Colombia',
    device='Computer',
    member_since='2018',
)

print(user_profile)
