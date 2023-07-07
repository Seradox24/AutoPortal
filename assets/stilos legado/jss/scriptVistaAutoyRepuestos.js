/*  funcion que me permite cambiar de imagen visualizacion producto    */
const imgs = document.querySelectorAll('.img-select a');
const imgBtns = [...imgs];
let imgId = 1;

imgBtns.forEach((imgItem) => {
    imgItem.addEventListener('click', (event) => {
        event.preventDefault();
        imgId = imgItem.dataset.id;
        slideImage();
    });
});

function slideImage(){
    const displayWidth = document.querySelector('.img-showcase img:first-child').clientWidth;

    document.querySelector('.img-showcase').style.transform = `translateX(${- (imgId - 1) * displayWidth}px)`;
}

window.addEventListener('resize', slideImage);
/**************************************************************************/


/* toggle titulos vistas individuales titulos los dos primeros */

const toggleDescripcion = document.querySelector('.titulo-descripcion'); 
const toggleInfoAdicional = document.querySelector('.titulo-info-adicional');
/* toggle  texto descripcion e info adicional */
const contentDescripcion = document.querySelector('.texto-descripcion');
const contentInfoAdicional = document.querySelector('.texto-info-adicional');

/* funciones toggle */

toggleDescripcion.addEventListener('click',  () => {
    contentDescripcion.classList.toggle('hidden');
});
toggleInfoAdicional.addEventListener('click',  () => {
    contentInfoAdicional.classList.toggle('hidden');
});
/**************************************************************************/

// Funciones Para aumentar cantidad del producto a comprar

const inputQuantity = document.querySelector('.input-cantidad');
const btnIncrement = document.querySelector('#incrementar');
const btnDecrement = document.querySelector('#reducir');

let valueByDefault = parseInt(inputQuantity.value);

// Funciones Click

btnIncrement.addEventListener('click', () => {
	valueByDefault += 1;
	inputQuantity.value = valueByDefault;
});

btnDecrement.addEventListener('click', () => {
	if (valueByDefault === 1) {
		return;
	}
	valueByDefault -= 1;
	inputQuantity.value = valueByDefault;
});