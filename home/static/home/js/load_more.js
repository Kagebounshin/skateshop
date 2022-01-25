// Got some help from this site. https://www.markuptag.com/javascript-load-more-content-on-click-button/ with some modifications!

// Get Buttons
const btn_loadmore = document.querySelector('#btn_loadmore');
const btn_loadless = document.querySelector('#btn_loadless');
// Get images
const images = document.querySelectorAll('.rated-products');
let currentImages = 4;

// Disable btn_loadless 
function disable_loadless() {
    if (currentImages === 4) {
        btn_loadless.classList.add('disabled');
    } 
}

disable_loadless();

// Add eventlistener
btn_loadmore.addEventListener('click', (e) => {
    // loop through the images, selecting how many to show.
    for (let i = currentImages; i < currentImages + 4; i++) {
        if (images[i]) {
            images[i].style.display = 'block';
            images[i].style.animation = "fadeIn 1.5s";
        }
    }
    currentImages += 4;

    // Disable loadmore button 
    if (images.length <= currentImages) {
        btn_loadmore.disabled = true;
    } else {
        btn_loadless.classList.remove('disabled');
    }
});

// Add eventlistener
btn_loadless.addEventListener('click', (e) => {
    // loop through the images, selecting how many to remove.
    for (let i = currentImages; i > currentImages - 5; i--) {
        if (images[i]) {
            images[i].style.display = 'none';
        }
    }
    currentImages -= 4;
    // Disable loadless button 
    if (currentImages === 4) {
        btn_loadless.classList.add('disabled');
    } else {
        btn_loadmore.disabled = false;
    }
});