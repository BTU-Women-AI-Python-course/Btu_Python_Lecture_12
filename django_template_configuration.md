# Django Temolate Configuration

To add a `templates` folder to your Django project, follow these steps:

### 1. Create the `templates` Directory
First, create a directory named `templates` at the root level of your Django project or inside one of your apps. For example:
```
my_project/
├── my_app/
│   ├── templates/
│   │   └── my_app/
│   │       └── example.html
│   └── ...
├── my_project/
│   ├── settings.py
│   └── ...
```
Or, you can have a global `templates` folder shared across all apps:
```
my_project/
├── templates/
│   └── example.html
├── my_app/
│   └── ...
└── my_project/
    └── settings.py
```

### 2. Configure the `TEMPLATES` Setting
In your `settings.py` file, you need to configure Django to know where to look for templates.

Open `settings.py` and find the `TEMPLATES` setting. It should look something like this:
```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add the path to your templates directory here
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
- **`DIRS`**: This is a list where you specify the paths to your template directories. Add the path to your `templates` folder here.
- **`APP_DIRS`**: When set to `True`, Django automatically looks for a `templates` directory in each app.

### 3. Use the Templates in Views
You can now reference templates in your views. For example:
```python
from django.shortcuts import render

def example_view(request):
    return render(request, 'example.html')
```
Or if the template is inside an app-specific folder:
```python
def example_view(request):
    return render(request, 'my_app/example.html')
```

### 4. Organizing Templates (Optional)
If you have multiple apps and want to organize your templates better, you can create subdirectories within the `templates` folder for each app:
```
my_project/
├── templates/
│   ├── my_app1/
│   │   └── example1.html
│   ├── my_app2/
│   │   └── example2.html
├── ...
```
And reference them accordingly in your views:
```python
def example1_view(request):
    return render(request, 'my_app1/example1.html')

def example2_view(request):
    return render(request, 'my_app2/example2.html')
```
