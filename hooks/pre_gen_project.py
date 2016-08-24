site_name = "{{ cookiecutter.site_name }}"
for character in site_name:
    if not character.isalnum() and character != "-":
        msg = "the site name {!r} contains an invalid chracter: {!r}"
        raise ValueError(msg.format(site_name, character))