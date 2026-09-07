from app.core.password_security import hash_password, verify_password

def test_hash_password():
    password = "abc"
    hashed_password = hash_password(password)
    assert hashed_password != password

def test_verify_password():
    password = "abc"
    password1 = "bcd"
    hashed_password = hash_password(password)
    assert verify_password(password, hashed_password)
    assert not verify_password(password1, hashed_password)