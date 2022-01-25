
## Table Of Content
1. [ **Testing User Stories**](#testing-user-stories)
    - [*First Time Visitor Goals*](#first-time-visitor-goals)
    - [*Frequent User Goals*](#frequent-user-goals)
    - [*Product Manager Goals*](#product-manager-goals)
2. [ **Further Testing**](#further-testing)
3. [ **Known Bugs**](#known-bugs)
4. [ **Resolved Bugs**](#resolved-bugs)
5. [ **Security**](#security)
6. [ **Code Validation**](#code-validation)
    - [*W3C Markup Validator*](#w3c-markup-validator)
    - [*W3C CSS Validator*](#w3c-css-validator)
    - [*PEP8 Online*](#pep8-online)
    - [*JSHint*](#jshint)
7. [ **Lighthouse Testing**](#lighthouse-testing)
    - [*Home*](#home)
    - [*Bag*](#bag)
    - [*Checkout*](#checkout)
    - [*Contact*](#contact)
    - [*Product*](#product)
    - [*Product Detail*](#product-detail)
    - [*Profile*](#profile)

---
## Testing User Stories
---

### First Time Visitor Goals
- "As a first time visitor, at the first look, I want to understand what the   site is all about. for example, wich products you can purchase here."
    - When I enter the site i'm greeted by the websites logo, a text underneath the logo, with a short explanation of the site, and a button that takes me to the products. 

- "As a first time visitor, I want the site to be easliy navigated, I would like to find what i'm searching for quick and easy."
    - I can easily navigate myself across the site using the navbar at the top of the screen. When shown on small & medium devieces the navbar collapses into a burger menu. The navbar is fixed to the top of the page. So it follows me when i'm navigating my way further down all the diffrent pages. 

- "As a first time visitor, I want the site to be well structred the sites features should be where there expected to be."
    - The navigationbar is at the top, where I can use a searchbar, go to account pages, see bag, and navigate between categorys. 
    - Buttons having a consitancy in coloring.
    - Footer has extra information.

- "As a first time visitor, I would like the site to look clean and modern. Good color matching, readble texts etc."
    - The text is easy to read, the color matching is good and consistant. 

- "As a first time visitor, I Would like to register to the page."
    - By clicking the account link in the navbar or the "Sign up" link in the footer I get to the register page. Here I'm asked to type in my email adress, choose a username, and choose a password. 
    - By leaving one of these field empty will result in an error, telling me to fill out that field. 
    - If I dont match either my email adress or password, it will throw an error saying they must match. 
    - If I dont use an password with at least 8 characters it will throw an error saying "This password is too short. It must contain at least 8 characters.". 
    - I fill in all the field correctly and then I click the sign up button. I now get a message telling me to verify my email adress.
    - I go to the confirmation email, clicking the link to confirm my email. I get back to the site, asked if this email belongs to the users that was just created. I click the "Confirm" button, and now I'm registred.  

-  "As a first time visitor, I want to be able to contact the site owner if I have a problem or just need some information."
    - Down at the footer I can see various way to contact the store owners. Either the old fanshioned way, by sending a letter to there adress or just by calling their phone under their opening hours. 
    - If I want to send an email I can click on the "Contact Us" link down at the footer, in the "Customer Support" section. 
    - Well at that page, I can enter my name, email, subject and my message to send a mail to the owners. 
    - Leaving any of the fields empty or not correctly filled, will throw an error, telling me to fill it out correctly. 
    - I fill it out correctly and click the send button, I get a top right message, saying that my message was sent. 


### Frequent User Goals
- "As a Frequent User, I Like the login process to be smooth."
- "As a Frequent User, I would like to access a profile page to manage my order history, and save personal details."
- "As a Frequent User, I want to search for specific products on the site."
- "As a Frequent User, I want to search for a specific category on the site."
- "As a Frequent User, I would like to add products to my bag easily."
- "As a Frequent User, I would like to remove/update products in my bag."
- "As a Frequent User, I want to see the shopping bag total amount all the time."
- "As a Frequent User, I want to review my bag before checkout."
- "As a Frequent User, I want to View confirmation of order before completing purchase."
- "As a Frequent User, I want to easily enter my payment information, so that the checkout is quick and easy."
- "As a Frequent User, I want to feel that my payment and personal information is secured."
- "As a Frequent User, I would like to get better shipping prices as my bags total increases."
### Product Manager Goals
- "As a Product Manager, I Would like to add products easily."
- "As a Product Manager, I Would like to edit/update products easily."
- "As a Product Manager, I Would like to delete products easily."

---
## Further Testing
---

## Known Bugs 
---

## Resolved Bugs
---

## Security
---
## Code Validation
---
### [W3C Markup Validator](https://validator.w3.org/)

- [Home](img-readme/home_html.png)
- [Bag](img-readme/bag_html.png)
- [Checkout](img-readme/checkout_html.png)
- [Contact](img-readme/contact_html.png)
- [Products](img-readme/products_html.png)
- [Product Detail](img-readme/product_detail_html.png)
- [Profile](img-readme/profile_html.png)
- [Add](img-readme/add_html.png)
- [Edit](img-readme/edit_html.png)


### [W3C CSS Validator](https://jigsaw.w3.org/) 
The code was validated by direct input.
- [base.css](img-readme/base_css.png)
    - [*Warnings*](img-readme/base_warnings_css.png) due to imported fonts from google, and copied text from Code Institutes Boutique Ado project.
    
- [bag.css](img-readme/bag_css.png)
- [checkout.css](img-readme/checkout_css.png)
- [contact.css](img-readme/contact_css.png)
- [home.css](img-readme/home_css.png)
- Product
    - [products.css](img-readme/products_css.png)
    - [product_detail.css](img-readme/product_detail_css.png)
    - [add_edit_product.css](img-readme/add_edit_product_css.png)
- [profile.css](img-readme/profile_css.png)


### [PEP8 Online](http://pep8online.com/)
- Validation for Python Code
    - [Home](img-readme/home_views.png)
    - [Bag](img-readme/bag_views.png)
    - [Checkout](img-readme/checkout_views.png)
    - [Contact](img-readme/contact_views.png)
    - [Product](img-readme/product_views.png)
    - [Profile](img-readme/profile_views.png)
    - [Subscribe](img-readme/sub_views.png)

### [JSHint](https://jshint.com/)
- Validation for javascript code
    - [back_to_top.js](img-readme/back_to_top_js.png)
    - [countryfield.js](img-readme/countryfield_js.png)
    - [dot_hover.js](img-readme/dot_hover_js.png)
    - [load_more.js](img-readme/load_more_js.png)
    - [sort_selector.js](img-readme/sort_selector_js.png)
    - [stripe_elements.js](img-readme/stripe_elements_js.png)


---
## Lighthouse Testing
---
### Home 
- [Desktop](pdf/home_desktop.pdf)
- [Mobile](pdf/home_mobile.pdf)
### Bag 
- [Desktop](pdf/bag_desktop.pdf)
- [Mobile](pdf/bag_mobile.pdf)
### Checkout
- [Desktop](pdf/checkout_desktop.pdf)
- [Mobile](pdf/checkout_mobile.pdf)
### Contact 
- [Desktop](pdf/contact_desktop.pdf)
- [Mobile](pdf/contact_mobile.pdf)
### Product 
- [Desktop](pdf/product_desktop.pdf)
- [Mobile](pdf/product_mobile.pdf)
### Product Detail 
- [Desktop](pdf/product_detail_desktop.pdf)
- [Mobile](pdf/product_detail_mobile.pdf)
### Profile 
- [Desktop](pdf/profile_desktop.pdf)
- [Mobile](pdf/profile_mobile.pdf)
---
