from joboard.models import Candidate
from datetime import datetime
from django.utils.timezone import make_aware

mo = Candidate.objects.create(
    full_name = "Bohdan Romanenko",
    logo_url = "xxx",
    title = "Senior Front-end Developer",
    location =  "Kiev, Ukraine",
    skills =  [{"skill_name": "Node.js"}, {"skill_name": "React.js"}, {"skill_name": "JavaScript"}, {"skill_name": "HTML5"}, {"skill_name": "CSS3"}, {"skill_name": "MongoDB"}, {"skill_name": "JQUERY"}, {"skill_name": "Swagger"}, {"skill_name": "Docker"}, {"skill_name": "PHP"}, {"skill_name": "MySQL"}, {"skill_name": "Laravel"}, {"skill_name": "OOP"}, {"skill_name": "Linux"}, {"skill_name": "PostgreSQL"}, {"skill_name": "UnitTests"}, {"skill_name": "Vue.js"}, {"skill_name": "Angular2"}, {"skill_name": "Design Patterns"}],
    exp = [{
        "title": "Front-end Developer",
        "company": "Epam",
        "start":  make_aware(datetime.strptime("2020-01-01", "%Y-%m-%d")),
        "finish":  make_aware(datetime.strptime("2021-11-30", "%Y-%m-%d")),
        "location": "Kiev, Ukraine",
        "notes": "I have worked at Epam under Front-end apps bla bla bla bla...",
        "is_experience_relevant": True
    },{
        "title": "Full Stack Developer",
        "company": "Luxoft",
        "start":  make_aware(datetime.strptime("2018-01-01", "%Y-%m-%d")),
        "finish":  make_aware(datetime.strptime("2019-12-01", "%Y-%m-%d")),
        "location": "Kiev, Ukraine",
        "notes": "I have worked at Luxoft under Front-end and Back-end apps bla bla bla bla...",
        "is_experience_relevant": 1
    },{
        "title": "Junior Front-end Developer",
        "company": "Daxx",
        "start":  make_aware(datetime.strptime("2016-01-01", "%Y-%m-%d")),
        "finish":  make_aware(datetime.strptime("2017-12-01", "%Y-%m-%d")),
        "location": "Lviv, Ukraine",
        "notes": "I have worked at Daxx under Front-end apps bla bla bla bla...",
        "is_experience_relevant": 1
    },{
        "title": "Account Manager",
        "company": "Zone3000",
        "start":  make_aware(datetime.strptime("2014-01-01", "%Y-%m-%d")),
        "finish":  make_aware(datetime.strptime("2015-12-01", "%Y-%m-%d")),
        "location": "Kharkiv, Ukraine",
        "notes": "I have been Account Manager at Zone3000 bla bla bla bla...",
        "is_experience_relevant": 0
    }],
    exp_total = 95,
    exp_relevant_total = 71,
    exp_last_total = 23,
    educations = [{
        "institution_name": "Lviv Polytechnic National University",
        "location": "Lviv, Ukraine",
        "start":  make_aware(datetime.strptime("2017-01-01", "%Y-%m-%d")),
        "finish":  make_aware(datetime.strptime("2021-11-10", "%Y-%m-%d"))
    },{
        "institution_name": "Lviv Polytechnic College",
        "location": "Lviv, Ukraine",
        "start":  make_aware(datetime.strptime("2014-01-01", "%Y-%m-%d")),
        "finish":  make_aware(datetime.strptime("2016-12-01", "%Y-%m-%d"))
    }],
    about = "Experienced Software Engineer with a demonstrated history of working in the information technology and services industry. Skilled in Amazon Web Services(AWS), MongoDB, Heroku, Javascript, TypeScript and Node.js. Strong information technology professional with a master of science focused in computer engineering from lviv polytechnic national university",
    contacts = {
      "email": "xxx",
      "linkedin": "xxx",
      "skype": "xxx",
      "github": "xxx",
      "fb": "xxx"
    }
)