/* SCRIPT DE NAVBAR DESDE AQUI*/

let submenu = document.getElementById("menusub");

function toggleMenu() {
    submenu.classList.toggle("open-menu");
}


(() => {

    const openNavMenu = document.querySelector(".open-nav-menu"),
        closeNavMenu = document.querySelector(".close-nav-menu"),
        navMenu = document.querySelector(".nav-menu"),
        menuOverlay = document.querySelector(".menu-overlay"),
        mediaSize = 991;

    openNavMenu.addEventListener("click", toggleNav);
    closeNavMenu.addEventListener("click", toggleNav);
    // close the navMenu by clicking outside
    menuOverlay.addEventListener("click", toggleNav);

    function toggleNav() {
        navMenu.classList.toggle("open");
        menuOverlay.classList.toggle("active");
        document.body.classList.toggle("hidden-scrolling");
    }

    navMenu.addEventListener("click", (event) => {
        if (event.target.hasAttribute("data-toggle") &&
            window.innerWidth <= mediaSize) {
            // prevent default anchor click behavior
            event.preventDefault();
            const menuItemHasChildren = event.target.parentElement;
            // if menuItemHasChildren is already expanded, collapse it
            if (menuItemHasChildren.classList.contains("active")) {
                collapseSubMenu();
            }
            else {
                // collapse existing expanded menuItemHasChildren
                if (navMenu.querySelector(".menu-item-has-children.active")) {
                    collapseSubMenu();
                }
                // expand new menuItemHasChildren
                menuItemHasChildren.classList.add("active");
                const subMenu = menuItemHasChildren.querySelector(".sub-menu");
                subMenu.style.maxHeight = subMenu.scrollHeight + "px";
            }
        }
    });
    function collapseSubMenu() {
        navMenu.querySelector(".menu-item-has-children.active .sub-menu")
            .removeAttribute("style");
        navMenu.querySelector(".menu-item-has-children.active")
            .classList.remove("active");
    }
    function resizeFix() {
        // if navMenu is open ,close it
        if (navMenu.classList.contains("open")) {
            toggleNav();
        }
        // if menuItemHasChildren is expanded , collapse it
        if (navMenu.querySelector(".menu-item-has-children.active")) {
            collapseSubMenu();
        }
    }

    window.addEventListener("resize", function () {
        if (this.innerWidth > mediaSize) {
            resizeFix();
        }
    });

})();

/* fin script de navbar  */



/*SCRIPT CARRITO DESDE AQUI*/

/*esto de aqui son las clases que deben ocupar las cards nuestras, para el correcto funcionamiento y no hayan errores
/*<section class="shop-section">
      <div class="card-wrapper">
        <div data-id="1" class="card-item">
          <img src="\img\pic1.jpeg" />
          <div class="details">
            <h3>Item Name</h3>
            <p>
              <span
                >Lorem ipsum dolor sit amet, consectetur adipisicing elit.</span>
              <span class="price">Price: $23.44</span>
              <span class="add-to-cart-btn">Add To Cart</span>
            </p>
          </div>
        </div>
      </div>
</section>*/




class CartItem {
    constructor(name, desc, img, price) {
        this.name = name
        this.desc = desc
        this.img = img
        this.price = price
        this.quantity = 1
    }
}

class LocalCart {
    static key = "cartItems"

    static getLocalCartItems() {
        let cartMap = new Map()
        const cart = localStorage.getItem(LocalCart.key)
        if (cart === null || cart.length === 0) return cartMap
        return new Map(Object.entries(JSON.parse(cart)))
    }

    static addItemToLocalCart(id, item) {
        let cart = LocalCart.getLocalCartItems()
        if (cart.has(id)) {
            let mapItem = cart.get(id)
            mapItem.quantity += 1
            cart.set(id, mapItem)
        }
        else
            cart.set(id, item)
        localStorage.setItem(LocalCart.key, JSON.stringify(Object.fromEntries(cart)))
        updateCartUI()

    }

