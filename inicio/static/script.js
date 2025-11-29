document.addEventListener('DOMContentLoaded', function() {
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    // ===============================================
    // 1. Funcionalidad del Menú de Hamburguesa para móviles
    // ===============================================
    menuToggle.addEventListener('click', function() {
        navLinks.classList.toggle('active');

        // Cambia el ícono
        const icon = menuToggle.querySelector('i');
        if (navLinks.classList.contains('active')) {
            icon.classList.remove('fa-bars');
            icon.classList.add('fa-times'); // Icono de 'X' para cerrar
        } else {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-bars'); // Icono de hamburguesa
        }
    });

    // Cierra el menú cuando se hace clic en un enlace (en móvil)
    const links = document.querySelectorAll('.nav-links a');
    links.forEach(link => {
        link.addEventListener('click', () => {
            if (window.innerWidth <= 768) {
                navLinks.classList.remove('active');
                menuToggle.querySelector('i').classList.remove('fa-times');
                menuToggle.querySelector('i').classList.add('fa-bars');
            }
        });
    });
    
    // NOTA: La lógica del contador animado fue removida en este archivo.
});