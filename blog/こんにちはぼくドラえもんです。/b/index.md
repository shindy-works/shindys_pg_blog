---
layout: page
title: "hoge"
date: 2020-05-24 10:15:03 +0900
categories: b
permalink: /blog/こんにちはぼくドラえもんです。/b/
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