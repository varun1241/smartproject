from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
class RegistrationForm(UserCreationForm):

    class Meta:
        model =User

        fields=["username","first_name","last_name","email"]
class EditForm(UserChangeForm):

    class Meta:
        model =User

        fields=["username","first_name","last_name","email"]

    def __init__(self, *args, **kwargs): #the password field will be shown
        super().__init__(*args, **kwargs)
        del self.fields["password"]