from django.shortcuts import render, redirect
from the_forum.articles.forms import ArticleCreateForm


# Create your views here.

# The GET method, which was used in the example earlier, appends name/value pairs to the URL. Unfortunately,
# the length of a URL is limited, so this method only works if there are only a few parameters.
# The URL could be truncated if the form uses a large number of parameters, or if the parameters contain large amounts
# of data. Also, parameters passed on the URL are visible in the address field of the browser not the best place for
# a password to be displayed.

# The alternative to the GET method is the POST method. This method packages the name/value pairs inside the body
# of the HTTP request, which makes for a cleaner URL and imposes no size limitations on the forms output.
# It is also more secure.

# @login_required
def add_article(request):
    # GET = view without change
    if request.method == 'GET':
        form = ArticleCreateForm()
    else:
        # POST = view and change
        form = ArticleCreateForm(request.POST)
        # if form.is_valid():
        #     pet = form.save(commit=False)
        #     pet.user = request.user
        #     pet.save()
        #     return redirect('details user', pk=request.user.pk)

    context = {
        'form': form,
    }

    return render(request, 'articles/article-add-page.html', context)
