import re

def check_password_strength(password):
    strength_score = 0
    
    if len(password) >= 12:
        strength_score += 2
    elif 12 > len(password) >= 8:
        strength_score += 1
        
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 2      
    if re.search(r"[A-Za-z]", password) or re.search(r"[0-9]", password):
        strength_score += 2
        
    common_passwords = ["123456", "password", "welcome", "querty"]    
    if password in common_passwords:
        strength_score -= 3
        
    print(f"Password strength score: {strength_score}") 
    if strength_score >= 5:
        notice = "Strong password"
    elif 3 <= strength_score <5:
        notice = "Medium password"
    else:
       notice = "Weak password"
     
    return notice   
        
password = input("Enter password: ")    
# if __name__ == "__main__":
#     check_password_strength(password)
    

print(check_password_strength(password))    