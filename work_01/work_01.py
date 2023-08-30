from flask import Flask, render_template, request

"""Наборы данных для отображения """
_SHOES = {
    'title': 'Обувь',
    'main_title': 'Сезонная обувь',
    'dress_list': [
        {
            'dress_title': 'Ботинки',
            'dress_text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi at beatae dolor exercitationem quibusdam. Architecto asperiores aspernatur beatae dolorem excepturi facilis, nemo pariatur quaerat quam repellendus, sint, soluta voluptas voluptate.',
            'picture': '/static/img/snikers.webp',
        },
        {
            'dress_title': 'Сапоги',
            'dress_text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi at beatae dolor exercitationem quibusdam. Architecto asperiores aspernatur beatae dolorem excepturi facilis, nemo pariatur quaerat quam repellendus, sint, soluta voluptas voluptate.',
            'picture': '/static/img/snikers.webp',
        },
        {
            'dress_title': 'Туфли',
            'dress_text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi at beatae dolor exercitationem quibusdam. Architecto asperiores aspernatur beatae dolorem excepturi facilis, nemo pariatur quaerat quam repellendus, sint, soluta voluptas voluptate.',
            'picture': '/static/img/snikers.webp',
        }
    ]
}
_DRESSES = {
    'title': 'Одежда',
    'main_title': 'Одежда',
    'dress_list': [
        {
            'dress_title': 'Кепка',
            'dress_text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi at beatae dolor exercitationem quibusdam. Architecto asperiores aspernatur beatae dolorem excepturi facilis, nemo pariatur quaerat quam repellendus, sint, soluta voluptas voluptate.',
            'picture': '/static/img/dress.webp',
        },
        {
            'dress_title': 'Платье',
            'dress_text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi at beatae dolor exercitationem quibusdam. Architecto asperiores aspernatur beatae dolorem excepturi facilis, nemo pariatur quaerat quam repellendus, sint, soluta voluptas voluptate.',
            'picture': '/static/img/dress.webp',
        },
        {
            'dress_title': 'Джинсы',
            'dress_text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi at beatae dolor exercitationem quibusdam. Architecto asperiores aspernatur beatae dolorem excepturi facilis, nemo pariatur quaerat quam repellendus, sint, soluta voluptas voluptate.',
            'picture': '/static/img/dress.webp',
        }
    ]
}
_JACKET = {
    'prod_title': 'Классная куртка',
    'prod_text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi at beatae dolor exercitationem quibusdam. Architecto asperiores aspernatur beatae dolorem excepturi facilis, nemo pariatur quaerat quam repellendus, sint, soluta voluptas voluptate.',
    'picture': '/static/img/dress.webp'
}

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    """Главная стриница сайта."""
    return render_template('main.html')


@app.route('/shoes/')
@app.route('/dress/')
def clothes():
    """Обработчик для списков одежды или обуви."""
    if 'dress' in request.url:
        return render_template('prod_list.html', **_DRESSES)

    return render_template('prod_list.html', **_SHOES)


@app.route('/jacket/')
def jacket():
    """Обработчик для куртки."""
    return render_template('prod_detail.html', **_JACKET)


if __name__ == '__main__':
    app.run(debug=True)
