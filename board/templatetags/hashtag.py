import re

from django import template

register =template.Library()

@register.filter
def add_link(value):
    content=value.content #전달된 value 객체의 content맴버 변수 전달받음
    tags=value.tag_set.all() #전달된 value 객체의 tag_set 전체를 가져오는 queryset

    for tag in tags:
        content=re.sub(r'\#'+tag.name+r'\b','<a href="/board/tag/'+tag.name+'">#'+tag.name+'</a>', content)

    return content