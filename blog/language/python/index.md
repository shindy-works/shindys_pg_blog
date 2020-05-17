---
layout: page
title: "Python"
date: 2020-05-17 22:24:17 +0900
categories: python
permalink: blog/language/python
---

<ul class="post-list"> 
{% for category in site.categories %}
  {% if category[0] == page.categories %} 
    {% for post in category[1] %}
  <li><span class="post-meta">{{ page.date | date: "%-d %B %Y" }}</span>
    <h3>
      <a class="post-link" href="{{ site.baseurl }}{{ post.url }}">
        {{ post.title }}
      </a>
    </h3>
  </li>
    {% endfor %}
  {% endif %}
{% endfor %}
</ul>