from django import forms


class CommentForm(forms.Form):

    name = forms.CharField(label='名称', max_length=20, error_messages={
        'required': '请填写您的称呼',
        'max_length': '称呼过长，请重新输入',
    })
    email = forms.CharField(label='邮箱', error_messages={
        'required': '请填写您的邮箱',
        'invalid': '邮箱格式不正确',
    })
    content = forms.CharField(label='内容', error_messages={
        'required': '请填写您的内容',
        'max_length': '评论内容太长',
    })
