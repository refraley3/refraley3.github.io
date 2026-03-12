---
layout: default
title: Fungi Field Notes
---

## Fungi Field Notes

This section is a working field notebook focused on the observation and identification of fungi encountered during photography and field exploration.

The emphasis is on **recognizable field characters**—growth form, substrate, color, texture, and seasonal appearance—combined with photographic documentation. Many fungi require microscopic examination or spore analysis for definitive identification, so these notes often remain **provisional or observational rather than taxonomically final**.

Content in this section may include:
- Field observations recorded across seasons and locations  
- Substrate and habitat associations  
- Diagnostic surface features and growth patterns  
- Comparisons between similar fungi  
- Photographic documentation supporting identification  

This material is intentionally separated from the Gallery.  
The Gallery presents fungi as photographic subjects; these field notes explore them as biological organisms.

Both perspectives inform one another.

---

### Observations

Current fungi documented in the field notes:


{% assign fungi_pages = site.pages | where_exp: "page", "page.path contains 'field-notes/fungi/'" %}

<ul>
{% for page in fungi_pages %}
  {% unless page.name == "index.md" %}
    <li>
        <a href="{{ page.url }}">
            {{ page.title }}{% if page.common_name %} — {{ page.common_name }}{% endif %}
        </a>
    </li>
  {% endunless %}
{% endfor %}
</ul>

---

### Orientation

These notes are organized as individual field observations rather than a complete catalog of fungal species. Additional pages may eventually explore broader topics such as fungal growth forms, rust fungi life cycles, wood-decay fungi, and seasonal fruiting patterns.

<p style="text-align:center">
	<img src="/assets/images/under-construction_wht.png" class="cover" alt="Under Construction" role="img" aria-label="Under Construction" />
</p>

---
