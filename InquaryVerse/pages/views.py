from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = "pages/home.html"

class AboutPageView(TemplateView):
    template_name = "pages/about.html"

class ContactPageView(TemplateView):
    template_name = "pages/contact.html"

class InquiryCreateView(TemplateView):
    template_name = 'pages/inquiry_create.html'

class InquiryListView(TemplateView):
    template_name = "pages/inquiry_list.html"