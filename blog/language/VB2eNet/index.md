---
layout: page
title: "VB.Net"
date: 2020-06-01 00:00:13 +0900
categories: VB.Net
permalink: /blog/language/VB2eNet/
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