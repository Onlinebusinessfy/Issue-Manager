from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Issue, Status
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)

class IssueListView(ListView, UserPassesTestMixin):
    template_name = "pages/issues.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_name = self.request.user.team.name
        context["issue_list"] = (
            Issue.objects
            .filter(reporter__team__name=team_name)
            .order_by("-created_on")
        )
        return context
    
class AllIssuesListView(ListView, UserPassesTestMixin):
    template_name = "pages/all_issues.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["issue_list"] = Issue.objects.order_by("-created_on")
        return context

class IssueDetailView(DetailView):
    model = Issue
    template_name = "pages/detail.html"
    context_object_name = 'issue'

class IssueCreateView(CreateView):
    template_name="pages/new.html"
    model=Issue
    fields=['name', 'summary', 'description', 'reporter', 'assignee', 'status', 'priority_level']

class IssueUpdateView(UpdateView):
    template_name="pages/edit.html"
    model=Issue
    fields=['name', 'summary', 'description', 'reporter', 'assignee', 'status', 'priority_level']