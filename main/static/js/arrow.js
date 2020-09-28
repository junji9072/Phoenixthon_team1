const left_arrow = document.querySelector('.left-arrow'),
    right_arrow = document.querySelector('.right-arrow');

const army = document.querySelector('.army'),
    ul = army.querySelector('.army-item'),
    li = ul.querySelectorAll('li');

let currentPosition = 683.75;
const slideWidth = 683.75;
const startNum = 1;

function moveLeft(positive)
{
    currentPosition += +`${positive ? '+' : '-'}${(slideWidth * (startNum))}`;
    ul.style.transform = `translate3d(${currentPosition}px, 0px, 0px)`;
}

// Event
left_arrow.addEventListener('click', () => {
    console.log('left');
    moveLeft(true);
});

right_arrow.addEventListener('click', () => {
    console.log('right');
    moveLeft(false);
});