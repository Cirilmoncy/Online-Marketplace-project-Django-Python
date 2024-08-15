from django import forms
from django.contrib.auth.models import User


class userregform(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password']
        widgets ={
            'username': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6  rounded-xl border'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6  rounded-xl border'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6  rounded-xl border'
            }),
            'email': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6  rounded-xl border'
            }),
            'password': forms.TextInput(attrs={
                'class': 'w-full py-4 px-6  rounded-xl border'
            })
        }
























# class LoginForm(AuthenticationForm):
#     username=forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Your username',
#         'class':'w-full py-4 px-6 rounded-xl'
#     }))
#     password=forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder': 'Your Password',
#         'class':'w-full py-4 px-6 rounded-xl'
#     }))




# class SignupForm(UserCreationForm):
#     class Meta:
#         model=User
#         fields=('username','first_name','last_name','email','password1','password2')

#     username=forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Your username',
#         'class':'w-full py-4 px-6 rounded-xl'
#     })) 

#     first_name=forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Your firstname',
#         'class':'w-full py-4 px-6 rounded-xl'
#     }))  

#     last_name=forms.CharField(widget=forms.TextInput(attrs={
#         'placeholder': 'Your lastname',
#         'class':'w-full py-4 px-6 rounded-xl'
#     }))   

#     email=forms.CharField(widget=forms.EmailInput(attrs={
#         'placeholder': 'Your email address',
#         'class':'w-full py-4 px-6 rounded-xl'
#     })) 
#     password1=forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder': 'Your Password',
#         'class':'w-full py-4 px-6 rounded-xl'
#     })) 
#     password2=forms.CharField(widget=forms.PasswordInput(attrs={
#         'placeholder': 'Repeat Password',
#         'class':'w-full py-4 px-6 rounded-xl'
#     }))  