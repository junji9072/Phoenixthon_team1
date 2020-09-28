const start = document.querySelector('.main-desc button');
const second_container = document.querySelector('.second-container');

let items, winH;

function initModule() {
    items = document.querySelectorAll("#scroll-effect");
    winH = window.innerHeight;
    addEventHandlers();
}

function addEventHandlers() {
    window.addEventListener("scroll", checkPosition);
    window.addEventListener("load", checkPosition);
    window.addEventListener("resize", initModule);
};

function checkPosition() {
    for (let i = 0; i < items.length; i++) {
        const posFromTop = items[i].getBoundingClientRect().top;
        if (winH > posFromTop) {
            items[i].classList.add("fade-in");
        }
    }
}

start.addEventListener('click', () => {
    const pos = second_container.offsetTop;
    scrollTo(0, pos);
})

initModule();