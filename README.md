<h1 align="center">Skate Shop</h1>

[View the live project here.](https://kagebounshin-skateshop.herokuapp.com/)

<h2 align="center"><img src="img-readme/amIResponsive.png"></h2>

The SkateShop is a place where you can assemble a skateboard of you choice, or just buy single items for you setup. For the already experienced Skater to the more novice once. The company for this E-commerce web application is fictional, and this site is a assignment from [Code Institute](https://codeinstitute.net/). 

## Table Of Content
1.[ **UX**](#user-experience) 
- [**User Stories**](#user-stories)
    - [*First Time Visitor Goals*](#first-time-visitor-goals)
    - [*Frequent User Goals*](#frequent-user-goals)
    - [*Product Manager Goals*](#product-manager-goals)
- [**Strategy**](#strategy)
- [**Structure**](#structure)
    - [*Framework*](#framework)
    - [*Navbar*](#navbar)
    - [*Home*](#home)
    - [*Products*](#products)
    - [*Bag*](#bag)
    - [*Checkout*](#checkout)
    - [*Toast*](#toast)
    - [*Allauth*](#allauth)
    - [*Contact*](#contact)
- [**Skeleton**](#skeleton)
    - [*Wireframes*](#wireframes)
- [**Surface**](#surface)
    - [*Colour Palette*](#colour-palette)
    - [*Colour Scheme*](#colour-scheme)
    - [*Typography*](#typography)
    - [*Imagery*](#imagery)

2.[ **Database Setup**](#database-setup)
- [**Schema**](#schema)
    - [*Account*](#account)
    - [*Category Model*](#category-model)
    - [*Product Model*](#product-model)
    - [*Review Model*](#review-model)
    - [*Contact Model*](#contact-model)
    - [*Subscribe Model*](#subscribe-model)
    - [*Order Model*](#order-model)
    - [*Order Line Item Model*](#order-line-item-model)
    - [*Profile Model*](#profile-model)

3.[ **Features**](#features)
- [**Features For The Future**](#features-for-the-future)

4.[ **Technologies**](#technologies-used)

5.[ **Testing**](#testing)

6.[ **Deployment**](#deployment)
- [**Heroku**](#heroku)
- [**Aws**](#aws)
    - [*Setting Up AWS S3*](#setting-up-aws-s3)
    - [*Setting up AWS Identity and Access Management Configuration*](#setting-up-aws-identity-and-access-management-configuration)

7.[ **Credits**](#credits)
- [**Code**](#code)
- [**Media**](#media)
- [**Acknowledgements**](#acknowledgements)

---

# User Experience

-   ## User stories

    -   ### First Time Visitor Goals
        1. As a first time visitor, at the first look, I want to understand what the site is all about. for example, wich products you can purchase here.
        2.  As a first time visitor, I want the site to be easliy navigated, I would like to find what i'm searching for quick and easy.
        3.  As a first time visitor,  I want the site to be well structred the sites features should be where there expected to be.
        4.  As a first time visitor, I would like the site to look clean and modern. Good color matching, readble texts etc. 
        5.  As a first time visitor, I Would like to register to the page. 
        6.  As a first time visitor, I want to be able to contact the site owner if I have a problem or just need some information.

    -   ### Frequent User Goals
        1. As a Frequent User, I Like the login process to be smooth.
        2. As a Frequent User, I would like to access a profile page to manage my order history, and save personal details. 
        3. As a Frequent User, I want to search for specific products on the site. 
        4. As a Frequent User, I would like to add products to my bag easily.
        5. As a Frequent User, I would like to remove/update products in my bag. 
        6. As a Frequent User, I want to see the shopping bag total amount all the time. 
        7. As a Frequent User, I want to review my cart	before checkout. 
        8. As a Frequent User, I want to view the order before completing purchase.
        9. As a Frequent User, I want to easily enter my payment information, so that the checkout is quick and easy. 
        10. As a Frequent User, I want to feel that my payment and personal information is secured. 
        11. As a Frequent User, I would like to get free shipping as my bags total increases. 

    -   ### Product Manager Goals
        1. As a Product Manager, I Would like to add products easily.
        2. As a Product Manager, I Would like to edit/update products easily.
        3. As a Product Manager, I Would like to delete products easily.

---

-   ## Strategy
    - This site will have it's focus on the already experienced skateboarder, to the more novice one. By having good product descirption and clear instructions on what you need to setup a skateboard, making it easy for the more novice user to assemble their own. Or the users will have the option to buy random gear to their setup in just a few clicks.
---
-   ## Structure
    ### Framework
    - I've choose to go with bootrap as framework for this project. Easy to work with it's responsive grid system, lots of prebuilt components, and great plugins. 
    ### Navbar
    - The navbar will be fixed at the top of the page, so it's always accessible for the user. 
    - On Desktop view, the navbar will have the sites logo to the left, the produt links centered, an the search, account management and the bag links will be displayed to the right.
    - On Mobile and Tablet, the product links and the logo are hidden in a collapsable menu, show them by clicking at the burger menu. The search, account management and the bag links will still be displayed to the right.
    - The search bar will be in a dropdown menu both on deskttop, tablet & mobile view, always accesible and easy for the user to search for a product at any time. 
    - The account management links will be in a dropdown menu, wich will have the choices to register, login, logout, and your own profile page, with order history and personal information.  
    ### Home
    - The homepage, will greet you with the sites brand, and a paragrapf, this should be enough to explain the sites purpose. 
    - Below that, I want to make like a tutorial for how to setup a skateboard properly. explaining step by step what you need to get started. At each step, have the option to go to that specific product. 
    ### Products
    - You will have the choice to display all the product at the same time, or by category. Also display on or more specific products based on your search criteria. The products will have an image, name and a pricing displayed. 
    - Click on a product to read more about that product. Such as a short discripion, sizes etc. Have the option to add it to the bag, with the quantity of your choice. 
    ### Bag
    - If the bag has no item, it will have a text, saying that the bag is empty. And a button directing you back to the shopping page.
    - If you have added something to your bag, you will see the total price displayed next to the bag link at the navbar or below the bag icon on mobile/tablet view.
    - By adding a product, See a quick preview of the bag and it's current products and total amount in a toast at the top right of the screen. 
    - When choosing the option to go to the bag you will be able to increase or decrease the quantity of each item, remove a item from the bag, see the total amount. If your happy with your bag items you can proceed to the checkout page.
    ### Checkout
    - the user's choosen items will be displayed here. You will see the price of your order. The you can enter your shipping credentials and card credentials to complete the order.
    ### Toast
    - Bootsrap has a component called ["Toasts"](https://getbootstrap.com/docs/4.3/components/toasts/), wich is notifications designed to mimic the push notifications.
    - The bag when clicked will show a quick preview of it's current products using the toast component. 
    - The toast component will also display warning, info, success or error messages, giving the user quick feedback, for example, if something unexcpected happens. 
    ### Contact 
    - At the contact page, you will be able to send mails to the sites admin. See other ways to contact the sites admins, and wich time of the day they reachable. 
    - The admin can access these emails from the django admin terminal. 
    ### Allauth 
    - These pages will be clean looking, centered at the page & be easily accessible at all time. 
 
---

- ## Skeleton
    ### Wireframes
    - Mobile
        - [First](wireframes/wireframesMobile1.png)
        - [Second](wireframes/wireframesMobile2.png)
        - [Third](wireframes/wireframesMobile3.png)
    - Tablet
        - [Home](wireframes/tabletHome.png)
        - [Products](wireframes/tabletProduct.png)
        - [Info](wireframes/tabletInfo.png)
        - [Register](wireframes/tabletReg.png)
        - [Sign In](wireframes/tabletSign.png)
        - [Bag](wireframes/tabletBag.png)
        - [Toast](wireframes/tabletToast.png)
        - [Dropdown](wireframes/tabletDrop.png)
        - [Check](wireframes/tabletCheck.png)
    - Desktop
        - [Home](wireframes/wireframeHome.png)
        - [Products](wireframes/wireframeProducts.png)
        - [Info](wireframes/wireframeInfo.png)
        - [Register](wireframes/wireframeReg.png)
        - [Sign In](wireframes/wireframeSign.png)
        - [Bag](wireframes/wireframeBag.png)
        - [Toast](wireframes/wireframeToast.png)
        - [Check](wireframes/wireframeCheck.png)

---

- ## Surface

    ### Colour Palette
    - [Colour Palette](img-readme/skateShopPalette.png)
    ### Colour Scheme
    - The body of this site and the navigationbar is set to have the background color of white (#ffffff). 
    - The footer has two section, the top section has the background color of "Jet" (#333333), the lower part of the footer has the background color of "Eerie Black" (#222222).
    - The site has three different types of CTA ("Call To Action") buttons. 
        - The first [Button](img-readme/ctabutton1.png) has the background color of "Razzmic Berry" (#764C87), and when ["Hovered"](img-readme/ctabutton2.png) the background color eases in to "Russian Violet" (#492857).
        - The secound [Button](img-readme/ctabutton3.png) has the background color of "White" (#fff) with a "Razzmic Berry" (#764C87) colored border & text. When ["Hovered"](img-readme/ctabutton4.png) the background eases in to the "Razzmic Berry" (#764C87) background color, and the text turns "White" (#fff). 
        - The third [Button](img-readme/ctabutton5.png) has the background color of "White" (#fff) with a "Red" (#ff0505) colored border & text. When ["Hovered"](img-readme/ctabutton6.png) the background eases in to the "Rosso Corsa" (#cc0101) background color, and the text turns "White" (#fff).
    ### Typography
    - The fonts I've used for this project are from [Google Fonts](https://fonts.google.com/). The fonts are ["Oswald"](img-readme/mainfont.png) & ["Pacifico"](img-readme/logofont.png).
        - [Oswald](https://fonts.google.com/?query=Oswald&preview.text=Oswald&preview.text_type=custom) has been used as the main font of this project. Looks really good in all the different weights, it's readble. Simpley a fine peace of sans serif typeface. 
        - [Pacifico](https://fonts.google.com/specimen/Pacifico?preview.text=Pacifico&preview.text_type=custom&category=Sans+Serif,Display,Handwriting,Monospace&query=Pacifico) is used for the sites [logo](img-readme/logo.png). The font is inspired by the 1950s American surf culture. Works perfect for this site, becouse the skateboarding sport was created by surfers in San Fransico, CA.
    ### Imagery
    - Products
        - I've choosed images that would help you to quickly indentify a specific product. So images with a white background, product placed at the center of the image. 
    - Other
        - The other images of the website, where choosen to match the theme of the website, in this case, skateboarding. So that the user would get a quick understanding of the sites purpose.

---

# Database Setup

## Schema

A relational database was used to structure this project. A relational database is a collection of data items with pre-defined relationships between them.

<details>
<summary>Selected applications from the Database</summary>

![Schema](img-readme/selected-models.png)

</details>
<br>
<details>
<summary>All applications from the Database</summary>

![Schema](img-readme/all-models.png)

</details>

---

### Account
The allauth Django Account app includes a number of models. I didn't create this models becouse they come with the use of django. It's the base for user authentication.

---

### Category model

Store's the diffrent kinds of product category's on the site. 

| Name | Data Type | Intent |
| ---- | --------- | ------- |
| name | string | The product category's name. |
| friendly_name | string | The product category's name for users.|

---

### Product model

For storing a product's data.

| Name | Data Type | Intent |
| ---- | --------- | ------ |
| category | foreign key | A foreign key wich will indentify wich category the product belongs to. |
| sku | charfield | Numbers to indentify a product. |
| name | string | Product's name. |
| description | string | Product's description. |
| has_sizes | boolean | Product's size. |
| price | decimal | Product's price |
| image_url | string | Product's url. |
| image | string | An image associated with the product. |

---

### Review Model

Review a product from the store if your are logged in.

| Name | Data Type | Intent |
| ---- | --------- | ------ |
| Product | foreign key | Get the current product |
| user | foreign key | Get the logged in user |
| review_title | string | The Review name. |
| review | string | The users review |
| review_rating | string | Review product from 1 to 5 |
| date | date | The date the review was made. |

---

### Contact Model

Store messages sent from the contact page. 

| Name | Data Type | Intent |
| ---- | --------- | ------ |
| full_name | string | The Contactor full name |
| email_address | string | The Contactor email adress |
| subject | string | The Subject for the message |
| message | string | The contactors message |

---

### Subscribe Model

Store emails for newletter. 

| Name | Data Type | Intent |
| ---- | --------- | ------ |
| email | string | User's email adress |

---

### Order Model

Stores the order details, also connected to the users profile & order line item model.

| Name | Data Type | Intent |
| ---- | --------- | ------ |
| order_number | string | Created an unique order number, using UUID. |
| user_profile | foreign key | A foregin key related to the users profile. |
| full_name | string | The user's full name. |
| email | string | The user's email address. |
| phone_number | string |  The user's phone number. |
| country | string | The user's country. |
| postcode | string | The user's postcode. |
| town_or_city | string | The user's town or city. |
| street_address1 | string | The user's address |
| street_address2 | string | The user's 2nd line of the address |
| county | string | The user's county. |
| date | date object | Date of the order |
| delivery_cost | decimal | The delivery cost base on the price |
| order_total | decimal | The total of the ordered products |
| grand_total | decimal | The total price of the entire order |
| original_bag | string | The user's shopping bag in stringformat. |
| stripe_pid | string | The user's stripe pid. |

---

### Order Line Item Model

Stores the details of each unique product in the order, if the order have more than one of the same product, it stores those as 1 line item but increases the quantity of that product.

| Name | Data Type | Intent |
| ---- | --------- | ------ |
| order | foreign key | A foreign key related to the order. |
| product | foreign key | A foreign key related with a product. |
| product_size | string | products size |
| quantity | integer | The product quantity |
| lineitem_total | decimal | The total price. |

---

### Profile Model

Stores users billing information.

| Name | Data Type | Intent |
| ---- | --------- | ------ |
| user | foreign key | A one to one relationship between the profile model and the allauth User model |
| default_phone_number | string | User's phone number. |
| default_street_address1 | string | User's address. |
| default_street_address2 | string | User's 2nd line of the address |
| default_town_or_city | string | User's town or city. |
| default_postcode | string | User's postcode. |
| default_county | string | User's county. |
| default_country | string | User's country |

---

## Features


### Features for the future 

---

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://www.javascript.com/)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

- [jQuery](https://jquery.com/) 

- [PostgreSQL](https://www.postgresql.org/) - Used to create relational databases

- [Bootstrap](https://getbootstrap.com/) - Front-end toolkit

- [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - Jinja was used with flask in the HTML code. For simple linking between the backend and frontend. 

- [Heroku](https://id.heroku.com/login) - Heroku was used as the hosting platform to deploy my project.

- [FontAwesome](https://fontawesome.com/) - Provides icons across the site

- [icons8](https://icons8.com/) - Icons for Shop By Category section.

- [GoogleFonts](https://fonts.google.com/) - Used for the sites typography

- [Git](https://git-scm.com/) - Git was used for version control.

- [GitHub](https://github.com/) - GitHub was used to store the project.

- [Balsamiq](https://balsamiq.com/) - Balsamiq was used to create the wireframes.

- [Am I Responsive](http://ami.responsivedesign.is/#) - Tested responsivness & the images at the top of the readMe.

- [Lighthouse](https://developers.google.com/web/tools/lighthouse) - Lighthouse was used to test the performanceof the website.

- [CSS Gradient](https://cssgradient.io/) - Linear Gradient Helper

- [favicon](https://favicon.io/) - Sites favicon

- [Coolors](https://coolors.co/) - For creating the colorpalette at the Design section of this README

- [Unsplash](https://unsplash.com/s/photos/skateboarders) - Images for the homepage

- [Tinyjpg](https://tinyjpg.com/) - Resizing images

---

# Testing

[**Test Docmentation**](TESTING.md)

---

# Deployment
The site was deployed to Heroku. Following the steps below.

## Heroku

1. Log in to [Heroku](https://dashboard.heroku.com/apps) and create an account and a new Heroku application, and select the region that is closest to you.
2. In the __Resourses__ tab at your desktop provision a new Postgres database. Search for ```Heroku Postgres```, and add it to your project, like [this](img-readme/heroku_deploy.png).
3. Move back to your IDE and ```pip install dj_database_url``` & ```pip install psycopg2-binary``` to access the use of the postgres database.
4. Then run: 
```
pip3 freeze > requirements.txt
```
5. In the projects ```settings.py``` file, add the following lines:

```
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

```
6. Create a superuser with:
```
python3 manage.py createsuperuser
```
7. Then install gunicorn with:
```
pip3 install gunicorn
```
8. Then run: 
```
pip3 freeze > requirements.txt
```
9. Create a Procfile, and add the following to it:
```
web: gunicorn appname.wsgi:application
```
10. Temporarily disable COLLECTSTATIC by running:
```
heroku config:set  DISABLE_COLLECTSTATIC=1 --app username-appname
```
11. Add the applications __Heroku__ hostname to __ALLOWED_HOSTS__ in ```settings.py``` 
```
ALLOWED_HOSTS = ['username-appname.herokuapp.com',]
```
12. Add a __SECRET_KEY__ config variable in Heroku settings.

13. ```git push``` your changes, then initialize a heroku git remote by running:
```
heroku git:remote -a username-appname
```
14. Push to heroku master deploy by running:
```
git push heroku main
```
15. Go to your __Deploy__ tab in Heroku to set up automatic deployments by connecting to your github repository. Look [here](img-readme/heroku_deploy01.png)

---

## AWS

### Setting Up AWS S3

1. Go to [Amazon](https://aws.amazon.com/) and set up your AWS account.
2. Search for S3 in the AWS Managment Console under "My Account".
3. Open S3 and create a new "Bucket", for best practices, name your bucket like your __Heroku__ appname. 
```
username-appname
```
4. Select the region closest to your location.
5. Uncheck "Block all public access" and aknowledge that the bucket will be public.
6. The click "Create Bucket".
7. Go to __Properties__ inside your newly created bucket, and enable "Static website hosting".
8. Go to the bucket's __Permisions__ tab, add the following to the CORS confiquration:
```
[
    {
        "AllowedHeaders": [
            "Authorization"
        ],
        "AllowedMethods": [
            "GET"
        ],
        "AllowedOrigins": [
            "*"
        ],
        "ExposeHeaders": []
    }
]
```
9. Still in the bucket's __Permisions__ tab, at the "Bucket Policy" tab, click on "Policy generator" and create a new policy which should then be added to the "Bucket Policy".
10. Still in the bucket's __Permisions__ tab, at the "Access Control List" tab, check the list objects box under the "Everyone (public access)" header.

---

### Setting up AWS Identity and Access Management Configuration

1. Go to services and click on IAM.
2. In the IAM dashboard click to the __"User Groups"__ tab and create a new group.
3. In the IAM dashboard click to the __"Policies"__, tab and create a new policy. 
4. Go to the JSON tab and then click on __"Import managed policy"__.
5. Select the __S3FullAccess__ policy and click on import.
4. Edit the imported JSON code to allow full access to the your bucket and its' associated files, using the your bucket's ARN. You can find the ARN in __Permissons__ in your bucket, in the __"Bucket Policy"__ tab.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": [
                "arn:aws:s3:::your-arn",
                "arn:aws:s3:::your-arn/*"
            ]
        }
    ]
}
```
5. Click on __"Review Policy"__, give the policy a name and description and then create the policy.
6. Go back to the IAM dashboard, click the __"User groups"__ tab, click on the your newly created group. Then go to the __"Permissions"__, click the dropdown menu __"Add permission"__ and then __"Attach Policies"__. Then click the checkbox on the policy that was just created and then click to __"Add permissions"__.
7. Go back to the IAM dashboard, click the __"Users"__ tab, click on __"Add Users"__, select a username, check the box for __"Programmatic access"__ the select next.
8. Add the newly created user to your group, click the next button til the end, then click __"Create User"__.
9. Download the CSV file, it containing the new user's access key and secret access key in order to add them to Django and authenticate this user.
10. ```pip3 install boto3``` & ```pip3 install django-storages``` in your IDE.
11. Then run: 
```
pip3 freeze > requirements.txt
```
12. Then add 'storages', to the installed apps list in ``````settings.py``````
13. Add the following AWS config variables to the ``````settings.py`````` to use if you have the __USE_AWS__ varibale in os.environ:
```
if 'USE_AWS' in os.environ:
    AWS_STORAGE_BUCKET_NAME = 'Your_Bucket_Name'
    AWS_S3_REGION_NAME = 'Your_Region'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
``` 
14. Add the Access Keys and USE_AWS=True to the __Heroku__ config variables.
15. Commit these changes and push, the build will collect all the Static files and place them in the S3 bucket and Heroku will then serve them successfully.
16. Go back to your S3 Bucket, create a new folder in the S3 bucket called Media and set __"Permissons"__ to grant __"Public-read Access"__.
17. Then upload all the images for your app into that folder.

---

## Github

### Forking the GitHub Repository

By forking the GitHub Repository you can make a copy of the original repository to your GitHub account to just view or make changes without affecting the original. Use these steps or press this [link](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo).

1. Log in to [GitHub](https://github.com/) and locate the [GitHub Repository](https://github.com/Kagebounshin/skateshop).
2. In the top-right corner of the page, click Fork.
3. Now you will have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

# Credits

### Code
### Media
### Acknowledgements

### Disclaimer
For educational purpose only!