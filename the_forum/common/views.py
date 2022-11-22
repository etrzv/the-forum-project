from django.shortcuts import render
from django.views.generic import TemplateView

from the_forum.accounts.forms import UserCreateForm

''' 
1. index 
2. like_article 
3. dislike_article 
3. share_article 
4. comment_article 
'''


class HomeView(TemplateView):
    # TODO: should it redirect there
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


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
'''