var product_total_amt = document.getElementById('product_total_amt');
var cargoEnvio = document.getElementById('cargo-envio');
var total_cart_amt = document.getElementById('total_cart_amt');
var discountCode = document.getElementById('discount_code1');
const decreaseNumber = (incdec, itemprice) => {
    var itemval = document.getElementById(incdec);
    var itemprice = document.getElementById(itemprice);
    console.log(itemprice.innerHTML);
    // console.log(itemval.value);
    if (itemval.value <= 0) {
        itemval.value = 0;
    } else {
        itemval.value = parseInt(itemval.value) - 1;
        itemval.style.background = '#fff';
        itemval.style.color = '#000';
        itemprice.innerHTML = parseInt(itemprice.innerHTML) - 10000;
        product_total_amt.innerHTML = parseInt(product_total_amt.innerHTML) - 10000;
        total_cart_amt.innerHTML = parseInt(product_total_amt.innerHTML) + parseInt(cargo-envio.innerHTML);
    }
}
const increaseNumber = (incdec, itemprice) => {
    var itemval = document.getElementById(incdec);
    var itemprice = document.getElementById(itemprice);
    // console.log(itemval.value);
    if (itemval.value >= 5) {
        itemval.value = 5;
        alert('max 5 articulos');
        itemval.style.background = 'red';
        itemval.style.color = '#fff';
    } else {
        itemval.value = parseInt(itemval.value) + 1;
        itemprice.innerHTML = parseInt(itemprice.innerHTML) + 10000;
        product_total_amt.innerHTML = parseInt(product_total_amt.innerHTML) + 10000;
        total_cart_amt.innerHTML = parseInt(product_total_amt.innerHTML) + parseInt(cargo-envio.innerHTML);
    }
}
const discount_code = () => {
    let totalamtcurr = parseInt(total_cart_amt.innerHTML);
    let error_msj = document.getElementById('error_msj');
    if (discountCode.value === 'Estreno2023') {
        let newtotalamt = totalamtcurr - 10000;
        total_cart_amt.innerHTML = newtotalamt;
        error_msj.innerHTML = "Codigo valido!";
    } else {
        error_msj.innerHTML = "Codigo invalido :(";
    }
}

/*
const btnDecrementar = document.getElementById('btndecrementar');
const btnIncrementar = document.getElementById('btnincrementar');
const cantidadInput = document.getElementById('textbox');

btnDecrementar.addEventListener('click', function() {
  let cantidad = parseInt(cantidadInput.value);
  if (cantidad > 0) {
    cantidad--;
  }
  cantidadInput.value = cantidad;
});

btnIncrementar.addEventListener('click', function() {
  let cantidad = parseInt(cantidadInput.value);
  cantidad++;
  cantidadInput.value = cantidad;
});  */