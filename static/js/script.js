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
