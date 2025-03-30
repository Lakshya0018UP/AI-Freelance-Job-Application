from app import db 
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime

class Jobs(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    description=db.Column(db.Text,nullable=False)
    budget=db.Column(db.Float,nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    skills=db.Column(db.String(200),nullable=False)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    

    def to_json(self):
        return{
            "id":self.id,
            "title":self.title,
            "description":self.description,
            "budget":self.budget,
            "created_at": self.created_at,
            "skills":self.skills,
            "user_id":self.user_id
        }
    
class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    name=db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False)  # Freelancer, Professional, Admin

    def set_password(self,password):
        self.password_hash=generate_password_hash(password)

    def check_password(self,password):
         return check_password_hash(self.password_hash, password)
    
    def to_json(self):
        return{
            "id":self.id,
            "name":self.name,
            "username":self.username,
            "email":self.email,
            "password_hash":self.password_hash,
            "role":self.role
        }
    

class Applied(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    job_id=db.Column(db.Integer,db.ForeignKey('jobs.id'),nullable=False)
    username=db.Column(db.String(80),nullable=False)
    name=db.Column(db.String(100),nullable=False)
    email=db.Column(db.String(120),nullable=False)
    date_created=db.Column(db.DateTime,default=datetime.utcnow())
    status=db.Column(db.String(20),default='applied')
    proposal=db.Column(db.Text,nullable=False)
    freelancer_id=db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
    bid_amount=db.Column(db.Float,nullable=False)

    def to_json(self):
        return{
            "id":self.id,
            "job_id":self.job_id,
            "username":self.username,
            "name":self.name,
            "email":self.email,
            "date_created":self.date_created,
            "status":self.status,
            "proposal":self.proposal,
            "freelancer_id":self.freelancer_id,
            "bid_amount":self.bid_amount


        }
    
