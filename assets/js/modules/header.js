/**
 * Aziz Studio Digital V2 - Header Module
 */

document.addEventListener('DOMContentLoaded', () => {
    initHeader();
});

function initHeader() {
    const header = document.getElementById('site-header');
    const navToggle = document.getElementById('mobile-nav-toggle');
    const primaryNav = document.getElementById('primary-navigation');
    const navLinks = document.querySelectorAll('.nav-link');

    if (!header || !navToggle || !primaryNav) return;

    // 1. Scroll Handler for Sticky Header animation
    const scrollThreshold = 50;
    
    function handleScroll() {
        if (window.scrollY > scrollThreshold) {
            header.classList.add('is-scrolled');
        } else {
            header.classList.remove('is-scrolled');
        }
    }

    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll(); // Call once immediately in case page is refreshed already scrolled

    // 2. Mobile Menu Toggling
    function openMenu() {
        navToggle.setAttribute('aria-expanded', 'true');
        primaryNav.classList.add('is-open');
        document.body.style.overflow = 'hidden'; // Prevent scrolling background
        
        // Accessibility: Focus first nav item
        const firstLink = primaryNav.querySelector('.nav-link');
        if (firstLink) {
            setTimeout(() => firstLink.focus(), 100);
        }
    }

    function closeMenu() {
        navToggle.setAttribute('aria-expanded', 'false');
        primaryNav.classList.remove('is-open');
        document.body.style.overflow = ''; // Restore scroll
        navToggle.focus();
    }

    navToggle.addEventListener('click', () => {
        const isExpanded = navToggle.getAttribute('aria-expanded') === 'true';
        if (isExpanded) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    // Close menu when clicking nav links (important for single-page hashes or mobile flows)
    navLinks.forEach(link => {
        link.addEventListener('click', () => {
            if (primaryNav.classList.contains('is-open')) {
                closeMenu();
            }
        });
    });

    // Close menu when pressing Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && primaryNav.classList.contains('is-open')) {
            closeMenu();
        }
    });

    // Keyboard Trap Focus inside mobile navigation when open
    primaryNav.addEventListener('keydown', (e) => {
        if (!primaryNav.classList.contains('is-open')) return;

        const focusableElements = primaryNav.querySelectorAll('a, button');
        const firstFocusable = focusableElements[0];
        const lastFocusable = focusableElements[focusableElements.length - 1];

        if (e.key === 'Tab') {
            if (e.shiftKey) { // Shift + Tab
                if (document.activeElement === firstFocusable) {
                    lastFocusable.focus();
                    e.preventDefault();
                }
            } else { // Tab
                if (document.activeElement === lastFocusable) {
                    firstFocusable.focus();
                    e.preventDefault();
                }
            }
        }
    });

    // 3. Active Link Detection
    function highlightActiveLink() {
        const currentPath = window.location.pathname;
        const currentFilename = currentPath.substring(currentPath.lastIndexOf('/') + 1);

        navLinks.forEach(link => {
            const linkHref = link.getAttribute('href');
            
            // Normalize names (e.g. index.html vs root /)
            const isHomeActive = (currentFilename === '' || currentFilename === 'index.html') && (linkHref === 'index.html');
            const isActive = isHomeActive || (currentFilename !== '' && currentFilename === linkHref);

            if (isActive) {
                link.classList.add('active');
                link.setAttribute('aria-current', 'page');
            } else {
                link.classList.remove('active');
                link.removeAttribute('aria-current');
            }
        });
    }

    highlightActiveLink();
}
