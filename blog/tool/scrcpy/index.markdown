---
layout: page
title: scrcpy
permalink: /blog/tool/scrcpy/
---

<ul class="post-list"> {% for category in site.categories %} {% if category[0] == "/blog/tool/scrcpy" %} {% for post in category[1] %}{% assign months = "January|February|March|April|May|June|July|August|September|October|November|December" | split: "|" %} {% assign m = post.date | date: "%-m" | minus: 1 %} {% assign day = post.date | date: "%d" %} {% assign month = months[m] %} {% assign year = post.date | date: "%Y" %}
  <li><span class="post-meta">{{ month }} {{ day }}, {{ year }}</span>
  <h3>
    <a class="post-link" href="{{site.baseurl}}{{ post.url }}">
      {{ post.title }}
    </a>
  </h3></li>{% endfor %}{% endif %}{% endfor %}</ul>