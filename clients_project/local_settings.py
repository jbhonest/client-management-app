from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'clients',  # replace with your desired database name
        'USER': 'clients_user',  # replace with your PostgreSQL username
        'PASSWORD': 'Clients_10925',  # replace with your PostgreSQL password
        'HOST': 'server.stockstats.ir',
        'PORT': '54032'
    }
}
print()
