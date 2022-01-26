
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
    - When I want to Sign In I locate the "Account" link in the upper right corner, same on mobile and on desktop.
    - I click the "Account" link an a dropdown menu is revealed, there I can find the chocice to Sign In.
    - I get to the sign in page, I can sign in by entering my correct email address and passowrd. I Do so and I get a [message](img-readme/toast_success_sign_in.png) that I the sign in was successful.
    - If I type in one or both of my "Sign in" credentials faulty, an [error message](img-readme/signin_fail.png) is displayed at the top of the form.
- "As a Frequent User, I would like to access a profile page to manage my order history, and save personal details."
    - When signed in, I can locate my profile page at the "Account" dropdown menu at the navbar, or at the footer in the customer support section.
    - At my profile page I can save my shipping information by filling out the [form](img-readme/profile_form.png) and click on the "Update Information" button. Now my shipping details is saved, and will be preloaded when at the checkout page. For the shipping details to be preloaded you need to be signed in.
    - If I want to see my [order history](img-readme/profile_order.png), I can do so on the profile page. If I click on the Order Number I will be redirected to a past order confirmation [page](img-readme/profile_past_order_information.png), with a [message](img-readme/profile_past_order.png) saying that this is an old order. 
- "As a Frequent User, I want to search for specific products on the site."
    - At the top right of the navbar I can locate a "Search" link. 
    - I click the link and the search form input reavels itself in a dropdown menu both on mobile and desktop views. 
    - I can now type in what i'm looking for, I enter the keyword "skate" and click on magnifying glass. 
    - I get redirected to a page with my search [results](img-readme/search_keyword.png) displayed. I found 9 products with the keyword of "skate".
- "As a Frequent User, I would like to add products to my bag easily."
    - If I go to a product I want to purchase, I click on the products image to get to it's details.
    - There I can choose the [quantity](img-readme/quantity_input.png) that I want to order, and click the ["Add to bag"](img-readme/add_bag_button.png) Button. And the product is added to my bag and a toast [message](img-readme/toast_bag.png) appears with what I just added. 
    - If I try to order a rediculus amount of a specific product, it will throw an [error](img-readme/quantity_input_fail.png).
    - Or if I try to add nothing to the bag, it will also throw an [error](img-readme/quantity_input_fail2.png)

- "As a Frequent User, I would like to remove/update products in my bag."
    - I go to my current bag item, by clicking on the bag link at the top right of the navigation bar. I'm not satisfied with the amount I've ordered of a product so I decrease the amount and click on the update button. A [message](img-readme/bag_update.png) is displayed saying that my update was successful.
    - I increase the amount and click on the update button. The update was successful once again.
    - If I try to increase the amount to a rediculus number using the input, it will throw an [error](img-readme/bag_bug04.png).
    - Or if I input the number "0" in the input field. I will remove the bag item from the bag.
    - I want to delete a product. I click on the [trash can](img-readme/bag_trash.png) for the product I want to remove. And the product gets [removed](img-readme/bag_removed.png) from the bag 
- "As a Frequent User, I want to see the shopping bags total amount all the time."
    - When I add any product to the bag, the total amount is displayed below the Bag link. Include the shipping. On [desktop](img-readme/bag_total_desk.png), on [mobile](img-readme/bag_total_mobile.png). If I go to any of the pages I fancy on the website, my bags total is always with me at the navbar. 
- "As a Frequent User, I want to review my bag before checkout."
    - Just by clicking the [bag](img-readme/bag_total_desk.png) link at the navbar or by clicking the ["GO TO BAG"](img-readme/go_to_bag.png) button displayed in a toast when adding an item. I can see a preview of my [bags](img-readme/bag_items.png) current items before going to the checkout. 
- "As a Frequent User, I want to view the order before completing purchase."
    - When I'm satisfied with my order, I can click on the [Secure Checkout](img-readme/secure_checkout.png) button to move on. 
    - Here I can see my [order summary](img-readme/checkout_order_sum.png).
- "As a Frequent User, I want to easily enter my payment information, so that the checkout is quick and easy."
    - I check if my order is in place, I fill out my order details and payment credentials, like [this](img-readme/order_pay_details.png), and click on the [complete order](img-readme/complete_order.png) button.
    - A [preloader](img-readme/preloader.png) appears, waiting for respone. 
    - If everything went well, I get to a confirmation [page](img-readme/order_complete.png) saying that the order was a success. I also get a [confirmation email](img-readme/order_confirm.png) to my sent to my email adress.
    - If I dosen't fill out my order details correctley the form will tell me to fill it out, like [this](img-readme/field_error.png) and  if I dont fill out my payment credentials correctly it will also throw an [error](img-readme/card_error.png), saying I need to fill out my card credentials correctly.
- "As a Frequent User, I want to feel that my personal information is secured."
    - I go to my profile page an copies the [adress](img-readme/secure_profile.png). I then sign out and then I paste in the adress and press enter. I get redirected to the sign in page.
    - I go to one of my past orders and copies the [adress](img-readme/secure_profile01.png). I sign out and then I paste in the adress and press enter. Then I'm redirected to a [403 Error](img-readme/secure_profile02.png) page, saying that I'm not allowed to to that.
- "As a Frequent User, I would like to get free shipping as my bags total increases."
    - I can see that I get free shipping if my bags amount is more than $50. So I add an item to see if a get free shipping. And yes, it [looks](img-readme/shipping_price.png) that I it. 
### Product Manager Goals
- "As a Product Manager, I Would like to add products easily."
    - I Sign In as a superuser, and locate the "Product Managment" link in the account dropdown menu. 
- "As a Product Manager, I Would like to edit/update products easily."
- "As a Product Manager, I Would like to delete products easily."

---
## Further Testing
---

## Known Bugs 

---

## Resolved Bugs
1. When updating my bag items by typing in the input area at the bag view. There was no cap on the amount I could choose. (Look [here](img-readme/bag_bug.png)). So I changed [this](img-readme/bag_bug02.png) code little snippet in my "adjust_bag" view. And added [this](img-readme/bag_bug03.png) line of code. So now if the quantity is higher than 99, a [error message](img-readme/bag_bug04.png) is displayed. 
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
