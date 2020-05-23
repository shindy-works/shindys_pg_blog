---
layout: page
title: Blog
permalink: /blog/
---

<!-- 未完成ページURL -->
{% assign not_yet = site.baseurl | append:"/not_yet/" %}


<!-- カテゴリ取得（重複あり） -->
{% assign categories = "" | split: "" %}
    {% for p in site.pages %}
        {% if p.url contains "blog"  %}
            {% assign category = p.url | split: "/" %}
            {% if category[2] != nil and category[2] != "else" %}
                {% assign categories = categories | push: category[2] %}
            {% endif %}
        {% endif %}
{% endfor %}

<!-- カテゴリ重複削除 -->
{% assign categories = categories | uniq | sort %}
<!-- タイトル昇順のページ配列 -->
{% assign rev_pages = site.pages | reverse %}

{% for category in categories %}
### {{ category | capitalize_first }}
    {% for p in rev_pages %}
        {% if p.url contains category %}
- [{{ p.title | capitalize_first }}]({{ site.baseurl }}{{ p.url }})
        {% endif %}
    {% endfor %}
{% endfor %}

### Else
{% for p in rev_pages %}
    {% if p.url contains "else" %}
- [{{ p.title | capitalize_first }}]({{ site.baseurl }}{{ p.url }})
    {% endif %}
{% endfor %}
