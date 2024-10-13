# Recipe Share

#### Video Demo: [https://youtu.be/6CgBFziR93E]

## Description
Recipe Share is a dynamic web application designed to allow users to share and explore various recipes. The application utilizes Django for the backend, JavaScript for frontend interactivity, and SQLite for the database. Recipe Share provides features such as user authentication, recipe submission, viewing and liking recipes, and following other users. The application is mobile-responsive, ensuring a seamless experience across devices.

## Features
- **Add New Recipes**: Users can submit recipes with titles, ingredients, instructions, and images.
- **Delete Recipes**: Users can delete their own recipes.
- **Like Recipes**: Users can like recipes, and the like count is displayed.
- **Follow Users**: Users can follow and unfollow other users.
- **View Profiles**: Users can view profiles with follower and following counts.
- **Responsive Design**: The application is mobile-responsive.

## Distinctiveness and Complexity

### Distinctiveness
Recipe Share stands out due to its unique combination of features and focus on user interaction within the culinary community. Unlike a typical social network or e-commerce site, it is specifically designed for recipe sharing and discovery. This focus on recipes involves unique requirements such as handling image uploads and rich text formats for recipes, which are not common in generic social media platforms.

Additionally, Recipe Share is not just about posting content; it fosters a community of culinary enthusiasts who can interact with each other through features like liking recipes and following users. This emphasis on community engagement makes Recipe Share distinct from other project submissions in the course, which may focus more on content delivery rather than user interaction and community building.

### Complexity
The complexity of Recipe Share arises from several key aspects:

**User Authentication and Profile Management**: Extending Django's authentication system with custom user profiles required managing user-specific data such as profile pictures, bio, and user interactions (e.g., likes and follows). This necessitated creating additional models and handling complex relationships between them.

**Recipe Submission and Display**: Allowing users to submit recipes involved handling form inputs, file uploads for images, and ensuring that the recipes are displayed in a user-friendly manner. The system needed to validate and sanitize inputs to prevent security issues such as XSS attacks, adding another layer of complexity.

**Interactive Features**: Implementing features like liking recipes and following users required additional database models to track these interactions. Efficiently querying this data to display real-time updates and maintaining the relational integrity between users and their interactions was a challenging task.

**Responsive Design**: Ensuring a seamless experience across various devices involved using CSS and Bootstrap to create a mobile-responsive design. This required careful planning and testing to ensure that all features worked well on different screen sizes and devices.

**Scalability and Performance**: Designing the application to handle a growing number of users and interactions required optimizing database queries and implementing caching where necessary. This ensures that the application remains responsive even under heavy load.

## File Structure

- **app/**: Main application directory.
  - **migrations/**: Database migrations.
  - **static/djangoapp/**: Static content.
    - **css/styles.css**: Main stylesheet.
  - **templates/djangoapp/**: HTML templates.
    - **base.html**: Base template extended by other templates.
    - **index.html**: Home page template.
    - **login.html**: Login page template.
    - **register.html**: Registration page template.
    - **recipe_detail.html**: Single recipe display template.
    - **user_profile.html**: User profile display template.
  - **views.py**: Contains view functions for handling requests and rendering templates.
  - **models.py**: Defines database models for the application.
  - **forms.py**: Defines forms for user registration and recipe submission.
  - **urls.py**: URL configurations for the app.
- **project/**: Project-wide settings and configurations.
  - **settings.py**: Configuration settings for the Django project.
  - **urls.py**: URL configurations for the project.
  - **wsgi.py**: WSGI configuration for deploying the project.
- **manage.py**: Django's command-line utility for administrative tasks.

## Running the Application

### Prerequisites

- Python 3.8+
- Django 3.2.25
- Additional packages listed in `requirements.txt`

### Installation

1. **Clone the repository**:
   ```sh
   git clone https://github.com/Subhash-04/recipe_share.git
   cd recipe_share

2. **Create and activate a virtual environment**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```
3. **Install the dependencies**
    ```sh
    pip install -r requirements.txt
    ```
4. **Apply migrations**
    ```sh
    python manage.py migrate
    ```

5. **Run the development serevr**
    ```sh
    python manage.py runserver
    ```

6. **Open the application in your browser**
    Navigate to `http://localhost:8000` in your web browser.
## Usage

### Adding a New Recipe

1. Click on the **"Submit Recipe"** button.
2. Fill in the recipe title, ingredients, instructions, and upload an image.
3. Click **"Save"** to add the recipe to the list.

### Viewing a Recipe

1. Click on the recipe title from the list of recipes on the home page.
2. View the recipe details including title, ingredients, instructions, and image.
3. You can like the recipe by clicking the **"Like"** button.

### Deleting a Recipe

1. Navigate to your profile by clicking on your username.
2. Click on the recipe you want to delete.
3. Click the **"Delete"** button to remove the recipe.

### Following a User

1. Navigate to another user's profile by clicking on their username.
2. Click the **"Follow"** button to follow the user.

### Liking a Recipe

1. Click on a recipe from the list on the home page.
2. Click the **"Like"** button to like the recipe.

## Conclusion

Recipe Share is a robust platform for culinary enthusiasts, offering a rich set of features, including recipe submission, user interactions through likes and follows, and a responsive design. By leveraging Django for the backend and JavaScript for frontend interactivity, Recipe Share ensures a seamless and dynamic user experience. Whether you are a home cook looking to share your creations or someone seeking new recipes, Recipe Share provides an excellent platform to connect and engage with a community of food lovers.
