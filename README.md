# **My Tasty Eats**

## Overview

My Tasty Eats is a website that allows members to easily share recipes amoung each other. The users can create and login to an account. Fill out a recipe form and upload their recipe to the site. They also have the ability to delete or edit recipos amd like and comment on other peoples recipes.

View the live project [Here]( https://my-tasty-eats.herokuapp.com/)


![Responsive Design Screenshot](README/assets/responsive-design-screenshot.png)


## User Experience (UX)

### User Stories

As a user I want to:
*	Register my account easily and efficiantly, so that I can post my recipes whilst also having the ability to update and delete them if I wish.
*	Register my account, so that I can interact with other users through the comment section on the site.
*	Easily log in and log out of my account so that I can access my personal information.
*	Find social media links easily so that I can contact the site owner if needed.
*	Easily and comprehensively understand the main purposes and content of the site, so that I can then in turn gain more knowledge and understanding of how to efficiantly use the site.
*	Navigate and explore different areas of the site in order to find content and be aware of the content contained within where I am on the site.
*	Be provided with a summary of all posts organised by the most recent which would appear first so that I can easily navigate through the information contained within, and  then quickly decide which posts are relevent to my needs.
*	Read other users’ posts in full detail and also any comments which are related to those posts so that I can then make an informed decision on whether to review and offer feedback to that user and not repeat other suggestions from previous comments.
*	Clearly see what other recipes users have posted and also have the ability to interact and open a line of communication with other users.
*	See clearly what date a post or comment was created so that I can clearly see how relevant and up to date the information is.
*	Clearly see how many comments are attached to a post before clicking in to the recipe in order to gain an insight into the views and opinions of others in relation to particular recipes.
*	Post my recipes to the site so that I can connect with others and receive feedback on my work.
*	Update and delete my own recipe posts so that I can keep the information up to date or fix any mistakes I may notice.
*	Comment on my own recipe posts so that I can respond and interact with other users’ comments.
*	Access the site on various devices such as desktop, tablet or mobile so that the site is universally accessible to the majority of users and have the ability to be accessed remotely.
*	Understand when an error occurs so that I am given clear feedback on what I should do.
*   As a site admin user, I can log in so that I can manage a supportive online peer code review community by viewing users, profiles, posts and comments, and updating and deleting accordingly.


### Agile Approach in this Project

An Agile Approach was used to develop this site.  That is, each activity was broken down into small bite-sized portions and performed iteratively, so that as it was repeated, it was tweaked and improved on with each cycle.  According to a report from the [Standish Group (2018)](https://standishgroup.myshopify.com/), Agile projects are statistically twice more likely to succeed, and a third less likely to fail than waterfall projects.

To complete the overall aim of the My Tasty Eats idea, 9 Epics were formed (documented under GitHub Issues) and these then were broken down into specific tasks called User Stories.  These User Stories are small, self-contained units of development work designed to accomplish a specific goal.  These User Stories then had acceptance criteria attached for each so that it was clear when the User Stories were achieved as each of these conditions were met.  The acceptance criteria where then further broken down into tasks.  These tasks were the list of actions required to implement the User Story. They described the technical work details and activities to be performed to complete each User Story properly.

**Example:**

    **Epic - User Account**

    User Story - Profile Page:

    As a User, I would like to be able to easily view my profile page so that I can update my account from there and display the information I would like others to see

    Acceptance Criteria 1
    Given that I am a registered user who is logged in
    When I click the Profile link in the navigate bar
    Then I am taken to my profile page and can see my details displayed

    Acceptance Criteria 2
    Given that I am a registered user who is logged in
    When I navigate to my profile page and edit my details
    Then I can click an update button and be alerted that my information was updated successfully.

    Tasks:
    *	create a profile app for users’ functionality
    *	create signal to create a user profile when a new user signs up
    *	link up views & templates & URLs and display link to profile page in nav after user is logged in
    *	display logged in users name on the profile page
    *	create a profile model to add profile picture, contact details such as email
    *	create form to allow users to be able to edit the information displayed on their profile page
    *	add update button for users to click to submit their changes
    *	show success message when user profile update
    *   manually test this works by setting up a test user


Story points estimated the effort required to complete a particular User Story in one iteration.  To create a Product Backlog GitHub Milestones was used to track progress on groups of issues relating to the User Stories.

Timeboxing defined the iteration where the User Stories were developed based on the assigned priority.  The MoSCoW Prioritization technique was used to assign priorities for Product Backlog Items to be completed in a particular time box.  GitHub Labels was used to categories the User Stories into Must Have, Should Have and Could Have. This clearly showed which User Stories were more important to implement first and in what order.  This kept the scope of the project in focus at all times and only implemented what was essential first.

Information radiators in Agile show real-time, informative and straightforward work status.  This project used a Kaban board, which was set up in GitHub Projects ([here](https://github.com/ciaraosull/project-4-django/projects/1)) to help keep track of work to do, in progress and completed.

Within the timeframe work stopped with 83% of the timebox User Story points total of all Must Have and some Should Have prioritised User Stories.  Only 1 Should Have and 3 Could Have were left uncompleted and are documented in the future features section below.


## Features

**This website takes the users stories mentioned above into consideration to create a positive UX.  The users stories are discussed in more detail below with examples of how each is implemented.**


1. **Favicon and logo**

A customised favicon and logo image was created using a free service from [Free Logo Design](https://www.freelogodesign.org/manager/showcase/c3daf13184dd4a90bcb4d07fef3f31d5?product=free).


2. **Header**

On purpose, the Header is fixed at the top of the screen. Light pink was picked for the background and black for the typeface in order to contrast each other and make the text easier to read.

*   Logo

    * The Logo I created for the project is the same as that which I used for the favicon. 
    
    * This logo is positioned in the top right of the navigation bar.
    
    * The logo is designed to have the same pink background colour as the rest of the header and opposite the logo to the left is the website's name.


*   Navigation Bar
    * The navigation bar is likewise located in the header. For larger screens, this is found in the top left corner. The bar contains links to different parts of the website.

    * When screen size drops below set amount the navigation bar changes to a toggle menu.

    * Depending on whether you are logged in or nuot changes what you can see or do with the links in the header.

        ![Header](README/assets/header-screenshot.png)

        ![Header Mobile](README/assets/header-mobile-screenshot.png)


3. **Landing Page**

    * The landing page brings the user straight to the six most recently uploaded recipes.

    * The background of the site is set to white to allow the Images to appear more pleasing to the eye of the user.

    * The posts are paginated every six posts and are listed with the most recent ones at the top. To make it simple for the user to navigate, the pagination is made to display not only the page numbers but also the first, previous, next, and last page.
 
        ![Landing Page](README/assets/about-us-screenshot.png)


4. **Post Detail Page**

Here the User can view the full recipe post, delete or edit the post if they are the post creator. the user can also add a comment to the post and like it either.

![Post Detail View](README/assets/post-detail-screenshot.png)



12. **Register, Sign In & Log Out**

As described in the future features section of this README, it is hoped that this project will be expanded to provide support for third-party (social) authentication via services like Github or Gmail.  As Django does not support this automatically, allauth was installed and used to create the register, sign in and log out functionality, so the project will already have the foundations in place to expand on this functionality in the future.

At present to register, the user is not required to provide an email address.  This was decided on because there is no use for it yet then the user should not be asked for it at this stage, so their private details are not being stored if they are not needed.  In time as the scope of the project expands, for example, sending email notifications or recovered password functionality, then this may become a requirement for the user to provide.

![Register](README/assets/register-screenshot.png)

![Sign In](README/assets/signin-screenshot.png)

![Log Out](README/assets/logout-screentshot.png)

As previously described, once a user is logged in the navigation bar will change to display the different features the user has access to.

![Success Sign In](README/assets/success-signin-screenshot.png)

![Success Log Out](README/assets/success-signout-screenshot.png)

13. **Admin User**

A superuser was created for this project to manage the administration section.  Admin users have more functionality than regular users and can allow them to create, read, update and delete information such as users, profiles, posts and comments.  

Only approved admin users can access this section of the site and can do so by adding /admin to the URL home page and signing in.  It was decided at this time not to provide a link to this on the site but could be a future feature to allow easier navigation for any admin users. 

![Admin Screenshot](README/assets/admin-screenshot.png)


14. **Footer**
    *   The Footer contains the Connect with Us section.  The background and font colours are kept consistant with the theme of the site.

    *   The GitHub & LinkedIn icons from [Font Awesome](https://fontawesome.com/) open in a new tab and take the user to the respective sites to connect.

    *   The Footer also contains a copyright and the authours name.
        
        ![Footer](README/assets/footer-screenshot.png)



15. **Error Pages**

Custom Error Pages were created to support the professionalism design and ensure appropriate link was added back to the main site to guide users who come across these messages.

* 400 Bad Request - the server cannot process the request due to something that is perceived to be a user error (it may be incorrect or corrupt).
* 403 Page Forbiden - the user does not have permission to access this resource
* 404 Page Not Found - the user requested a page that is not available
* 500 Server Error - internal server error where there is a general problem with the website's server and not the fault of the user


### Features Left to Implement

The scope of this project really can be expanded to great lenghts but within a short time frame the following could be easily implemented:

*   An extra added feature of styling the navigation links when a user is on that page was added.  This was to allow for easy navigation and sign post the user.  However, the 2 section links in the navigation bar About Us & View Posts could not be styled in this was as they did not have a url_name.  It was decided to leave this feature as is for now as the styling is only indicating to the user that they are on a different page.  As the Aout Us and Post View are within the Home Page this seems clear.  However, to change this some solutions to add to add this feature in the future could be using JavaScript and add an event listener and when the section is clicked the active class is then added to it as shown here in [W3Schools](https://www.w3schools.com/howto/howto_js_active_element.asp).  Another optiion would be to use Bootstrap5 [Scrollspy](https://getbootstrap.com/docs/5.2/components/scrollspy/), which could add a nice effect with less code.

*   As described above, using the allauth already installed and set up, support for third-party (social) authentication via services like Github or Gmail so that users can use passwords and accounts to log in to this site instead of creating new ones.  Email notifications and reset password functionality could also be implemented quite easily in a short timeframe.

*   Profile page - to allow users to view each others profile pages and include more information such as user bio.  This could allow users to get more familiar with each other and build up a supportive report.

*   Users history - to allow users to see all the posts they have written and comments on their own user profile page so they can navigate to each one easily without having to find on the site.  This would make it easier for users to update and delete their work.

*   Resize Profile Image - Pillow was installed with the intention of wrintg a function to ensure that the images the users upload as their profile picture are reduced to a certain file size to avoid users uploading images that take up too much space and load faster.  This could be easily implemented next within a short timeframe.

*   Reply to Comments - The comments model could be expanded to include a parent field and then a function to show the child of each of those fields as a reply to each individual comment.  The comment form could be copied and some Javascript used to hide the form and then show on click of a reply icon under each main comment.  This fuctionality would allow better flow to conversations between users.

*   Search functionality - a search box could be included to allow users to search for project posts by language/ library/framework or topic such as website / game / api ect.  The Post model could be expanded to use this as a field topic users can enter the details of the language or framework they used and this then could also be displayed on the post list view or used to filter the views to make the topics shown more relevant to each user.

*   Accessibility & Privacy - an accessibility page and privacy policy page would be important to implement in the next iteration, especially if the users data such as email is to be required and stored.  This is important for users to be able to understand how the site can be adapted for specific accessiblitiy issues and also inform the users of how their date is stored and kept.

*   Report inappropriate comments / projects - this project opted not to allow the comments to be approved before showing due to it not being maintained very regulalry at present.  However, a way for the user to report inappropriate content would be important feture to impliment next, along with either users content having to be approved first and/or profanity checker installed.  This would ensure the community was kept safe and supportive.

*   Likes - it was decided not to use the feature of like or dislike or upvote/downvote on posts to ensure a more supportive and less competitive space for users.  However, a views counter could be implimented to allow users to see how many people have viewed their post to give an indication of how many people might have tested or used it.


## Design

### Data Model

[LucidCharts](www.lucidchart.com) was used to visualise the custom models for this project.  [AllAuth](https://django-allauth.readthedocs.io/en/latest/) was also used for the user authentication system.  This uses the built-in Django User Model.

The Profile model allows users who sign up to have a profile automatically created for them and the user can then update and change their profile information if they wish.  One User has One Profile, so this is a One-to-One relationship with the User’s name acting as the Foreign Key to the User Model.

As each User and their Profile can have many posts, this is represented using the One-to-Many relationship however each post can only have one author.  The author’s name acts as the Foreign Key to the User Model.

Also, every post can have 0 or many Comments and the post acts as the Foreign Key to the Comments & Post Model.  As only one User can be the author of any one comment this is represented by the One-to-One relationship with the User Model and the author of the comment is acting as the Foreign Key for the Comments.

![ERD Image](README/assets/entity-relationship-diagram.png)

Throughout this project, I have opted to use Object-Oriented Programming and Django’s Class-Based Generic Editing Views are used for this.  These are an advanced set of built-in views which are used to implement Create, Retrieve, Update and Delete instances of a table in the database. 

### Wireframes

After the design of the models [Balsamic Wireframes](www.balsamiq.com) were created to visualise the content the user sees and to design a positive UX (as described in more detail in the Features section).  A mobile first approach was used to design the site specifically for mobile use and then the design was altered slightly for desktop view.  [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used with some customised styling to create a unique feel to the site.  [Font Awesome](https://fontawesome.com/) Icons were used throughout the site for reading accessibilty also.

![Mobile Home](README/assets/home-mobile-wireframe.png)

![Desktop Home](README/assets/home-desktop-wireframe.png)

![Mobile Post Detail View](README/assets/post-mobile-wireframe.png)

![Desktop Post Detail View](README/assets/post-desktop-wireframe.png)


### Fonts

The fonts used were Lato, Roboto and sans-serif. Fonts were imported from [Google Fonts](https://fonts.google.com/).

### Colour Scheme

The colour scheme was chosen by using [olorate](https://colorate.azurewebsites.net/). The following palette was chosen for using on the fonts throughout the site due to high contrast for user reading accessibility:

![Colour Pallet](README/assets/colour-pallet.png)