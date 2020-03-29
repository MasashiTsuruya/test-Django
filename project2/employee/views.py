from django.views import generic
from .models import Employee
from .forms import SearchForm

class IndexView(generic.ListView):
    model = Employee
    paginate_by = 1

    def get_context_data(self):
        """テンプレートへ渡す辞書の作成"""
        context = super().get_context_data()
        context['form'] = SearchForm(self.request.GET) #もとの辞書にformを追加
        return context

    def get_queryset(self):
        """テンプレートへ渡すemployee_listの作成"""
        form = SearchForm(self.request.GET)
        form.is_valid() #これをしないとcleaned_dataが出来ない
        #まず全社員を取得
        queryset = super().get_queryset()

        #部署の選択があれば、部署で絞り込み(filter)
        department = form.cleaned_data['department']
        if department:
            queryset = queryset.filter(department = department)
        #サークルの選択があれば、サークルで絞り込み(filter)
        club = form.cleaned_data['club']
        if club:
            queryset = queryset.filter(club = club)
        return queryset
