from django.contrib.auth.models import User

# ARQUIVO USADO PARA QUE OS USUÁRIOS POSSAM FAZER O LOGIN USANDO O EMAIL
# POR PADRÃO O DJANGO USA APENAS O USERNAME

class EmailAuthBackend:
    def authenticate(self, request, email=None, password=None):
        users = User.objects.filter(email=email)
        
        if users.count() == 1: 
            user = users.first()  
            if user.check_password(password):  
                return user
        elif users.count() > 1:  
            return None
        
        return None 
