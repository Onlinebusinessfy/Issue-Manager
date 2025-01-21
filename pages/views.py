from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name="pages/home.html"

class AboutPageView(TemplateView):
    template_name="pages/about.html"

class IssueListView(TemplateView):
    template_name="pages/issues.html"

class IssueDetailView(TemplateView):
    template_name="pages/detail.html"

class IssueCreateView(TemplateView):
    template_name="pages/new.html"

class IssueUpdateView(TemplateView):
    template_name="pages/edit.html"

class AllIssuesView(TemplateView):
    template_name="pages/all_issues.html"
