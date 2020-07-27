Crispy form was added to the project
pip install django-crispy-forms
Add cripsy to the seetings app
'crispy_forms',
Add this to the last section of settings 
CRISPY_TEMPLATE_PACK = 'bootstrap4'
{% load crispy_forms_tags %}
{{ form|crispy }}