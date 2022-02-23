
# Custom Token Authentication

Custom token autentication in this project we can override Django default User table and we use our customizable user table for token authentication







## API Reference

#### Get all items

```http
  Python
  Django
  Django Rest Framework
  Django-rest-auth
  
```



```Installation
pip install Django==3.2.10
pip install djangorestframework==3.13.1
pip install django-rest-auth
pip install django-rest-auth[with_social]


```

## Appendix

Important concepts 

why use binascii , OS, Lazy translation, Model verbose

binascii : Convert between binary and ASCII

OS: os module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system dependent functionality.

Lazy translation:
Use the lazy versions of translation functions in django.utils.translation (easily recognizable by the lazy suffix in their names) to translate strings lazily – when the value is accessed rather than when they’re called.

These functions store a lazy reference to the string – not the actual translation. The translation itself will be done when the string is used in a string context, such as in template rendering.

This is essential when calls to these functions are located in code paths that are executed at module load time.

This is something that can easily happen when defining models, forms and model forms, because Django implements these such that their fields are actually class-level attributes. For that reason, make sure to use lazy translations in the following cases:

Model fields and relationships verbose_name and help_text option values

You can mark names of ForeignKey, ManyToManyField or OneToOneField relationship as translatable by using their verbose_name options:
Just like you would do in verbose_name you should provide a lowercase verbose name text for the relation as Django will automatically titlecase it when required.

Model verbose names values:

It is recommended to always provide explicit verbose_name and verbose_name_plural options rather than relying on the fallback English-centric and somewhat naïve determination of verbose names Django performs by looking at the model’s class name

Reference:
https://docs.djangoproject.com/en/4.0/topics/i18n/translation/#lazy-translations




## Demo

Insert gif or link to demo


## Installation

Install usercustomtokenauth with npm

```bash
  npm install requirments.txt
```


    
## Optimizations

What optimizations did you make in your code? E.g. refactors, performance improvements, accessibility


## Tech Stack

**Client:** Django, Django Restframework

**Server:** Python



## Run Locally

Clone the project

```bash
  git clone https://link-to-project
```

Go to the project directory

```bash
Activate virtual envirnment
  cd usercustomtokenauth
  cd venv
  cd scripts
  activte
```

Install dependencies

```bash
  pip instll requirments.txt
```

Start the server

```bash
  python manage.py runserver
```






## Documentation

[Token authentication](https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication)

[Permissions](https://www.django-rest-framework.org/api-guide/permissions/)

[Lazy translation](https://docs.djangoproject.com/en/4.0/topics/i18n/translation/#lazy-translations)





## 🚀 About Me
I'm a Python Django Developer


## 🛠 Skills
Python, Django, Rest frmework, HTML, CSS


## Running Tests

To run tests, run the following command

```bash
  npm run test
```


# Hi, I'm Deepak Wankhede! 👋


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`API_KEY`

`ANOTHER_API_KEY`


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

