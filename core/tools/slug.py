from unidecode import unidecode


def slugify(title):
    symbol_mapping = (
        (" ", "-"),
        (".", "-"),
        (",", "-"),
        ("!", "-"),
        ("?", "-"),
        ("'", "-"),
        ('"', "-"),
        ("ə", "e"),
        ("ı", "i"),
        ("ö", "o"),
        ("ğ", "g"),
        ("ü", "u"),
        ("ş", "s"),
        ("ç", "c"),
    )

    title_url = title.strip().lower()

    for before, after in symbol_mapping:
        title_url = title_url.replace(before, after)

    return unidecode(title_url)

def __set_slug__(self):
            if self.cache_title != self.title:
                from core.models import Service  

                new_slug = slugify(self.title)
                difference = 1
                while Service.objects.filter(slug = new_slug).exists():
                    new_slug = slugify(self.title) + str(difference)
                    difference += 1

                self.slug = new_slug