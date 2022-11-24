from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from the_forum.accounts.forms import UserCreateForm

''' 
1. index 
2. like_article 
3. dislike_article 
3. share_article 
4. comment_article 
'''
UserModel = get_user_model()


class HomeView(TemplateView):
    # TODO: should it redirect there
    template_name = 'common/home-page.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['hide_additional_nav_items'] = True
    #     context['profile'] = UserModel.objects.filter.get(user=UserModel.pk)
    #     return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('register user')
        return super().dispatch(request, *args, **kwargs)


'''
def show_index(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
        'profile': False,
    }

    return render(request, 'home-no-profile.html', context)
    
    
# we have created a CBV from the function above
class HomeView(RedirectToDashboard, TemplateView):
    template_name = 'main/home_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context
        
        
class DashboardView(ListView):
    model = Game
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hide_additional_fields = False
        context['games'] = Game.objects.all()
        return context
'''