from django.contrib.auth.base_user import BaseUserManager

class GeekUserManager(BaseUserManager):
    def create_user (self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email должен быть задан обязательно")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        uswr.save()
        return user

    def create_superuser(self,email, password, **extra_fields ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)


        if extra_fields.get("is_staff") is not True:
            raise ValueError("Суперюзер должен иметь is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Суперюзер должен иметь is_superuser=True")
        return self.create_superuser(email, password, **extra_fields)