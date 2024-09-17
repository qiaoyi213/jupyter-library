import bcrypt


def encode_password(password: str) -> str:
    """
    Encode the password through bcrypt
    :param password: str
    :return: str
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed.decode()


def check_password(password: str, hashed_password: str) -> bool:
    """
    check the password
    :param password: str
    :param hashed_password: str
    :return: bool
    """
    return bcrypt.checkpw(password.encode(), hashed_password.encode())
