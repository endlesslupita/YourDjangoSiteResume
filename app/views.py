"""
Definition of views.
"""
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.views.generic import CreateView, ListView
from .forms import PledgeForm
from .models import Pledge

YOUR_INFO = {
    'name' : 'Pledge My Part',
    'bio' : 'What will you do to promote diversity in tech?',
    'email' : '', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'tweettweet', # No @ symbol, just the handle.
    'github_username' : "fetchpush", 
    'headshot_url' : '', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
            })
    )
    
class PledgeView(CreateView):
    template_name = 'app/base.html'
    form_class = PledgeForm
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        return super(PledgeView, self).get_context_data(
            object_list=Pledge.objects.all(),
            attendee=YOUR_INFO,
            year=datetime.now().year,
            **kwargs
        )
    
    
class PledgeListView(ListView):
    model = Pledge
    template_name = 'app/pledge_list.html'