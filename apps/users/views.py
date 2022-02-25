from urllib import request
from django.shortcuts import get_object_or_404, render
from django.views import View
from .forms import UserCreationForm, ProfileFillUpForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import UserModel
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import login

User = get_user_model()


class SignUpUserView(CreateView):
    model = UserModel
    form_class = UserCreationForm
    template_name = 'users/sign_up_page.html'
    context_object_name = 'form'

    def get_success_url(self):
        return reverse('users:user_detail')

    def form_valid(self, form):
        response = super().form_valid(form)
        print('self.object: ', self.object)
        login(request=self.request, user=self.object)
        return response


class UserDetailFillUpView(UpdateView):
    model = UserModel
    form_class = ProfileFillUpForm
    template_name = 'users/usermodel_form.html'
    # template_name = 'users/profile_edit.html'

    def get_object(self):
        # user_id = self.kwargs.get("pk")
        # return get_object_or_404(UserModel, id=user_id)
        return self.request.user

    def get_success_url(self):
        return reverse('users:user_detail')


class UserDetail(DetailView):
    model = UserModel
    context_object_name = 'user'
    template_name = 'users/profile_view.html'

    def get_object(self):
        # user_id = self.kwargs.get("pk")
        # return get_object_or_404(UserModel, id=user_id)
        return self.request.user

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        return context


class ChangePasswordView(View):

    def get(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user)
        return render(
            request,
            'users/change_password.html',
            {
                'form': form
            }
        )

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            return reverse('users:user_detail')

        return render(
            request,
            'users/change_password.html',
            {
                'form': form
            }
        )
