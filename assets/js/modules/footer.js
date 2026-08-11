/**
 * Aziz Studio Digital V2 - Footer Module
 */

document.addEventListener('DOMContentLoaded', () => {
    initFooter();
});

function initFooter() {
    const yearElement = document.getElementById('footer-year');
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
}
