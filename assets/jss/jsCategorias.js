/* script para ajustar cards de grid al otro modo paginas categorias*/


const itemList = document.querySelector('.item-list-cat');
const gridViewBtn = document.getElementById('grid-active-btn');
const detailsViewBtn = document.getElementById('details-active-btn');

gridViewBtn.classList.add('active-btn');

gridViewBtn.addEventListener('click', () => {
    gridViewBtn.classList.add('active-btn');
    detailsViewBtn.classList.remove('active-btn');
    itemList.classList.remove('details-active');
});

detailsViewBtn.addEventListener('click', () => {
    detailsViewBtn.classList.add('active-btn');
    gridViewBtn.classList.remove("active-btn");
    itemList.classList.add("details-active");
});









perfilIcon.addEventListener('mouseover', () => {
    if (ventanaperfil.classList.contains('hide'))
    ventanaperfil.classList.remove('hide')
})

perfilIcon.addEventListener('mouseleave', () => {
    // if(wholeCartWindow.classList.contains('hide'))
    setTimeout(() => {
        if (ventanaperfil.inWindow === 0) {
            ventanaperfil.classList.add('hide')
        }
    }, 500)

})

ventanaperfil.addEventListener('mouseover', () => {
    ventanaperfil.inWindow = 1
})

ventanaperfil.addEventListener('mouseleave', () => {
    ventanaperfil.inWindow = 0
    ventanaperfil.classList.add('hide')
})
