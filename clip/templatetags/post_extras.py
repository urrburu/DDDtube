from django import template
import re

register = template.Library()

@register.filter
def add_link(value):
    contents = value.contents # 전달된 value 객체의 content 멤버변수를 가져온다.
    tags = value.tag_set.all() # 전달된 value 객체의 tag_set 전체를 가져오는 queryset을 리턴한다.
    # tags의 각각의 인스턴를(tag)를 순회하며, content 내에서 해당 문자열을 => 링크를 포함한 문자열로 replace 한다.
    for tag in tags:
        contents = re.sub(r'\#'+tag.name+r'\b', '<a href="/clip/tags/'+tag.name+'">#'+tag.name+'</a>', contents)
    return contents # 원하는 문자열로 치환이 완료된 content를 리턴한다.
