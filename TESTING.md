# Testing


 For any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. A particularly useful form for describing your testing process is via scenarios, such as:


## Navbar

 1.Logo (home button)
    Go to the Navbar and try to press Logotype button (PATRYCJA.IO)
    If it will redirect you to the main/home page it means it works
   
 2. Home button
    Go to the Navbar and try to press home button (HOME)
    If it will redirect you to the main/home page it means it works

 3.Portfolio button.
    Go to the Navbar and try to press portfolio button (PORTFOLIO))
    If it will redirect you to the portfolio page it means it works

 4.Contact button (visible only when admin is logged out)
    Go to the Navbar and try to press contact button (CONTACT)
    If it will redirect you to the contact page it means it works.

 5.Log out button ( appears only when admin is logged in ).
    Log out button shouldn't be visible when admin is logged out.
    Logged out from admin Panel and logout button vanished.
    Contact appeared instead.

## Footer
   Go to social icons and press on every single one if it works.
   If it redirects to social services it works.
   Twitter redirect to main account as it I doesn't have Twitter account.

## Portfolio

   Go to portfolio section and press on particular square presenting project.
   Square should redirect to portfolio view. It redirects to particular project page.

   In project page there is a main photo, after pressing on it, visitor should be redirected to real life project.
   It redirect to project. When Admin is logged in should see "visible go back to admin panel button".
   After logging to admin panel - button is visible and redirects to admin panel.


## Contact form
     Go to the "Contact" page. Try to submit the empty form and verify that an error message about the required fields appears.Try to submit the form with an invalid email address and verify that a relevant error message appears.Try to submit the form with all inputs valid and verify that a success message appears.

 In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

 You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

 If this section grows too long, you may want to split it off into a separate file and link to it from here.