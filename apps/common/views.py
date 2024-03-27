import json
from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.core.serializers.json import DjangoJSONEncoder
from apps.common.models import Position, Event
from apps.common.models import Post


class HomeView(generic.ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all()


class AboutView(generic.ListView):
    model = Post
    template_name = "about.html"


class PostList(generic.ListView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        slug = self.kwargs["slug"]
        return Post.objects.get(slug=slug)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        slug = self.kwargs["slug"]
        post = get_object_or_404(Post, slug=slug)

        context["post"] = post

        tags = post.tag.all()
        context["tags"] = tags

        if post:
            post.views += 1
            post.save()

        return context


class EventListView(generic.ListView):
    model = Event
    template_name = "event.html"

    def get_queryset(self):
        queryset = Event.objects.all()
        return queryset


class LocationsView(generic.ListView):
    model = Position
    template_name = "location.html"
    context_object_name = "positions"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any):
        event_id = self.kwargs["id"]
        posotions = list(
            Position.objects.filter(event_id=event_id).values("latitude", "longitude")
        )
        event_title = Event.objects.get(pk=event_id)
        return render(
            request,
            "location.html",
            context={"positions": posotions, "event_title": event_title},
        )
