/* Silverbowl.co.ke – Main JS */
document.addEventListener('DOMContentLoaded', () => {

    /* ── Mobile nav ─────────────────────────────────────────── */
    const navToggle = document.querySelector('.nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', () => {
            navMenu.classList.toggle('open');
            navToggle.setAttribute('aria-expanded', navMenu.classList.contains('open'));
        });
        // close on outside click
        document.addEventListener('click', (e) => {
            if (!navToggle.contains(e.target) && !navMenu.contains(e.target)) {
                navMenu.classList.remove('open');
            }
        });
    }

    /* ── Sticky header ──────────────────────────────────────── */
    const header = document.querySelector('.site-header');
    if (header) {
        const onScroll = () => {
            header.classList.toggle('scrolled', window.scrollY > 50);
        };
        window.addEventListener('scroll', onScroll, { passive: true });
        onScroll();
    }

    /* ── FAQ Accordion ──────────────────────────────────────── */
    document.querySelectorAll('.faq-question').forEach((q) => {
        q.addEventListener('click', () => {
            const item = q.closest('.faq-item');
            const isOpen = item.classList.contains('open');
            // close all
            document.querySelectorAll('.faq-item').forEach(el => el.classList.remove('open'));
            if (!isOpen) item.classList.add('open');
        });
    });

    /* ── Back to top ────────────────────────────────────────── */
    const backTop = document.getElementById('back-top');
    if (backTop) {
        window.addEventListener('scroll', () => {
            backTop.classList.toggle('visible', window.scrollY > 400);
        }, { passive: true });
        backTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    }

    /* ── Inline search redirect ─────────────────────────────── */
    document.querySelectorAll('.search-form').forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const q = form.querySelector('input').value.trim();
            if (q) window.location.href = `/blog/?s=${encodeURIComponent(q)}`;
        });
    });

    /* ── Newsletter form ─────────────────────────────────────── */
    document.querySelectorAll('.newsletter-form').forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            const email = form.querySelector('input[type=email]').value.trim();
            if (!email) return;
            const btn = form.querySelector('button');
            btn.textContent = '✓ Subscribed!';
            btn.disabled = true;
            btn.style.background = '#0f7a4a';
            form.querySelector('input[type=email]').value = '';
        });
    });

    /* ── Smooth scroll for anchor links ─────────────────────── */
    document.querySelectorAll('a[href^="#"]').forEach(link => {
        link.addEventListener('click', (e) => {
            const target = document.querySelector(link.getAttribute('href'));
            if (target) {
                e.preventDefault();
                target.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    /* ── Lazy image intersection observer ───────────────────── */
    if ('IntersectionObserver' in window) {
        const imgs = document.querySelectorAll('img[data-src]');
        const io = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    io.unobserve(img);
                }
            });
        }, { rootMargin: '200px' });
        imgs.forEach(img => io.observe(img));
    }

    /* ── Blog Category Filter ───────────────────────────────── */
    const categoryButtons = document.querySelectorAll('.category-filter-btn');
    if (categoryButtons.length > 0) {
        const postCards = document.querySelectorAll('.post-card');

        const filterPosts = (filterValue) => {
            postCards.forEach(card => {
                if (filterValue === 'all') {
                    card.style.display = 'flex'; // post-card is flex usually, or block
                } else {
                    const cardCat = card.dataset.category;
                    if (cardCat === filterValue) {
                        card.style.display = 'flex';
                    } else {
                        card.style.display = 'none';
                    }
                }
            });
        };

        categoryButtons.forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.preventDefault();
                categoryButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filter = btn.dataset.filter;
                filterPosts(filter);
            });
        });

        // Handle URL parameter
        const urlParams = new URLSearchParams(window.location.search);
        const catParam = urlParams.get('cat');
        if (catParam) {
            const targetBtn = Array.from(categoryButtons).find(btn => btn.dataset.filter === catParam);
            if (targetBtn) {
                targetBtn.click();
            } else {
                filterPosts(catParam);
            }
        }
    }
});
