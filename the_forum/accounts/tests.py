from django.test import TestCase

# Create your tests here.

'''
class User(models.Model):
    .
    .
    def __str__(self):
        return self.nombre_del_sitio

class Profile(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    .
    .
    def __str__(self):
        return self.User.nombre_del_sitio
        
        

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['slug',]
        widgets = {
        'fecha_de_contratacion' : forms.DateInput(attrs={
          'type' : 'date',
          'class' : "form-control pull-right",
          'id' : "fechadecon",
           }),
        'User' : forms.Select(attrs={
          'type' : 'text',
          'class' : "form-control",
          'id' : 'nombresitio',
          }),
          .
          .
        }


class CrearSitiosContratadosView(CreateView):
    model = Profile
    template_name = 'sitios/contratados/editar_contratado.html'
    form_class = ProfileForm
    success_url = reverse_lazy('pagina:tabla_contratados')

class UpdateSitiosContratadosView(UpdateView):
    model = Profile
    second_model = User
    template_name = 'sitios/contratados/editar_contratado.html'
    form_class = ProfileForm
    second_form_class = UserForm
    success_url = reverse_lazy('pagina:tabla_contratados')

    def get_context_data(self, **kwargs):
        context = super(UpdateSitiosContratadosView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        Profile = self.model.objects.get(id=pk)
        User = self.second_model.objects.get(id=Profile.User_id)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=User)
            context['form2'] = self.second_form_class(instance=request.Profile.sitioproyecto)

        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_Profile = kwargs['pk']
        Profile = self.model.objects.get(id=id_Profile)
        User = self.second_model.objects.get(id=Profile.User_id)
        form = self.form_class(request.POST, instance=Profile)
        form2 = self.second_form_class(request.POST, instance=User)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


'''