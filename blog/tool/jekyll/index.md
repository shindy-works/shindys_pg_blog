---
layout: page
title: "Jekyll"
date: 2020-05-17 22:18:49 +0900
categories: jekyll
permalink: blog/tool/jekyll
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