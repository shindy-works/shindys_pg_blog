---
layout: page
title: "dart"
date: 2020-10-09 01:22:07 +0900
categories: dart
permalink: /blog/language/dart/
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