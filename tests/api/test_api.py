import pytest


@pytest.mark.change
def test_remove_name(user):
    user.name = ''
    assert user.name == ''


@pytest.mark.check
def test_name(user):
    assert user.name == "Nadiia"


@pytest.mark.check
def test_second_name(user):
<<<<<<< HEAD
    assert user.second_name == "Makliak"    
=======
    assert user.second_name == "Makliak"
>>>>>>> b2d02cb (lost in commits)
