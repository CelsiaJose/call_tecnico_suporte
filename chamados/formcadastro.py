from django import forms
from django.contrib.auth.forms import UserCreationForm #permite validar senha
from django.contrib.auth.models import User

#forms.ModelForm) Aqui nao se tira do form mas do Usercreation
class formCadastro(UserCreationForm): 
    email = forms.EmailField(required=True)
    class Meta:
         model=User
         fields= ('username','email','password','password2')
         widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Nome de usuário',
                'class': 'form-control'})}
         labels = {
            'username': 'Usuário',
            'email': 'Email',
            'password': 'Senha',
            'password2': 'Confirme a senha',
                 }
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email já cadastrado")
        return email

    #Para pegar valores dos form vou depois tentar esta forma
    '''if form.is_valid():
    username = form.cleaned_data['username']
    email = form.cleaned_data['email']
    password = form.cleaned_data['password1']'''
