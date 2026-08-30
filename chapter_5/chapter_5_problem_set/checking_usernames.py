# create a list of your current user names
current_users = ['billy', 'starlight', 'homelander', 'vought', 'nairaease']
# create a list for new users
new_users = ['baba', 'verstapphen', 'billy', 'deep', 'homelander']
for users in new_users:
    if users in current_users:
        print(f"The username '{users}' is not available")
    else:
        print(f"The username '{users}' is available")