from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    class Meta:
        model = User #hangi modeli kullanacağımızı belirtiyoruz.
        fields = ('username', 'email', 'password1', 'password2')#göstermek istediğimiz inputları yazıyoruz.
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        # self.fields['username'].widget.attrs.update({'class':'form-control'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})