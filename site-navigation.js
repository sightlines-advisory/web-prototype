(function () {
  const toggle = document.querySelector('.menu-toggle');
  const navigation = document.querySelector('.header-nav');

  if (!toggle || !navigation) return;

  function closeMenu() {
    navigation.classList.remove('is-open');
    toggle.setAttribute('aria-expanded', 'false');
  }

  toggle.addEventListener('click', function () {
    const isOpen = navigation.classList.toggle('is-open');
    toggle.setAttribute('aria-expanded', String(isOpen));
  });

  navigation.querySelectorAll('a').forEach(function (link) {
    link.addEventListener('click', closeMenu);
  });

  document.addEventListener('keydown', function (event) {
    if (event.key === 'Escape') closeMenu();
  });

  window.matchMedia('(min-width: 761px)').addEventListener('change', function (event) {
    if (event.matches) closeMenu();
  });
}());
