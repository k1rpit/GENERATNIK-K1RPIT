import secrets
import uuid

list_int = list(range(9999))

def mutat_basic(*,user: str,int_=list_int) -> str:
    user = user.swapcase()
    user += str(secrets.choice(int_))
    return user

def mutat_hard(*,user: str,int_=list_int) -> str:
    user = user.swapcase()
    user += str(secrets.choice(int_))
    user = f'{user}|{user}'

    user_list = user.split('|')
    user_list.insert(1,str(uuid.uuid4())[::10])
    user = "".join(user_list)
    return user
