from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .validators import CustomPasswordValidator
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(
        label="비밀번호",
        widget=forms.PasswordInput,
        validators=[CustomPasswordValidator()],
    )
    password2 = forms.CharField(label="비밀번호 확인", widget=forms.PasswordInput)
    birth_day = forms.DateField(widget=forms.DateInput(format="%m%d"))

    class Meta:
        model = User
        fields = (
            "email",
            "birth_day",
            "user_name",
            "nick_name",
        )

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다!")
        return password2

    def clean_birth_day(self):
        birth_day = self.cleaned_data.get("birth_day")
        if birth_day:
            birth_day = birth_day.strftime("%m%d")
        return birth_day

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    birth_day = forms.DateField(widget=forms.DateInput(format="%m%d"))

    class Meta:
        model = User
        fields = (
            "email",
            "birth_day",
            "user_name",
            "nick_name",
        )

    def clean_birth_day(self):
        birth_day = self.cleaned_data.get("birth_day")
        if birth_day:
            birth_day = birth_day.strftime("%m%d")
        return birth_day
