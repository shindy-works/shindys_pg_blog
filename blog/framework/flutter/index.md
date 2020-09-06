---
layout: page
title: "flutter"
date: 2020-09-06 00:43:54 +0900
categories: flutter
permalink: /blog/framework/flutter/
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