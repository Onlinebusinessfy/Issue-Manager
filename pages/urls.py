from django.urls import path
from .views import HomePageView, AboutPageView, IssueListView, IssueDetailView, IssueCreateView, AllIssuesView
from issues import views

urlpatterns=[
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("issues/", views.IssueListView.as_view(), name="issues"),
    path("issues/<int:pk>/", views.IssueDetailView.as_view(), name="detail"),
    path("new/", views.IssueCreateView.as_view(), name="new"),
    path("<int:pk>/edit/", views.IssueUpdateView.as_view(), name="edit"),
    path("allissues/", views.AllIssuesListView.as_view(), name="all_issues" )
]