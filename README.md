# Maria Zawilska Art

Maria Zawilska Art is a portfolio of a contemporary artist Maria Zawilska as well as the e-commerce website where Maria can sell her original artworks. 
![Am I responsive image](readme_img/responsive.png)  

[Click Here To Visit Live Site](https://maria-zawilska-art-68e0986b160e.herokuapp.com/)

## Table Of Contents:
1. [Design & Planning](#design-&-planning)
    * [Business model](#business-model)
	* [Marketing strategies](#user-stories)
    * [SEO](#seo)
    * [User Stories](#user-stories)
    * [Wireframes](#wireframes)
    * [Agile Methodology](#agile-methodology)
    * [Logo](#logo)
    * [Color Scheme](#color-scheme)
    * [Database Diagram](#database-diagram)
2. [Features](#features)
3. [Future features](#future-features)
4. [Technologies Used](#technologies-used)
5. [Testing](#testing)
6. [Bugs](#bugs)
7. [Deployment](#deployment)
8. [Credits](#credits)
9. [Acknowledgments](#acknowledgments)

## Design & Planning:
Design and planning took into account Maria's 30 years of experience in the fine art world as well as my own research.
The website design is purposefully minimal to allow the visitors to fully focus on the artwork.
Fine art world tends to favour art over matter and look unfavourably upon the artists who are deemed to be focused solely on sales. 
Keeping this in mind I have designed a separate landing page serving as a portfolio and only after choosing to enter the shop tab 
will the user be led to the ecommerce part of the website. To maintain cohesion they are identical in styling yet posses different navbars.
As selling fine art is an artform in itself I have focused on avoiding the overly commercialized look to the store letting the artwork speak for itself.


### Business model
Maria Zawilska Art website will serve double purpose:
- as a portfolio:
   * allowing Maria to keep presence in the world of contemporary fine art
   * introducing new potential collectors to Maria's work
   * as a point of contact for potential galleries and exhibition opportunities
- as a store:
   * allowing Maria to sell her original works
   * with potential expansion in the future into the limited fine art prints
In the future customers  will be able to sign up to the mailing list to receive updates on new works being available in the store.

 ### Marketing 
In the future customers  will be able to sign up to the mailing list to receive updates on new works being available in the store and connect with Maria over the Instagram or Cara.

#### Newsletter: 
In the future customers  will be able to sign up to the mailing list to receive updates on new works being available in the store.

### SEO
-  I have used wordtracker.com to identify short tail and long tail keywords.

### User Stories

#### User
- As a site visitor, I want be able to register for an account so that I can get more access to the website content, and to store my profile information 
- As a site visitor, I want to be able to view a list of the products so that I can select some to purchase 
- As a site visitor, I want to be able to view my shopping bag, so I that can confirm my choices or remove items 
- As a site visitor, I want to be able to view details of the products so that I can learn more about a specific painting 
- As a site visitor, I want to be able to pay for selected products so that I can complete my purchase option 
- As a site visitor, I want to be able to subscribe to a newsletter so that I can receive promotions and information about new products 
- As a site visitor, I want to be able to contact the site owner so that I can get answers to any enquires that I may have about the products or website 


#### Registered user
- As a registered user, I want to be able to reset my password so that I can recover access to my account in case I forget my password
- As a registered user, I want to be able to update my profile and delivery information
- As a registered user, I want to be able to view my order history on the profile page so that I can have better insight of my previous purchases
- As a registered user, I want to be able to change my password

#### Site owner
- As a site owner I want to be able to add, update and delete products directly from the website so I don't have to access admin panel

### Wireframes


### Agile Methodology
[Github project board](https://github.com/users/codebyMai/projects/5/views/1)

### Logo
I have designed the logo in [Canva](https://www.canva.com/) giving it a painterly effect to reflect the nature of the website

### Color scheme
Colour scheme is intentionally minimal to not to detract from the artwork.

### Database 


# Features

### Navigation
### About  
### Gallery
### Shop
### FAQ
### Product page
### Product detail page
### Shopping bag page
### Checkout page
### Contact page
### Footer
### Admin

# Future features

# Technologies used
# Testing

## Code validation
### HTML
The W3C Markup Validation Service 
### CSS
Jigsaw CSS validator 
### JS
JS Hint
## Python
PEP8 CI Python Linter 

## Testing purchase 
## Testing user stories
## Testing features 


# Bugs
## Remaining bugs


# Deployment
###Heroku

### Stripe
- Sign in or create an account with [Stripe](https://stripe.com/gb)
- Click "Developers" from the menu on the left hand side and then "API keys"
- Copy the "Publishable key" and "Secret key"
- Add these to Heroku Config Vars as STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY respectivly.
- Click "Webhooks" from the Developers tab and then "+ Add endpoint"
- Enter the following as the "Endpoint URL":
```
https://'your-website-name'.herokuapp.com/checkout/wh/
```
- Select "Recieve all events" and then "Add endpoint"
- Copy the "Signing secret"
- Add the "Signing secret" to Heroku Config Vars as STRIPE_WH_SECRET

### Steps to clone project
- Click on the code tab under the repository name.
- Then click on "Code" button to the right above the files listed.
- Click on the clipboard icon to copy the URL.
- Open Git Bash in your preferred IDE.
- Change the working directory to where you want your cloned directory.
- Type git clone and then paste the URL that you copied.
- Press enter and clone is complete.
- In the terminal install the requirements by using the following: pip install -r requirements.txt
- Next create the env.py file containing variables to use.
- Add env.py to a .gitignore to prevent it from being pushed to Github
- Make migrations by running : python manage.py makemigrations
- Migrate those changes with python manage.py migrate
- To run the project type python manage.py runserver into the terminal.
- This will open the project locally for you to work on.

### Forking repository on GitHub
- Login to Github and find the repository
- You will find the fork button on the right hand side
- Click on the fork button to copy the repository.

# Credits
- Maria Zawilska for the opportunity to work with her amazing art
- All the photos used were taken by me with the exception of two images of art materials which came from [Pixabay](https://pixabay.com/)
- Product descriptions were written by me with some help from [ChatGPT](https://chatgpt.com/)
- [Code institute](https://codeinstitute.net) Butique Ado walkthrough informed core for my website
- [Stackoverflow](https://stackoverflow.com) for inspiration and solutions to many problems, among them django-countries issue with Django 5.1.4 and Bootstrap5 issue with crispy forms 
- [@CloudWithDjango](https://www.youtube.com/watch?v=fQo9ivqX4xs) - very clear and concise instructions on how to host uploaded images and static files on Cloudinary
- The image conversions from png to webp were done with [Picflow](https://picflow.com)
- @Richard Ash for publishing on Slack his custom solution to uncooperative toast messages in Bootstrap5
- https://www.contemporaryartissue.com/how-to-create-a-professional-artist-website/ https://artprof.org/pro-development/how-to-create-an-artist-website/
- youtube channels [@Codemycom](https://www.youtube.com/@Codemycom), @DennisIvy(https://www.youtube.com/@DennisIvy)helped me to get a better understanding of Django

# Acknowledgments
- I would like to thank my mentor, cohort facilitator and Code Institute.
  
[Back to the top](#Maria Zawilska Art)
