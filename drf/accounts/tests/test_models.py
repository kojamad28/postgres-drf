class TestCustomUser:

    def test_is_staff(self, user):
        assert user.is_staff is user.is_admin
