from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

class OnlyLoggedsuperUser(UserPassesTestMixin,LoginRequiredMixin):
    def test_func(self):
        return self.request.user.is_superuser