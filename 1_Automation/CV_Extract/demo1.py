import nltk

nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def extract_skills(cv_text):
    # Tokenize the text
    words = word_tokenize(cv_text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]
    
    # Define a list of skills
    skills = ["Python", "Java", "C++", "JavaScript", "SQL", "Excel", "R", "C#", "PHP", "Ruby", "C", "Rust", "Swift", "Go", "Django", "Flask", "Express.js", "React", "Vue.js", "Angular", "Node.js", "Backbone.js", "Ember.js", "Meteor.js", "AJAX", "jQuery", "Bootstrap", "Foundation", "Materialize", "Semantic UI", "Bulma", "Tailwind", "Bootstrap Material", "Material-UI", "Element", "Ant Design", "Vuetify", "Quasar", "Tachyons", "Tailwind", "Bootstrap Material", "Material-UI", "Element", "Ant Design", "Vuetify", "Quasar", "Tachyons"]
    
    # Initialize a list to store the found skills
    found_skills = []
    
    # Iterate through the list of skills
    for skill in skills:
        # Check if the skill is in the list of words
        if skill in words:
            # If it is, add it to the list of found skills
            found_skills.append(skill)
    
    # Return the list of found skills
    return found_skills

# Example usage
cv_text = "I am a software developer with experience in Python, JavaScript, and SQL. I have also worked with Excel and C++."
print(extract_skills(cv_text))