    static removeItemFromCart(id) {
        let cart = LocalCart.getLocalCartItems()
        if (cart.has(id)) {
            let mapItem = cart.get(id)
            if (mapItem.quantity > 1) {
                mapItem.quantity -= 1
                cart.set(id, mapItem)
            }
            else
                cart.delete(id)
        }
        if (cart.length === 0)
            localStorage.clear()
        else
            localStorage.setItem(LocalCart.key, JSON.stringify(Object.fromEntries(cart)))
        updateCartUI()
    }
}


const cartIcon = document.querySelector('.fa-cart-arrow-down')
const wholeCartWindow = document.querySelector('.whole-cart-window')
wholeCartWindow.inWindow = 0
const addToCartBtns = document.querySelectorAll('.add-to-cart-btn')
addToCartBtns.forEach((btn) => {
    btn.addEventListener('click', addItemFunction)
})

function addItemFunction(e) {
    const id = e.target.parentElement.parentElement.parentElement.getAttribute("data-id")
    const img = e.target.parentElement.parentElement.previousElementSibling.src
    const name = e.target.parentElement.previousElementSibling.textContent
    const desc = e.target.parentElement.children[0].textContent
    let price = e.target.parentElement.children[1].textContent
    price = price.replace("Price: $", '')
    const item = new CartItem(name, desc, img, price)
    LocalCart.addItemToLocalCart(id, item)
    console.log(price)
}


cartIcon.addEventListener('mouseover', () => {
    if (wholeCartWindow.classList.contains('hide'))
        wholeCartWindow.classList.remove('hide')
})

cartIcon.addEventListener('mouseleave', () => {
    // if(wholeCartWindow.classList.contains('hide'))
    setTimeout(() => {
        if (wholeCartWindow.inWindow === 0) {
            wholeCartWindow.classList.add('hide')
        }
    }, 500)

})

wholeCartWindow.addEventListener('mouseover', () => {
    wholeCartWindow.inWindow = 1
})

wholeCartWindow.addEventListener('mouseleave', () => {
    wholeCartWindow.inWindow = 0
    wholeCartWindow.classList.add('hide')
})


function updateCartUI() {
    const cartWrapper = document.querySelector('.cart-wrapper')
    cartWrapper.innerHTML = ""
    const items = LocalCart.getLocalCartItems()
    if (items === null) return
    let count = 0
    let total = 0
    for (const [key, value] of items.entries()) {
        const cartItem = document.createElement('div')
        cartItem.classList.add('cart-item')
        let price = value.price * value.quantity
        price = Math.round(price * 100) / 100
        count += 1
        total += price
        total = Math.round(total * 100) / 100
        cartItem.innerHTML =
            `
        <img src="${value.img}"> 
                       <div class="details">
                           <h3>${value.name}</h3>
                           <p>${value.desc}
                            <span class="quantity">Quantity: ${value.quantity}</span>
                               <span class="price">Price: $ ${price}</span>
                           </p>
                       </div>
                       <div class="cancel"><i class="fas fa-window-close"></i></div>
        `
        cartItem.lastElementChild.addEventListener('click', () => {
            LocalCart.removeItemFromCart(key)
        })
        cartWrapper.append(cartItem)
    }
    // si carrito le le aplico remove a los items dentro de el, subtotal = total, = cero.
    if (count > 0) {
        cartIcon.classList.add('non-empty')
        let root = document.querySelector(':root')
        root.style.setProperty('--after-content', `"${count}"`)
        const subtotal = document.querySelector('.subtotal')
        subtotal.innerHTML = `SubTotal: $${total}`
    }
    else  // si carrito le le aplico remove a los items dentro de el, subtotal = total, = cero.
        cartIcon.classList.remove('non-empty')
    const subtotal = document.querySelector('.subtotal')
    subtotal.innerHTML = `SubTotal: $ ${total}`


}
document.addEventListener('DOMContentLoaded', () => { updateCartUI() })




