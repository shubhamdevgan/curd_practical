from django.contrib.auth.models import BaseUserManager


class UserModelManager(BaseUserManager):
    '''
        Objects Manager for Defualt User Model.
    '''

    def create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError("Email must be provided")

        user = self.model(
            username=email,
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email=None, username=None, password=None, *args, **kwargs):
        if not email:
            raise ValueError("Email must be provided")

        user = self.create_user(
            email=email, password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user
