const left_arrow = second_container.querySelector('.left-arrow'),
    right_arrow = second_container.querySelector('.right-arrow');

const army_card_view = document.querySelector('.army-card-view');
const army_card_list = document.querySelectorAll('.army-card');

const SELECT_CLASS = 'army-card-selected';
const CARD_WIDTH = 700;

let current_card = 0;

let cardPositions = [];

function initCardPosition() {
    let current_pos = CARD_WIDTH;
    [...army_card_list].forEach(() => cardPositions.push(current_pos -= CARD_WIDTH));
    army_card_list[0].classList.add(SELECT_CLASS);
}

function slideCard(x) {
    army_card_list[current_card].classList.remove(SELECT_CLASS);
    if (x < 0)
        current_card += 1;
    else
        current_card -= 1;

    console.log(current_card)
    if (current_card >= army_card_list.length)
        current_card = 0;
    else if (current_card < 0)
        current_card = army_card_list.length - 1;
    army_card_view.style.transform = `translate(${cardPositions[current_card]}px)`;
    army_card_list[current_card].classList.add(SELECT_CLASS);
}

left_arrow.addEventListener('click', () => {
    slideCard(1);
});

right_arrow.addEventListener('click', () => {
    slideCard(-1);
});

initCardPosition();