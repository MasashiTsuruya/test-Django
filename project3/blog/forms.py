from django import forms
from .models import Comment

class CommentCreateForm(forms.ModelForm):
    """
        親クラス(ModelForm)の__init__を上書きして、
        htmlのinput要素の全てにcssクラスを追加する。
        この処理を書くことによって、bootstrapなどのフレームワークを利用することが出来る。
        また、この処理をしたい時はviews.pyでform_class='xxx'と指定する必要がある。
        """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ('name', 'text')