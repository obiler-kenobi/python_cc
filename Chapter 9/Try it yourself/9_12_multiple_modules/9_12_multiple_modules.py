from admin import Admin as ad

admin = ad('oliver', 'arenas', 29, 'oliver@gmail.com')
admin.greet_user()
admin.privilege.privileges = [
    "can add post", 
    "can delete post", 
    "can ban user"
    ]

admin.privilege.show_privileges()