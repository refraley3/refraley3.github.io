---
layout: default
---

<main class="photo-page">
  <article class="photo-article">
    <header class="photo-header">
      <h1>{{ page.title }}</h1>
      {% if page.date %}
        <p class="photo-date">{{ page.date | date: "%B %-d, %Y" }}</p>
      {% endif %}
    </header>

    <section class="photo-content">
      {{ content }}
    </section>

    {% if page.tags %}
    <footer class="photo-footer">
      <p>Tags:
        {% for tag in page.tags %}
          <a href="{{ '/tags/' | append: tag | relative_url }}" class="tag-link">{{ tag }}</a>{% unless forloop.last %}, {% endunless %}
        {% endfor %}
      </p>
    </footer>
    {% endif %}
  </article>
</main>
