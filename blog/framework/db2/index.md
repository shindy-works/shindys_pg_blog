---
layout: page
title: "DB2"
date: 2020-10-06 00:21:10 +0900
categories: DB2
permalink: /blog/framework/db2/
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