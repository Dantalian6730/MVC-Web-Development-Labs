from django.shortcuts import render


def homepage(request):
    data = {
        'header': 'Django Articles',
        'message': 'Добро пожаловать на сайт статей!'
    }

    return render(
        request,
        'homepage.html',
        context=data
    )


def about(request):
    data = {
        'header': 'О проекте Django Articles',
        'description': (
            'Django Articles — учебное веб-приложение '
            'для публикации и просмотра статей.'
        ),
        'features': [
            'Просмотр списка статей',
            'Просмотр подробной информации о статье',
            'Отображение изображений',
            'Регистрация пользователей',
            'Авторизация и выход из аккаунта'
        ],
        'technologies': [
            'Python',
            'Django',
            'HTML',
            'CSS',
            'SQLite'
        ]
    }

    return render(
        request,
        'about.html',
        context=data
    )