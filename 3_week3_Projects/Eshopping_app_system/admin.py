from user import Admin

class AdminManager:
    def __init__(self, store):
        self.store = store

    def view_all_admins(self):
        print("\nAll Admins:")
        for idx, admin in enumerate(self.store.admins):
            print(f"{idx + 1}. {admin.email}")

    def register_admin(self, email, password):
        new_admin = Admin(email, password)
        self.store.admins.append(new_admin)
        print(f"Admin {email} registered successfully.")

    def remove_admin(self, index):
        if 0 <= index < len(self.store.admins):
            admin = self.store.admins.pop(index)
            print(f"Admin {admin.email} removed successfully.")
        else:
            print("Invalid admin.")
