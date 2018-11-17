from registration.backends.simple.views import RegistrationView


class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        # the named URL that we want to redirect to after 
        # successful registration
        return ('registration_create_cat')