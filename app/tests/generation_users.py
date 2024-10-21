

def generation_users() -> list[tuple[str, bytes]]:
    list_logins = ['Sasha21', 'Fight13', 'helloworld11', 'viola44', 'milaninter09', 'spartak96', 'russianbear2000',
                   'soberforewer', 'kuzkinamat', 'rebenok2021']
    result = []
    for login in list_logins:
        hash_password = login.encode()
        result.append((login, hash_password))
    return result


users = generation_users()
