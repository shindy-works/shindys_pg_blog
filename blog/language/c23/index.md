---
layout: page
title: "c#"
date: 2020-05-18 22:08:33 +0900
categories: c#
permalink: blog/language/c23
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