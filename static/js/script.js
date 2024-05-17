$('.owl-carousel').owlCarousel({
    loop:false,
    margin:10,
    nav:false,
    responsive:{
        0:{
            items:1
        },
        600:{
            items:3
        },
        1000:{
            items:5
        }
    }
})

document.addEventListener('DOMContentLoaded', function() {
    const popUpBackground = document.querySelector('.pop-up-background');
    const popUpCard = document.querySelector('.pop-up-card');
    const closeButton = document.querySelector('.close-add-chat');
    const openButton = document.querySelector('.add-chat');

    closeButton.addEventListener('click', function() {
        popUpCard.classList.add('hide');
        setTimeout(() => {
            popUpBackground.style.display = 'none';
        }, 500);
    });
    openButton.addEventListener('click', function() {
        popUpCard.classList.remove('hide');
        setTimeout(() => {
            popUpBackground.style.display = 'block';
        }, 500);
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const searchField = document.getElementById('searchfield-friend');
    const listItems = document.querySelectorAll('.scrollable-list li');

    searchField.addEventListener('input', function() {
        const searchText = this.value.trim().toLowerCase();

        listItems.forEach(function(item) {
            const text = item.textContent.toLowerCase();
            if (text.includes(searchText)) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const frnd = document.getElementById('friend');
    const no_frnd = document.getElementById('non-friend');
    const all_users = document.getElementById('all-users');
    const listItems = document.querySelectorAll('.scrollable-list li');

    frnd.addEventListener('click', function() {

        listItems.forEach(function(item) {
            if (item.classList.contains('in-friend-list')) {
                item.style.display = 'block';
            }
            else if(item.classList.contains('favorites')){
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    });
    no_frnd.addEventListener('click', function() {
        
        listItems.forEach(function(item) {
            if (item.classList.contains('not-in-friend-list')) {
                item.style.display = 'block';
            }
            else if(item.classList.contains('favorites')){
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    });
    all_users.addEventListener('click', function() {
        
        listItems.forEach(function(item) {
            item.style.display = 'block';
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    // Обработчик события для кнопки "Добавить в друзья"
    document.querySelectorAll('.add-friend').forEach(button => {
        button.addEventListener('click', function() {
            const userId = this.dataset.userId; // Получаем id пользователя из атрибута data-user-id
            addToFriendList(userId);
        });
    });

    // Обработчик события для кнопки "Удалить из друзей"
    document.querySelectorAll('.remove-friend').forEach(button => {
        button.addEventListener('click', function() {
            const userId = this.dataset.userId; // Получаем id пользователя из атрибута data-user-id
            removeFromFriendList(userId);
        });
    });

    // Функция для добавления пользователя в список друзей
    function addToFriendList(userId) {
        const csrftoken = getCookie('csrftoken');
        // Отправляем AJAX-запрос на сервер
        fetch('/add-friend/', {
            method: 'POST',
            body: JSON.stringify({ userId: userId }),
            headers: {
                "Content-type": "application/json;",
                'X-CSRFToken': csrftoken,
            },
        })
        .then(response => {
            if (response.ok) {
                // Обновляем страницу или выполняем другие действия при успешном добавлении в друзья
                location.reload(); // Например, обновляем страницу
            } else {
                console.error('Ошибка при добавлении в друзья');
            }
        })
        .catch(error => {
            console.error('Произошла ошибка', error);
        });
    }

    // Функция для удаления пользователя из списка друзей
    function removeFromFriendList(userId) {
        const csrftoken = getCookie('csrftoken');
        // Отправляем AJAX-запрос на сервер
        fetch('/remove-friend/', {
            method: 'POST',
            body: JSON.stringify({ userId: userId }),
            headers: {
                "Content-type": "application/json;",
                'X-CSRFToken': csrftoken,
            },
        })
        .then(response => {
            if (response.ok) {
                // Обновляем страницу или выполняем другие действия при успешном удалении из друзей
                location.reload(); // Например, обновляем страницу
            } else {
                console.error('Ошибка при удалении из друзей');
            }
        })
        .catch(error => {
            console.error('Произошла ошибка', error);
        });
    }
});

function getCookie(name) {
    const cookieValue = document.cookie.match('(^|;)\\s*' + name + '\\s*=\\s*([^;]+)');
    return cookieValue ? cookieValue.pop() : '';
}


