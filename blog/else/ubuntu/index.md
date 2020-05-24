---
layout: page
title: "ubuntu"
date: 2020-05-23 12:54:38 +0900
categories: ubuntu
permalink: /blog/else/ubuntu/
---

<ul class="post-list"> 
{% for category in site.categories %}
  {% if category[0] == page.categories %} 
    {% for post in category[1] %}
  <li><span class="post-meta">{{ page.date | date: "%B %-d %Y" }}</span>
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