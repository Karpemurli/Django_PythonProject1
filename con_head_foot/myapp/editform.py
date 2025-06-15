from django import  forms
from .models import Register
from .models import Contactpages

class EditUserForm(forms.ModelForm):
    class Meta:
        model = Register
        fields ='__all__'
        # fields = ['username','email','password'] #separate field pahije asli tr.

    def __init__(self,*args, **kwargs):
        super(EditUserForm,self).__init__(*args,**kwargs)
        self.fields['address'].required = False

class EditContactForm(forms.ModelForm):
    class Meta:
        model = Contactpages
        fields ='__all__'

    def __init__(self,*args,**kwargs):
        super(EditContactForm,self).__init__(*args, **kwargs)
        self.fields['message'].required = False