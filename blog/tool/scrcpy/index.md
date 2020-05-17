---
layout: page
title: scrcpy
categories: scrcpy
permalink: blog/tool/scrcpy
---

<ul class="post-list"> 
{% for category in site.categories %} 
  {% if category[0] == page.categories %}
    {% for post in category[1] %}
  <li><span class="post-meta">{{ post.date | date: "%-d %B %Y" }}</span>
    <h3>
      <a class="post-link" href="{{site.baseurl}}{{ post.url }}">
        {{ post.title }}
      </a>
    </h3>
  </li>
    {% endfor %}
  {% endif %}
{% endfor %}</ul>

<ul class="post-list"> 
</ul>