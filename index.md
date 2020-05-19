---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults
title: Home
layout: page #home
---
<!-- 更新履歴ボックス -->
<style type="text/css">
    .kousin {
        overflow:auto;
        height:256px;
        padding:8px;
    }
</style>



# はじめに
***
> Hello World!

当サイトではプログラミングをしていて「ふ～ん」と思ったことから普段使いそうなツールの紹介まで、自由に投稿していきます！  
※メモ代わりでもあるため、記事によって質にムラがあります。ご了承ください。  
[ブログ]({{site.baseurl}}/blog/)へ

# 更新履歴
***
<div class="kousin">
    {% for post in site.posts limit:10 %}
    {% if post.upload_date != post.date %}
    <font color="#00C000">[UPDATE]</font>
    {% else %}
    <font color="#ff4500">[UPLOAD]</font>
    {% endif %}
    {{ post.date | date: "%B %-d %Y" }} :   
    <a href="{{site.baseurl}}{{ post.url }}">
      {{ post.title }}
    </a> <br>
    {% endfor %}
</div>

# 今まで勉強してきた言語
***
- **Programing**
    - **C言語**  
        最初に勉強した言語。正直もう覚えてない。

    - **C++**  
        ゼミ配属されてから使い始めた言語。この言語でオブジェクト指向を勉強。  
        ImGuiというGUIライブラリで色々作ってた。

    - **Java**  
        android使いとしてある程度コードは読めた方がいいだろうと勉強してる。

    - **Python**  
        ゼミでメインに使ってた言語。機械学習で使うと思いきやGUIを作ってた。  
        簡単（楽）にかけるし大好きな言語の一つ。

    - **Kotlin**  
        Javaと同じ理由だけど、新しい言語！って感じで面白そうだったから勉強した。結構好き。

    - **VB.Net**  
        最近勉強中の言語。今までGUI開発向けでない言語で作ってたからかなり開発が捗りそう。

    - **C#**  
        Unity使ったことないのに質問されたから勉強してみた。VB.Netとほとんど変わらない。  
        Unityに関してはモデル作るのが面倒で2Dしか触れてない。

- **Markup**
    - **HTML**, **CSS**  
        高校の情報の授業で触ったことがあるくらい。Web系は詳しくない。

    - **kv言語**  
        PythonのGUIライブラリ「Kivy」でGUIを作成するときにレイアウトや基本動作を楽に設定できるマークアップ言語。CSSに近いのかな。