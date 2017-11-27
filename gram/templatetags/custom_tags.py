import re
from django import template
from django.core.urlresolvers import reverse, NoReverseMatch
from gram.models import Like

register = template.Library()

@register.simple_tag
def has_user_liked_post(post, user):
    try:
        like = Like.objects.get(post=post, user=user)
        return "fa-heart"
    except:
        return "fa-heart-o"


@register.simple_tag
def is_following(users_profile, profile_to_check):
    return users_profile.following.filter(user_id=profile_to_check.user_id).exists()



@register.filter(name='addClass')
def addClass(field, css):
   return field.as_widget(attrs={"class":css})


@register.filter(name='addID')
def addID(field, css):
   return field.as_widget(attrs={"id":css})


@register.simple_tag(takes_context=True)
def active(context, pattern_or_urlname):
    try:
        pattern = '^' + reverse(pattern_or_urlname)
    except NoReverseMatch:
        pattern = pattern_or_urlname
    path = context['request'].path
    if re.search(pattern, path):
        return 'active'
    return ''





